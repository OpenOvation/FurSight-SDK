"""
FurSight SDK Models

Pydantic models for the FurSight Pet Adoption API.
These models are independent copies of the API models for client-side validation.
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict, Any
from datetime import datetime


class AdopterProfile(BaseModel):
    """
    Adopter profile information for pet adoption matching.
    Contains 49 fields related to the potential adopter's situation and preferences.
    """
    
    model_config = ConfigDict(
        title="Adopter Profile",
        description="Complete adopter information for pet matching"
    )
    
    # Housing and Living Situation
    adopter_housing_type: Optional[str] = Field(None, description="Housing type (Suburban Home, Apartment, etc.)")
    adopter_home_ownership_status: Optional[str] = Field(None, description="Home ownership status (Own, Rent)")
    adopter_landlord_permission: Optional[str] = Field(None, description="Landlord permission for pets")
    adopter_yard_type: Optional[str] = Field(None, description="Yard type (Shared, Fenced)")
    adopter_fence_type: Optional[str] = Field(None, description="Fence type (Chain-link, Wood)")
    adopter_fence_height_ft: Optional[float] = Field(None, description="Fence height in feet")
    adopter_household_members: Optional[str] = Field(None, description="Household composition")
    
    # Children and Family
    adopter_has_kids: Optional[str] = Field(None, description="Has children in household")
    adopter_num_kids: Optional[float] = Field(None, description="Number of children")
    adopter_kids_ages: Optional[str] = Field(None, description="Ages of children (comma-separated)")
    adopter_kids_dog_experience: Optional[str] = Field(None, description="Children's experience with dogs")
    
    # Allergies and Health
    adopter_household_allergies: Optional[str] = Field(None, description="Household allergies to pets")
    adopter_allergy_severity: Optional[str] = Field(None, description="Severity of allergies")
    adopter_hypoallergenic_preference: Optional[str] = Field(None, description="Preference for hypoallergenic pets")
    
    # Schedule and Availability
    adopter_hours_dog_left_alone: Optional[float] = Field(None, description="Hours dog would be left alone daily")
    adopter_daytime_presence: Optional[str] = Field(None, description="Who is home during the day")
    adopter_move_plan_within_6mo: Optional[str] = Field(None, description="Plans to move within 6 months")
    
    # Financial Capacity
    adopter_monthly_dog_budget_usd: Optional[float] = Field(None, description="Monthly budget for dog care")
    adopter_can_afford_vet_grooming: Optional[str] = Field(None, description="Can afford veterinary and grooming costs")
    
    # Pet Preferences
    adopter_preferred_breed: Optional[str] = Field(None, description="Preferred dog breed")
    adopter_preferred_breed_status: Optional[str] = Field(None, description="Preference for purebred vs mixed")
    adopter_preferred_age: Optional[str] = Field(None, description="Preferred age (Puppy, Adult, Senior)")
    adopter_preferred_size: Optional[str] = Field(None, description="Preferred size (Small, Medium, Large)")
    adopter_preferred_energy_level: Optional[str] = Field(None, description="Preferred energy level")
    adopter_desired_temperament: Optional[str] = Field(None, description="Desired temperament")
    adopter_preferred_sex: Optional[str] = Field(None, description="Preferred sex")
    adopter_preferred_housetraining_status: Optional[str] = Field(None, description="Housetraining preference")
    adopter_okay_with_medical_needs: Optional[str] = Field(None, description="Willing to handle medical needs")
    adopter_okay_with_behavior_issues: Optional[str] = Field(None, description="Willing to handle behavior issues")
    
    # Motivation and Care Plans
    adopter_reason_for_adoption: Optional[str] = Field(None, description="Reason for wanting to adopt")
    adopter_exercise_routine: Optional[str] = Field(None, description="Planned exercise routine")
    adopter_exercise_frequency_per_week: Optional[float] = Field(None, description="Exercise frequency per week")
    adopter_discipline_method: Optional[str] = Field(None, description="Preferred discipline method")
    adopter_training_plan: Optional[str] = Field(None, description="Training plans")
    adopter_leash_behavior: Optional[str] = Field(None, description="Leash behavior expectations")
    adopter_dog_sleeping_area: Optional[str] = Field(None, description="Where dog will sleep")
    
    # Experience and History
    adopter_previous_dog_experience: Optional[str] = Field(None, description="Previous experience with dogs")
    adopter_pitbull_experience: Optional[str] = Field(None, description="Experience with pit bull type dogs")
    adopter_owned_dogs_last_5yrs: Optional[float] = Field(None, description="Number of dogs owned in last 5 years")
    adopter_previous_pet_outcome: Optional[str] = Field(None, description="What happened to previous pets")
    
    # Current Pets and Integration
    adopter_has_other_pets: Optional[str] = Field(None, description="Currently has other pets")
    adopter_other_pets_info: Optional[str] = Field(None, description="Information about current pets")
    adopter_pets_adjustment_expectation: Optional[str] = Field(None, description="Expectations for pet adjustment")
    adopter_experience_with_issues: Optional[str] = Field(None, description="Experience handling pet issues")
    
    # Commitment and Planning
    adopter_surrender_risks: Optional[str] = Field(None, description="Potential reasons for surrender")
    adopter_long_term_commitment: Optional[str] = Field(None, description="Long-term commitment understanding")
    adopter_pet_loss_plan: Optional[str] = Field(None, description="Plan if pet gets lost")
    adopter_preparation_confidence: Optional[str] = Field(None, description="Confidence in preparation")
    adopter_adopter_breed_restrictions: Optional[str] = Field(None, description="Any breed restrictions")
    
    # Generated Content
    adopter_rewritten_adopter_letter: Optional[str] = Field(None, description="Generated adopter letter")


class DogProfile(BaseModel):
    """
    Dog profile information for pet adoption matching.
    Contains 73 fields related to the dog's characteristics, behavior, and needs.
    """
    
    model_config = ConfigDict(
        title="Dog Profile",
        description="Complete dog information for adoption matching"
    )
    
    # Basic Information
    dog_breed: Optional[str] = Field(None, description="Dog breed")
    dog_primaryBreed: Optional[str] = Field(None, description="Primary breed")
    dog_secondaryBreed: Optional[str] = Field(None, description="Secondary breed")
    dog_sex: Optional[str] = Field(None, description="Dog sex (Male, Female)")
    dog_mixed: Optional[str] = Field(None, description="Is mixed breed")
    dog_age: Optional[str] = Field(None, description="Age category (Baby, Young, Adult, Senior)")
    dog_birthdate: Optional[str] = Field(None, description="Birth date")
    dog_altered: Optional[str] = Field(None, description="Spayed/neutered status")
    
    # Compatibility
    dog_dogs: Optional[str] = Field(None, description="Good with other dogs")
    dog_cats: Optional[str] = Field(None, description="Good with cats")
    dog_kids: Optional[str] = Field(None, description="Good with children")
    dog_oKWithAdults: Optional[str] = Field(None, description="OK with adults")
    dog_oKForSeniors: Optional[str] = Field(None, description="Suitable for seniors")
    dog_oKWithFarmAnimals: Optional[str] = Field(None, description="OK with farm animals")
    
    # Physical Characteristics
    dog_size: Optional[str] = Field(None, description="Size category (Small, Medium, Large, X-Large)")
    dog_sizeCurrent: Optional[float] = Field(None, description="Current weight in pounds")
    dog_sizePotential: Optional[float] = Field(None, description="Potential adult weight")
    dog_sizeUOM: Optional[str] = Field(None, description="Size unit of measure")
    dog_color: Optional[str] = Field(None, description="Coat color")
    dog_coatLength: Optional[str] = Field(None, description="Coat length (Short, Medium, Long)")
    dog_pattern: Optional[str] = Field(None, description="Coat pattern")
    dog_earType: Optional[str] = Field(None, description="Ear type")
    dog_eyeColor: Optional[str] = Field(None, description="Eye color")
    dog_tailType: Optional[str] = Field(None, description="Tail type")
    
    # Training and Behavior
    dog_housetrained: Optional[str] = Field(None, description="House training status")
    dog_obedienceTraining: Optional[str] = Field(None, description="Obedience training level")
    dog_leashtrained: Optional[str] = Field(None, description="Leash training status")
    dog_cratetrained: Optional[str] = Field(None, description="Crate training status")
    dog_ownerExperience: Optional[str] = Field(None, description="Required owner experience level")
    
    # Activity and Exercise
    dog_exerciseNeeds: Optional[str] = Field(None, description="Exercise requirements")
    dog_energyLevel: Optional[str] = Field(None, description="Energy level")
    dog_activityLevel: Optional[str] = Field(None, description="Activity level")
    dog_yardRequired: Optional[str] = Field(None, description="Yard requirement")
    dog_fence: Optional[str] = Field(None, description="Fence requirements")
    
    # Care Requirements
    dog_groomingNeeds: Optional[str] = Field(None, description="Grooming requirements")
    dog_shedding: Optional[str] = Field(None, description="Shedding level")
    dog_hypoallergenic: Optional[str] = Field(None, description="Hypoallergenic status")
    dog_specialNeeds: Optional[str] = Field(None, description="Has special needs")
    dog_uptodate: Optional[str] = Field(None, description="Up to date on vaccinations")
    
    # Health and Medical
    dog_declawed: Optional[str] = Field(None, description="Declawed status")
    dog_hasAllergies: Optional[str] = Field(None, description="Has allergies")
    dog_specialDiet: Optional[str] = Field(None, description="Requires special diet")
    dog_ongoingMedical: Optional[str] = Field(None, description="Has ongoing medical needs")
    dog_hearingImpaired: Optional[str] = Field(None, description="Hearing impaired")
    dog_sightImpaired: Optional[str] = Field(None, description="Sight impaired")
    
    # Personality Traits
    dog_obedient: Optional[str] = Field(None, description="Obedient")
    dog_playful: Optional[str] = Field(None, description="Playful")
    dog_timid: Optional[str] = Field(None, description="Timid")
    dog_skittish: Optional[str] = Field(None, description="Skittish")
    dog_independent: Optional[str] = Field(None, description="Independent")
    dog_affectionate: Optional[str] = Field(None, description="Affectionate")
    dog_eagerToPlease: Optional[str] = Field(None, description="Eager to please")
    dog_intelligent: Optional[str] = Field(None, description="Intelligent")
    dog_eventempered: Optional[str] = Field(None, description="Even tempered")
    dog_gentle: Optional[str] = Field(None, description="Gentle")
    dog_goofy: Optional[str] = Field(None, description="Goofy")
    
    # Behavioral Characteristics
    dog_newPeople: Optional[str] = Field(None, description="Reaction to new people")
    dog_vocal: Optional[str] = Field(None, description="Vocal level")
    dog_goodInCar: Optional[str] = Field(None, description="Good in car")
    dog_fetches: Optional[str] = Field(None, description="Likes to fetch")
    dog_playsToys: Optional[str] = Field(None, description="Plays with toys")
    dog_swims: Optional[str] = Field(None, description="Likes to swim")
    dog_lap: Optional[str] = Field(None, description="Lap dog")
    dog_drools: Optional[str] = Field(None, description="Drools")
    dog_protective: Optional[str] = Field(None, description="Protective")
    dog_escapes: Optional[str] = Field(None, description="Tendency to escape")
    dog_predatory: Optional[str] = Field(None, description="Predatory behavior")
    
    # Environmental Preferences
    dog_apartment: Optional[str] = Field(None, description="Suitable for apartment")
    dog_noHeat: Optional[str] = Field(None, description="Sensitive to heat")
    dog_noCold: Optional[str] = Field(None, description="Sensitive to cold")
    
    # Generated Content
    dog_combined_breeds: Optional[str] = Field(None, description="Combined breed information")
    dog_enriched_profile: Optional[str] = Field(None, description="Generated dog profile")


class PredictionResponse(BaseModel):
    """
    Response from the FurSight prediction API.
    Contains recommendation, probability scores, and enhanced explanations.
    """
    
    model_config = ConfigDict(
        title="Prediction Response",
        description="Complete prediction results from FurSight API"
    )
    
    # Core Prediction Results
    recommendation: str = Field(description="Adoption recommendation (Good Match, Poor Match, etc.)")
    adoption_probability: float = Field(description="Probability score (0.0 to 1.0)")
    confidence_score: float = Field(description="Model confidence in prediction")
    
    # Model Information
    model_version: str = Field(description="Version of the prediction model used")
    timestamp: str = Field(description="Timestamp of prediction")
    
    # Enhanced Explanation System (3-band system)
    simplified_band_info: Optional[Dict[str, Any]] = Field(None, description="3-band system information (green/yellow/red)")
    volunteer_guidance: Optional[Dict[str, Any]] = Field(None, description="Guidance for adoption counselors")
    
    # Transaction Details
    transaction_info: Optional[Dict[str, Any]] = Field(None, description="API transaction information")


class FormValidationError(BaseModel):
    """
    Validation error details for form fields.
    """
    
    field: str = Field(description="Field name that failed validation")
    message: str = Field(description="Error message")
    received_value: Optional[str] = Field(None, description="Value that was received")
    allowed_values: Optional[list] = Field(None, description="List of allowed values")


class HealthStatus(BaseModel):
    """
    API health status response.
    """
    
    status: str = Field(description="Overall health status")
    timestamp: str = Field(description="Health check timestamp")
    model_loaded: bool = Field(description="Whether prediction model is loaded")
    version: Optional[str] = Field(None, description="API version")
    uptime: Optional[str] = Field(None, description="API uptime")


class ModelInfo(BaseModel):
    """
    Information about the loaded prediction model.
    """
    
    model_name: str = Field(description="Name of the loaded model")
    model_version: str = Field(description="Version of the model")
    features_count: int = Field(description="Number of features in the model")
    training_date: Optional[str] = Field(None, description="When the model was trained")
    accuracy_metrics: Optional[Dict[str, Any]] = Field(None, description="Model accuracy metrics")
