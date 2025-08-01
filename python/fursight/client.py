"""
FurSight API Client

Main client class for interacting with the FurSight Pet Adoption API.
"""

import requests
import time
from typing import Dict, List, Optional, Any, Union
from urllib.parse import urljoin
import logging

from .models import AdopterProfile, DogProfile, PredictionResponse
from .exceptions import FurSightError, ValidationError, APIError, RateLimitError

logger = logging.getLogger(__name__)


class FurSightClient:
    """
    Main client for the FurSight Pet Adoption API.
    
    Args:
        api_key: Your FurSight API key
        base_url: API base URL (default: https://api.fursight.ai)
        timeout: Request timeout in seconds (default: 30)
        max_retries: Maximum number of retries for failed requests (default: 3)
    """
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.fursight.ai",
        timeout: int = 30,
        max_retries: int = 3
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.max_retries = max_retries
        
        # Setup session with default headers
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
            'User-Agent': 'FurSight-SDK-Python/1.0.0'
        })
        
        # Rate limiting
        self.last_request_time = 0
        self.min_request_interval = 0.1  # 100ms between requests
    
    def _wait_for_rate_limit(self):
        """Ensure we don't exceed rate limits"""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.min_request_interval:
            time.sleep(self.min_request_interval - elapsed)
        self.last_request_time = time.time()
    
    def _make_request(
        self, 
        method: str, 
        endpoint: str, 
        **kwargs
    ) -> requests.Response:
        """
        Make HTTP request with retry logic and error handling.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            **kwargs: Additional arguments for requests
            
        Returns:
            Response object
            
        Raises:
            APIError: For API-related errors
            RateLimitError: When rate limit is exceeded
            FurSightError: For other errors
        """
        self._wait_for_rate_limit()
        
        url = urljoin(self.base_url, endpoint)
        
        for attempt in range(self.max_retries):
            try:
                response = self.session.request(
                    method, 
                    url, 
                    timeout=self.timeout,
                    **kwargs
                )
                
                # Handle rate limiting
                if response.status_code == 429:
                    retry_after = int(response.headers.get('Retry-After', 60))
                    logger.warning(f"Rate limited, waiting {retry_after} seconds")
                    
                    if attempt == self.max_retries - 1:
                        raise RateLimitError(
                            f"Rate limit exceeded. Retry after {retry_after} seconds."
                        )
                    
                    time.sleep(retry_after)
                    continue
                
                # Handle other HTTP errors
                if not response.ok:
                    try:
                        error_data = response.json()
                        error_message = error_data.get('detail', f'HTTP {response.status_code}')
                    except:
                        error_message = f'HTTP {response.status_code}: {response.text}'
                    
                    if response.status_code == 400:
                        raise ValidationError(error_message)
                    elif response.status_code == 401:
                        raise APIError("Invalid API key")
                    elif response.status_code == 402:
                        raise APIError("Insufficient credits")
                    else:
                        raise APIError(error_message)
                
                return response
                
            except requests.exceptions.Timeout:
                if attempt == self.max_retries - 1:
                    raise FurSightError(f"Request timeout after {self.timeout} seconds")
                logger.warning(f"Request timeout on attempt {attempt + 1}")
                time.sleep(2 ** attempt)  # Exponential backoff
                
            except requests.exceptions.RequestException as e:
                if attempt == self.max_retries - 1:
                    raise FurSightError(f"Request failed: {str(e)}")
                logger.warning(f"Request failed on attempt {attempt + 1}: {str(e)}")
                time.sleep(2 ** attempt)  # Exponential backoff
        
        raise FurSightError("Max retries exceeded")
    
    def predict_single(
        self,
        adopter_data: Union[Dict[str, Any], AdopterProfile],
        dog_data: Union[Dict[str, Any], DogProfile],
        include_explanation: bool = True
    ) -> PredictionResponse:
        """
        Make a single pet adoption prediction.
        
        Args:
            adopter_data: Adopter information (dict or AdopterProfile)
            dog_data: Dog information (dict or DogProfile)
            include_explanation: Whether to include prediction explanation
            
        Returns:
            PredictionResponse with recommendation and details
            
        Raises:
            ValidationError: If input data is invalid
            APIError: If API request fails
        """
        # Convert models to dicts if needed
        if isinstance(adopter_data, AdopterProfile):
            adopter_data = adopter_data.model_dump()
        if isinstance(dog_data, DogProfile):
            dog_data = dog_data.model_dump()
        
        # Combine data
        prediction_data = {**adopter_data, **dog_data}
        
        # Make request
        response = self._make_request(
            'POST',
            '/predict/single',
            json=prediction_data,
            params={'include_explanation': include_explanation}
        )
        
        result = response.json()
        return PredictionResponse(**result)
    
    # REMOVED: predict_batch method - endpoint is disabled in current API
    # The /predict/batch endpoint has been temporarily disabled
    
    def get_sample_data(self) -> Dict[str, Any]:
        """
        Get sample form data with all 122 fields.
        
        Returns:
            Dictionary with sample data for testing
            
        Raises:
            APIError: If API request fails
        """
        response = self._make_request('GET', '/form/sample-data')
        result = response.json()
        return result['sample_data']
    
    # REMOVED: get_dropdown_values method - endpoint is disabled in current API
    # The /form/dropdown-values endpoint has been temporarily disabled
    
    # REMOVED: generate_adopter_letter method - endpoint is disabled in current API
    # The /form/generate-adopter-letter endpoint has been temporarily disabled
    
    # REMOVED: generate_dog_profile method - endpoint is disabled in current API
    # The /form/generate-dog-profile endpoint has been temporarily disabled
    
    def get_health(self) -> Dict[str, Any]:
        """
        Check API health status.
        
        Returns:
            Health status information
            
        Raises:
            APIError: If API request fails
        """
        response = self._make_request('GET', '/health')
        return response.json()
    
    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the loaded model.
        
        Returns:
            Model information and metadata
            
        Raises:
            APIError: If API request fails
        """
        response = self._make_request('GET', '/model/info')
        return response.json()
    
    def get_prediction_bands(self) -> Dict[str, Any]:
        """
        Get comprehensive information about the 3-band prediction system.
        
        Returns:
            Complete reference guide for the 3-band prediction system (Green/Yellow/Red)
            
        Raises:
            APIError: If API request fails
        """
        response = self._make_request('GET', '/prediction/bands')
        return response.json()
