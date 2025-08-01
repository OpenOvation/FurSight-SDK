"""
FurSight SDK Exceptions

Custom exception classes for the FurSight SDK.
"""


class FurSightError(Exception):
    """Base exception for all FurSight SDK errors."""
    pass


class ValidationError(FurSightError):
    """Raised when input data validation fails."""
    pass


class APIError(FurSightError):
    """Raised when API requests fail."""
    
    def __init__(self, message: str, status_code: int = None):
        super().__init__(message)
        self.status_code = status_code


class RateLimitError(APIError):
    """Raised when API rate limit is exceeded."""
    
    def __init__(self, message: str, retry_after: int = None):
        super().__init__(message, status_code=429)
        self.retry_after = retry_after


class AuthenticationError(APIError):
    """Raised when API authentication fails."""
    
    def __init__(self, message: str = "Invalid API key"):
        super().__init__(message, status_code=401)


class InsufficientCreditsError(APIError):
    """Raised when account has insufficient credits."""
    
    def __init__(self, message: str = "Insufficient credits"):
        super().__init__(message, status_code=402)
