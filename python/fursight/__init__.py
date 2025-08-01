"""
FurSight SDK - Python Client Library

Official Python SDK for the FurSight Pet Adoption API.
"""

from .client import FurSightClient
from .models import AdopterProfile, DogProfile, PredictionResponse
from .forms import AdoptionForm
from .exceptions import FurSightError, ValidationError, APIError, RateLimitError

__version__ = "1.0.0"
__author__ = "FurSight.ai"
__email__ = "admin@fursight.ai"

__all__ = [
    "FurSightClient",
    "AdopterProfile", 
    "DogProfile",
    "PredictionResponse",
    "AdoptionForm",
    "FurSightError",
    "ValidationError", 
    "APIError",
    "RateLimitError",
]
