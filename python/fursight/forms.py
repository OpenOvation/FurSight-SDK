"""
FurSight SDK Forms

Form building and validation utilities for the FurSight Pet Adoption API.
"""

from typing import Dict, List, Any, Optional, Union
from .client import FurSightClient
from .models import AdopterProfile, DogProfile, PredictionResponse
from .exceptions import ValidationError


class AdoptionForm:
    """
    High-level form builder for pet adoption predictions.
    Handles form creation, validation, and submission.
    """
    
    def __init__(self, client: FurSightClient):
        """
        Initialize the adoption form.
        
        Args:
            client: FurSightClient instance for API communication
        """
        self.client = client
        self._adopter_data = {}
        self._dog_data = {}
        self._dropdown_values = None
        self._sample_data = None
    
    def get_dropdown_values(self) -> Dict[str, List[str]]:
        """
        Get all available dropdown values for form fields.
        
        Returns:
            Dictionary mapping field names to allowed values
        """
        if self._dropdown_values is None:
            self._dropdown_values = self.client.get_dropdown_values()
        return self._dropdown_values
    
    def get_sample_data(self) -> Dict[str, Any]:
        """
        Get sample form data for testing.
        
        Returns:
            Dictionary with sample data for all 122 fields
        """
        if self._sample_data is None:
            self._sample_data = self.client.get_sample_data()
        return self._sample_data
    
    def set_adopter_field(self, field_name: str, value: Any) -> 'AdoptionForm':
        """
        Set an adopter field value.
        
        Args:
            field_name: Name of the adopter field
            value: Field value
            
        Returns:
            Self for method chaining
        """
        self._adopter_data[field_name] = value
        return self
    
    def set_dog_field(self, field_name: str, value: Any) -> 'AdoptionForm':
        """
        Set a dog field value.
        
        Args:
            field_name: Name of the dog field
            value: Field value
            
        Returns:
            Self for method chaining
        """
        self._dog_data[field_name] = value
        return self
    
    def set_adopter_data(self, data: Dict[str, Any]) -> 'AdoptionForm':
        """
        Set multiple adopter fields at once.
        
        Args:
            data: Dictionary of adopter field values
            
        Returns:
            Self for method chaining
        """
        self._adopter_data.update(data)
        return self
    
    def set_dog_data(self, data: Dict[str, Any]) -> 'AdoptionForm':
        """
        Set multiple dog fields at once.
        
        Args:
            data: Dictionary of dog field values
            
        Returns:
            Self for method chaining
        """
        self._dog_data.update(data)
        return self
    
    def load_sample_data(self) -> 'AdoptionForm':
        """
        Load sample data into the form for testing.
        
        Returns:
            Self for method chaining
        """
        sample = self.get_sample_data()
        
        # Split sample data into adopter and dog fields
        for field_name, value in sample.items():
            if field_name.startswith('adopter_'):
                self._adopter_data[field_name] = value
            elif field_name.startswith('dog_'):
                self._dog_data[field_name] = value
        
        return self
    
    def validate_field(self, field_name: str, value: Any) -> bool:
        """
        Validate a single field value against dropdown constraints.
        
        Args:
            field_name: Name of the field to validate
            value: Value to validate
            
        Returns:
            True if valid, False otherwise
            
        Raises:
            ValidationError: If validation fails with details
        """
        dropdown_values = self.get_dropdown_values()
        
        if field_name in dropdown_values:
            allowed_values = dropdown_values[field_name]
            if allowed_values and str(value) not in allowed_values:
                raise ValidationError(
                    f"Field '{field_name}' must be one of: {allowed_values[:5]}{'...' if len(allowed_values) > 5 else ''}. "
                    f"Received: '{value}'"
                )
        
        return True
    
    def validate(self) -> bool:
        """
        Validate all form data.
        
        Returns:
            True if all data is valid
            
        Raises:
            ValidationError: If validation fails
        """
        # Validate adopter fields
        for field_name, value in self._adopter_data.items():
            if value is not None:
                self.validate_field(field_name, value)
        
        # Validate dog fields
        for field_name, value in self._dog_data.items():
            if value is not None:
                self.validate_field(field_name, value)
        
        # Check for required fields
        if not self._adopter_data and not self._dog_data:
            raise ValidationError("Form must contain at least some adopter and dog data")
        
        return True
    
    def get_adopter_profile(self) -> AdopterProfile:
        """
        Get validated adopter profile.
        
        Returns:
            AdopterProfile instance
            
        Raises:
            ValidationError: If adopter data is invalid
        """
        return AdopterProfile(**self._adopter_data)
    
    def get_dog_profile(self) -> DogProfile:
        """
        Get validated dog profile.
        
        Returns:
            DogProfile instance
            
        Raises:
            ValidationError: If dog data is invalid
        """
        return DogProfile(**self._dog_data)
    
    def submit(self, include_explanation: bool = True) -> PredictionResponse:
        """
        Submit the form and get prediction results.
        
        Args:
            include_explanation: Whether to include detailed explanation
            
        Returns:
            PredictionResponse with recommendation and details
            
        Raises:
            ValidationError: If form data is invalid
            APIError: If API request fails
        """
        # Validate before submission
        self.validate()
        
        # Submit to API
        return self.client.predict_single(
            adopter_data=self._adopter_data,
            dog_data=self._dog_data,
            include_explanation=include_explanation
        )
    
    def generate_adopter_letter(self) -> str:
        """
        Generate adopter letter from current form data.
        
        Returns:
            Generated adopter letter text
            
        Raises:
            APIError: If API request fails
        """
        combined_data = {**self._adopter_data, **self._dog_data}
        return self.client.generate_adopter_letter(combined_data)
    
    def generate_dog_profile(self) -> str:
        """
        Generate dog profile from current form data.
        
        Returns:
            Generated dog profile text
            
        Raises:
            APIError: If API request fails
        """
        combined_data = {**self._adopter_data, **self._dog_data}
        return self.client.generate_dog_profile(combined_data)
    
    def clear(self) -> 'AdoptionForm':
        """
        Clear all form data.
        
        Returns:
            Self for method chaining
        """
        self._adopter_data.clear()
        self._dog_data.clear()
        return self
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Get all form data as a dictionary.
        
        Returns:
            Dictionary containing all form data
        """
        return {**self._adopter_data, **self._dog_data}
    
    def from_dict(self, data: Dict[str, Any]) -> 'AdoptionForm':
        """
        Load form data from a dictionary.
        
        Args:
            data: Dictionary containing form data
            
        Returns:
            Self for method chaining
        """
        self.clear()
        
        for field_name, value in data.items():
            if field_name.startswith('adopter_'):
                self._adopter_data[field_name] = value
            elif field_name.startswith('dog_'):
                self._dog_data[field_name] = value
        
        return self
    
    def get_field_info(self, field_name: str) -> Dict[str, Any]:
        """
        Get information about a specific field.
        
        Args:
            field_name: Name of the field
            
        Returns:
            Dictionary with field information including allowed values
        """
        dropdown_values = self.get_dropdown_values()
        
        info = {
            'field_name': field_name,
            'is_dropdown': field_name in dropdown_values,
            'allowed_values': dropdown_values.get(field_name, []),
            'current_value': self._adopter_data.get(field_name) or self._dog_data.get(field_name)
        }
        
        # Add field type information
        if field_name.startswith('adopter_'):
            info['category'] = 'adopter'
        elif field_name.startswith('dog_'):
            info['category'] = 'dog'
        else:
            info['category'] = 'unknown'
        
        return info
    
    def get_all_fields(self) -> List[str]:
        """
        Get list of all available field names.
        
        Returns:
            List of field names
        """
        dropdown_values = self.get_dropdown_values()
        sample_data = self.get_sample_data()
        
        # Combine field names from both sources
        all_fields = set(dropdown_values.keys()) | set(sample_data.keys())
        return sorted(list(all_fields))
    
    def get_adopter_fields(self) -> List[str]:
        """
        Get list of adopter field names.
        
        Returns:
            List of adopter field names
        """
        all_fields = self.get_all_fields()
        return [f for f in all_fields if f.startswith('adopter_')]
    
    def get_dog_fields(self) -> List[str]:
        """
        Get list of dog field names.
        
        Returns:
            List of dog field names
        """
        all_fields = self.get_all_fields()
        return [f for f in all_fields if f.startswith('dog_')]


class FormBuilder:
    """
    Utility class for building forms programmatically.
    """
    
    @staticmethod
    def create_basic_form(client: FurSightClient) -> AdoptionForm:
        """
        Create a basic adoption form with minimal required fields.
        
        Args:
            client: FurSightClient instance
            
        Returns:
            AdoptionForm with basic structure
        """
        form = AdoptionForm(client)
        
        # Set some basic defaults
        form.set_adopter_data({
            'adopter_housing_type': 'Suburban Home',
            'adopter_has_kids': 'No',
            'adopter_previous_dog_experience': 'Moderate',
            'adopter_long_term_commitment': 'Yes'
        })
        
        form.set_dog_data({
            'dog_age': 'Adult',
            'dog_size': 'Medium',
            'dog_energyLevel': 'Moderate'
        })
        
        return form
    
    @staticmethod
    def create_from_template(client: FurSightClient, template_name: str) -> AdoptionForm:
        """
        Create a form from a predefined template.
        
        Args:
            client: FurSightClient instance
            template_name: Name of the template to use
            
        Returns:
            AdoptionForm with template data
        """
        form = AdoptionForm(client)
        
        if template_name == 'family_with_kids':
            form.set_adopter_data({
                'adopter_housing_type': 'Suburban Home',
                'adopter_has_kids': 'Yes',
                'adopter_num_kids': 2,
                'adopter_kids_ages': '8, 12',
                'adopter_kids_dog_experience': 'Good',
                'adopter_yard_type': 'Fenced',
                'adopter_preferred_size': 'Medium',
                'adopter_previous_dog_experience': 'Moderate'
            })
            
            form.set_dog_data({
                'dog_kids': 'Yes',
                'dog_size': 'Medium',
                'dog_energyLevel': 'Moderate',
                'dog_housetrained': 'Yes'
            })
        
        elif template_name == 'apartment_dweller':
            form.set_adopter_data({
                'adopter_housing_type': 'Apartment',
                'adopter_has_kids': 'No',
                'adopter_yard_type': 'Shared',
                'adopter_preferred_size': 'Small',
                'adopter_exercise_routine': 'Walks'
            })
            
            form.set_dog_data({
                'dog_size': 'Small',
                'dog_apartment': 'Yes',
                'dog_energyLevel': 'Low',
                'dog_vocal': 'Quiet'
            })
        
        elif template_name == 'senior_adopter':
            form.set_adopter_data({
                'adopter_housing_type': 'Condo',
                'adopter_has_kids': 'No',
                'adopter_preferred_age': 'Senior',
                'adopter_preferred_energy_level': 'Low',
                'adopter_exercise_routine': 'Walks'
            })
            
            form.set_dog_data({
                'dog_age': 'Senior',
                'dog_energyLevel': 'Low',
                'dog_oKForSeniors': 'Yes',
                'dog_gentle': 'Yes'
            })
        
        else:
            # Default to sample data
            form.load_sample_data()
        
        return form
