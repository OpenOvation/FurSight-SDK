/**
 * FurSight SDK Errors
 * 
 * Custom error classes for the FurSight JavaScript SDK
 */

/**
 * Base error class for all FurSight SDK errors
 */
export class FurSightError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'FurSightError';
    Object.setPrototypeOf(this, FurSightError.prototype);
  }
}

/**
 * Error thrown when input data validation fails
 */
export class ValidationError extends FurSightError {
  constructor(message: string) {
    super(message);
    this.name = 'ValidationError';
    Object.setPrototypeOf(this, ValidationError.prototype);
  }
}

/**
 * Error thrown when API requests fail
 */
export class APIError extends FurSightError {
  public statusCode?: number;
  public response?: any;

  constructor(message: string, statusCode?: number, response?: any) {
    super(message);
    this.name = 'APIError';
    this.statusCode = statusCode;
    this.response = response;
    Object.setPrototypeOf(this, APIError.prototype);
  }
}

/**
 * Error thrown when API rate limit is exceeded
 */
export class RateLimitError extends APIError {
  public retryAfter?: number;

  constructor(message: string, retryAfter?: number) {
    super(message, 429);
    this.name = 'RateLimitError';
    this.retryAfter = retryAfter;
    Object.setPrototypeOf(this, RateLimitError.prototype);
  }
}

/**
 * Error thrown when API authentication fails
 */
export class AuthenticationError extends APIError {
  constructor(message: string = 'Invalid API key') {
    super(message, 401);
    this.name = 'AuthenticationError';
    Object.setPrototypeOf(this, AuthenticationError.prototype);
  }
}

/**
 * Error thrown when account has insufficient credits
 */
export class InsufficientCreditsError extends APIError {
  constructor(message: string = 'Insufficient credits') {
    super(message, 402);
    this.name = 'InsufficientCreditsError';
    Object.setPrototypeOf(this, InsufficientCreditsError.prototype);
  }
}

/**
 * Error thrown when network requests timeout
 */
export class TimeoutError extends FurSightError {
  constructor(message: string = 'Request timeout') {
    super(message);
    this.name = 'TimeoutError';
    Object.setPrototypeOf(this, TimeoutError.prototype);
  }
}

/**
 * Error thrown when network requests fail
 */
export class NetworkError extends FurSightError {
  constructor(message: string) {
    super(message);
    this.name = 'NetworkError';
    Object.setPrototypeOf(this, NetworkError.prototype);
  }
}
