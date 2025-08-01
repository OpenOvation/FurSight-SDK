/**
 * FurSight SDK - JavaScript/TypeScript Client
 * 
 * Official JavaScript SDK for the FurSight Pet Adoption API
 */

export { FurSightClient } from './client';
export { AdoptionForm, FormBuilder } from './forms';
export * from './types';
export {
  FurSightError,
  ValidationError,
  APIError,
  RateLimitError,
  AuthenticationError,
  InsufficientCreditsError,
  TimeoutError,
  NetworkError
} from './errors';

// Default export for convenience
export { FurSightClient as default } from './client';
