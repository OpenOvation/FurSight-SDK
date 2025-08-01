/**
 * FurSight SDK Forms
 * 
 * Form building and validation utilities for the FurSight Pet Adoption API
 */

import { FurSightClient } from './client';
import {
  AdopterProfile,
  DogProfile,
  FormData,
  PredictionResponse,
  DropdownValues,
  SampleData,
  FieldInfo,
  FormTemplate
} from './types';
import { ValidationError } from './errors';

/**
 * High-level form builder for pet adoption predictions
 */
export class AdoptionForm {
  private client: FurSightClient;
  private adopterData: Partial<AdopterProfile> = {};
  private dogData: Partial<DogProfile> = {};
  private dropdownValues: DropdownValues | null = null;
  private sampleData: SampleData | null = null;

  /**
   * Initialize the adoption form
   * 
   * @param client - FurSightClient instance for API communication
   */
  constructor(client: FurSightClient) {
    this.client = client;
  }

  /**
   * Get all available dropdown values for form fields
   */
  async getDropdownValues(): Promise<DropdownValues> {
    if (this.dropdownValues === null) {
      this.dropdownValues = await this.client.getDropdownValues();
    }
    return this.dropdownValues;
  }

  /**
   * Get sample form data for testing
   */
  async getSampleData(): Promise<SampleData> {
    if (this.sampleData === null) {
      this.sampleData = await this.client.getSampleData();
    }
    return this.sampleData;
  }

  /**
   * Set an adopter field value
   * 
   * @param fieldName - Name of the adopter field
   * @param value - Field value
   * @returns Self for method chaining
   */
  setAdopterField(fieldName: keyof AdopterProfile, value: any): AdoptionForm {
    this.adopterData[fieldName] = value;
    return this;
  }

  /**
   * Set a dog field value
   * 
   * @param fieldName - Name of the dog field
   * @param value - Field value
   * @returns Self for method chaining
   */
  setDogField(fieldName: keyof DogProfile, value: any): AdoptionForm {
    this.dogData[fieldName] = value;
    return this;
  }

  /**
   * Set multiple adopter fields at once
   * 
   * @param data - Dictionary of adopter field values
   * @returns Self for method chaining
   */
  setAdopterData(data: Partial<AdopterProfile>): AdoptionForm {
    this.adopterData = { ...this.adopterData, ...data };
    return this;
  }

  /**
   * Set multiple dog fields at once
   * 
   * @param data - Dictionary of dog field values
   * @returns Self for method chaining
   */
  setDogData(data: Partial<DogProfile>): AdoptionForm {
    this.dogData = { ...this.dogData, ...data };
    return this;
  }

  /**
   * Load sample data into the form for testing
   * 
   * @returns Self for method chaining
   */
  async loadSampleData(): Promise<AdoptionForm> {
    const sample = await this.getSampleData();

    // Split sample data into adopter and dog fields
    for (const [fieldName, value] of Object.entries(sample)) {
      if (fieldName.startsWith('adopter_')) {
        this.adopterData[fieldName as keyof AdopterProfile] = value;
      } else if (fieldName.startsWith('dog_')) {
        this.dogData[fieldName as keyof DogProfile] = value;
      }
    }

    return this;
  }

  /**
   * Validate a single field value against dropdown constraints
   * 
   * @param fieldName - Name of the field to validate
   * @param value - Value to validate
   * @returns True if valid
   * @throws ValidationError if validation fails
   */
  async validateField(fieldName: string, value: any): Promise<boolean> {
    const dropdownValues = await this.getDropdownValues();

    if (fieldName in dropdownValues) {
      const allowedValues = dropdownValues[fieldName];
      if (allowedValues && allowedValues.length > 0 && !allowedValues.includes(String(value))) {
        const preview = allowedValues.slice(0, 5);
        const suffix = allowedValues.length > 5 ? '...' : '';
        throw new ValidationError(
          `Field '${fieldName}' must be one of: ${preview.join(', ')}${suffix}. Received: '${value}'`
        );
      }
    }

    return true;
  }

  /**
   * Validate all form data
   * 
   * @returns True if all data is valid
   * @throws ValidationError if validation fails
   */
  async validate(): Promise<boolean> {
    // Validate adopter fields
    for (const [fieldName, value] of Object.entries(this.adopterData)) {
      if (value !== null && value !== undefined) {
        await this.validateField(fieldName, value);
      }
    }

    // Validate dog fields
    for (const [fieldName, value] of Object.entries(this.dogData)) {
      if (value !== null && value !== undefined) {
        await this.validateField(fieldName, value);
      }
    }

    // Check for required fields
    if (Object.keys(this.adopterData).length === 0 && Object.keys(this.dogData).length === 0) {
      throw new ValidationError('Form must contain at least some adopter and dog data');
    }

    return true;
  }

  /**
   * Get validated adopter profile
   */
  getAdopterProfile(): AdopterProfile {
    return this.adopterData as AdopterProfile;
  }

  /**
   * Get validated dog profile
   */
  getDogProfile(): DogProfile {
    return this.dogData as DogProfile;
  }

  /**
   * Submit the form and get prediction results
   * 
   * @param includeExplanation - Whether to include detailed explanation
   * @returns Prediction response
   * @throws ValidationError if form data is invalid
   */
  async submit(includeExplanation: boolean = true): Promise<PredictionResponse> {
    // Validate before submission
    await this.validate();

    // Submit to API
    return this.client.predictSingle(
      this.adopterData as AdopterProfile,
      this.dogData as DogProfile,
      includeExplanation
    );
  }

  /**
   * Generate adopter letter from current form data
   * 
   * @returns Generated adopter letter text
   */
  async generateAdopterLetter(): Promise<string> {
    const combinedData: FormData = { ...this.adopterData, ...this.dogData };
    return this.client.generateAdopterLetter(combinedData);
  }

  /**
   * Generate dog profile from current form data
   * 
   * @returns Generated dog profile text
   */
  async generateDogProfile(): Promise<string> {
    const combinedData: FormData = { ...this.adopterData, ...this.dogData };
    return this.client.generateDogProfile(combinedData);
  }

  /**
   * Clear all form data
   * 
   * @returns Self for method chaining
   */
  clear(): AdoptionForm {
    this.adopterData = {};
    this.dogData = {};
    return this;
  }

  /**
   * Get all form data as a dictionary
   */
  toDict(): FormData {
    return { ...this.adopterData, ...this.dogData };
  }

  /**
   * Load form data from a dictionary
   * 
   * @param data - Dictionary containing form data
   * @returns Self for method chaining
   */
  fromDict(data: FormData): AdoptionForm {
    this.clear();

    for (const [fieldName, value] of Object.entries(data)) {
      if (fieldName.startsWith('adopter_')) {
        this.adopterData[fieldName as keyof AdopterProfile] = value;
      } else if (fieldName.startsWith('dog_')) {
        this.dogData[fieldName as keyof DogProfile] = value;
      }
    }

    return this;
  }

  /**
   * Get information about a specific field
   * 
   * @param fieldName - Name of the field
   * @returns Field information including allowed values
   */
  async getFieldInfo(fieldName: string): Promise<FieldInfo> {
    const dropdownValues = await this.getDropdownValues();

    const info: FieldInfo = {
      field_name: fieldName,
      is_dropdown: fieldName in dropdownValues,
      allowed_values: dropdownValues[fieldName] || [],
      current_value: this.adopterData[fieldName as keyof AdopterProfile] || 
                     this.dogData[fieldName as keyof DogProfile],
      category: fieldName.startsWith('adopter_') ? 'adopter' : 
                fieldName.startsWith('dog_') ? 'dog' : 'unknown'
    };

    return info;
  }

  /**
   * Get list of all available field names
   */
  async getAllFields(): Promise<string[]> {
    const dropdownValues = await this.getDropdownValues();
    const sampleData = await this.getSampleData();

    // Combine field names from both sources
    const allFields = new Set([
      ...Object.keys(dropdownValues),
      ...Object.keys(sampleData)
    ]);

    return Array.from(allFields).sort();
  }

  /**
   * Get list of adopter field names
   */
  async getAdopterFields(): Promise<string[]> {
    const allFields = await this.getAllFields();
    return allFields.filter(f => f.startsWith('adopter_'));
  }

  /**
   * Get list of dog field names
   */
  async getDogFields(): Promise<string[]> {
    const allFields = await this.getAllFields();
    return allFields.filter(f => f.startsWith('dog_'));
  }
}

/**
 * Utility class for building forms programmatically
 */
export class FormBuilder {
  /**
   * Create a basic adoption form with minimal required fields
   * 
   * @param client - FurSightClient instance
   * @returns AdoptionForm with basic structure
   */
  static createBasicForm(client: FurSightClient): AdoptionForm {
    const form = new AdoptionForm(client);

    // Set some basic defaults
    form.setAdopterData({
      adopter_housing_type: 'Suburban Home',
      adopter_has_kids: 'No',
      adopter_previous_dog_experience: 'Moderate',
      adopter_long_term_commitment: 'Yes'
    });

    form.setDogData({
      dog_age: 'Adult',
      dog_size: 'Medium',
      dog_energyLevel: 'Moderate'
    });

    return form;
  }

  /**
   * Create a form from a predefined template
   * 
   * @param client - FurSightClient instance
   * @param templateName - Name of the template to use
   * @returns AdoptionForm with template data
   */
  static createFromTemplate(client: FurSightClient, templateName: FormTemplate): AdoptionForm {
    const form = new AdoptionForm(client);

    switch (templateName) {
      case 'family_with_kids':
        form.setAdopterData({
          adopter_housing_type: 'Suburban Home',
          adopter_has_kids: 'Yes',
          adopter_num_kids: 2,
          adopter_kids_ages: '8, 12',
          adopter_kids_dog_experience: 'Good',
          adopter_yard_type: 'Fenced',
          adopter_preferred_size: 'Medium',
          adopter_previous_dog_experience: 'Moderate'
        });

        form.setDogData({
          dog_kids: 'Yes',
          dog_size: 'Medium',
          dog_energyLevel: 'Moderate',
          dog_housetrained: 'Yes'
        });
        break;

      case 'apartment_dweller':
        form.setAdopterData({
          adopter_housing_type: 'Apartment',
          adopter_has_kids: 'No',
          adopter_yard_type: 'Shared',
          adopter_preferred_size: 'Small',
          adopter_exercise_routine: 'Walks'
        });

        form.setDogData({
          dog_size: 'Small',
          dog_apartment: 'Yes',
          dog_energyLevel: 'Low',
          dog_vocal: 'Quiet'
        });
        break;

      case 'senior_adopter':
        form.setAdopterData({
          adopter_housing_type: 'Condo',
          adopter_has_kids: 'No',
          adopter_preferred_age: 'Senior',
          adopter_preferred_energy_level: 'Low',
          adopter_exercise_routine: 'Walks'
        });

        form.setDogData({
          dog_age: 'Senior',
          dog_energyLevel: 'Low',
          dog_oKForSeniors: 'Yes',
          dog_gentle: 'Yes'
        });
        break;

      default:
        // Default to basic form
        return FormBuilder.createBasicForm(client);
    }

    return form;
  }
}
