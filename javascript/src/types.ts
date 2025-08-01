/**
 * FurSight SDK Types
 * 
 * TypeScript type definitions for the FurSight Pet Adoption API
 */

// Band Information
export interface BandInfo {
  band_number: number;
  band_name: string;
  risk_level: string;
  action_guidance: string;
}

// Core API Response Types
export interface PredictionResponse {
  recommendation: string;
  adoption_probability: number;
  confidence_score: number;
  band_info: BandInfo;
  explanation: string;
  model_version: string;
  timestamp: string;
}

// Adopter Profile (49 fields)
export interface AdopterProfile {
  // Housing and Living Situation
  adopter_housing_type?: string;
  adopter_home_ownership_status?: string;
  adopter_landlord_permission?: string;
  adopter_yard_type?: string;
  adopter_fence_type?: string;
  adopter_fence_height_ft?: number;
  adopter_household_members?: string;
  
  // Children and Family
  adopter_has_kids?: string;
  adopter_num_kids?: number;
  adopter_kids_ages?: string;
  adopter_kids_dog_experience?: string;
  
  // Allergies and Health
  adopter_household_allergies?: string;
  adopter_allergy_severity?: string;
  adopter_hypoallergenic_preference?: string;
  
  // Schedule and Availability
  adopter_hours_dog_left_alone?: number;
  adopter_daytime_presence?: string;
  adopter_move_plan_within_6mo?: string;
  
  // Financial Capacity
  adopter_monthly_dog_budget_usd?: number;
  adopter_can_afford_vet_grooming?: string;
  
  // Pet Preferences
  adopter_preferred_breed?: string;
  adopter_preferred_breed_status?: string;
  adopter_preferred_age?: string;
  adopter_preferred_size?: string;
  adopter_preferred_energy_level?: string;
  adopter_desired_temperament?: string;
  adopter_preferred_sex?: string;
  adopter_preferred_housetraining_status?: string;
  adopter_okay_with_medical_needs?: string;
  adopter_okay_with_behavior_issues?: string;
  
  // Motivation and Care Plans
  adopter_reason_for_adoption?: string;
  adopter_exercise_routine?: string;
  adopter_exercise_frequency_per_week?: number;
  adopter_discipline_method?: string;
  adopter_training_plan?: string;
  adopter_leash_behavior?: string;
  adopter_dog_sleeping_area?: string;
  
  // Experience and History
  adopter_previous_dog_experience?: string;
  adopter_pitbull_experience?: string;
  adopter_owned_dogs_last_5yrs?: number;
  adopter_previous_pet_outcome?: string;
  
  // Current Pets and Integration
  adopter_has_other_pets?: string;
  adopter_other_pets_info?: string;
  adopter_pets_adjustment_expectation?: string;
  adopter_experience_with_issues?: string;
  
  // Commitment and Planning
  adopter_surrender_risks?: string;
  adopter_long_term_commitment?: string;
  adopter_pet_loss_plan?: string;
  adopter_preparation_confidence?: string;
  adopter_adopter_breed_restrictions?: string;
  
  // Generated Content
  adopter_rewritten_adopter_letter?: string;
}

// Dog Profile (73 fields)
export interface DogProfile {
  // Basic Information
  dog_breed?: string;
  dog_primaryBreed?: string;
  dog_secondaryBreed?: string;
  dog_sex?: string;
  dog_mixed?: string;
  dog_age?: string;
  dog_birthdate?: string;
  dog_altered?: string;
  
  // Compatibility
  dog_dogs?: string;
  dog_cats?: string;
  dog_kids?: string;
  dog_oKWithAdults?: string;
  dog_oKForSeniors?: string;
  dog_oKWithFarmAnimals?: string;
  
  // Physical Characteristics
  dog_size?: string;
  dog_sizeCurrent?: number;
  dog_sizePotential?: number;
  dog_sizeUOM?: string;
  dog_color?: string;
  dog_coatLength?: string;
  dog_pattern?: string;
  dog_earType?: string;
  dog_eyeColor?: string;
  dog_tailType?: string;
  
  // Training and Behavior
  dog_housetrained?: string;
  dog_obedienceTraining?: string;
  dog_leashtrained?: string;
  dog_cratetrained?: string;
  dog_ownerExperience?: string;
  
  // Activity and Exercise
  dog_exerciseNeeds?: string;
  dog_energyLevel?: string;
  dog_activityLevel?: string;
  dog_yardRequired?: string;
  dog_fence?: string;
  
  // Care Requirements
  dog_groomingNeeds?: string;
  dog_shedding?: string;
  dog_hypoallergenic?: string;
  dog_specialNeeds?: string;
  dog_uptodate?: string;
  
  // Health and Medical
  dog_declawed?: string;
  dog_hasAllergies?: string;
  dog_specialDiet?: string;
  dog_ongoingMedical?: string;
  dog_hearingImpaired?: string;
  dog_sightImpaired?: string;
  
  // Personality Traits
  dog_obedient?: string;
  dog_playful?: string;
  dog_timid?: string;
  dog_skittish?: string;
  dog_independent?: string;
  dog_affectionate?: string;
  dog_eagerToPlease?: string;
  dog_intelligent?: string;
  dog_eventempered?: string;
  dog_gentle?: string;
  dog_goofy?: string;
  
  // Behavioral Characteristics
  dog_newPeople?: string;
  dog_vocal?: string;
  dog_goodInCar?: string;
  dog_fetches?: string;
  dog_playsToys?: string;
  dog_swims?: string;
  dog_lap?: string;
  dog_drools?: string;
  dog_protective?: string;
  dog_escapes?: string;
  dog_predatory?: string;
  
  // Environmental Preferences
  dog_apartment?: string;
  dog_noHeat?: string;
  dog_noCold?: string;
  
  // Generated Content
  dog_combined_breeds?: string;
  dog_enriched_profile?: string;
}

// Combined form data
export interface FormData extends AdopterProfile, DogProfile {}

// API Response Types
export interface HealthStatus {
  status: string;
  timestamp: string;
  model_loaded: boolean;
  version?: string;
  uptime?: string;
}

export interface ModelInfo {
  model_name: string;
  model_version: string;
  features_count: number;
  training_date?: string;
  accuracy_metrics?: Record<string, any>;
}

export interface DropdownValues {
  [fieldName: string]: string[];
}

export interface SampleData extends FormData {}

export interface BatchPredictionRequest {
  data: FormData[];
}

export interface BatchPredictionResponse {
  predictions: PredictionResponse[];
}

export interface TextGenerationResponse {
  generated_text: string;
}

export interface PredictionBandsResponse {
  bands: Record<string, any>;
  description: string;
}

// Client Configuration
export interface ClientConfig {
  apiKey: string;
  baseUrl?: string;
  timeout?: number;
  maxRetries?: number;
}

// Form Validation
export interface FieldInfo {
  field_name: string;
  is_dropdown: boolean;
  allowed_values: string[];
  current_value?: any;
  category: 'adopter' | 'dog' | 'unknown';
}

export interface ValidationError {
  field: string;
  message: string;
  received_value?: string;
  allowed_values?: string[];
}

// Template Types
export type FormTemplate = 'family_with_kids' | 'apartment_dweller' | 'senior_adopter';

// HTTP Method Types
export type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';

// Request Options
export interface RequestOptions {
  method: HttpMethod;
  url: string;
  data?: any;
  params?: Record<string, any>;
  headers?: Record<string, string>;
}
