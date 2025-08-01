/**
 * FurSight API Client
 * 
 * Main client class for interacting with the FurSight Pet Adoption API
 */

import axios, { AxiosInstance, AxiosResponse, AxiosError } from 'axios';
import {
  ClientConfig,
  PredictionResponse,
  HealthStatus,
  ModelInfo,
  DropdownValues,
  SampleData,
  BatchPredictionResponse,
  TextGenerationResponse,
  PredictionBandsResponse,
  AdopterProfile,
  DogProfile,
  FormData,
  RequestOptions
} from './types';
import {
  FurSightError,
  APIError,
  RateLimitError,
  AuthenticationError,
  InsufficientCreditsError,
  TimeoutError,
  NetworkError,
  ValidationError
} from './errors';

/**
 * Main client for the FurSight Pet Adoption API
 */
export class FurSightClient {
  private apiKey: string;
  private baseUrl: string;
  private timeout: number;
  private maxRetries: number;
  private httpClient: AxiosInstance;
  private lastRequestTime: number = 0;
  private minRequestInterval: number = 100; // 100ms between requests

  /**
   * Create a new FurSight client
   * 
   * @param config - Client configuration
   */
  constructor(config: ClientConfig) {
    this.apiKey = config.apiKey;
    this.baseUrl = config.baseUrl || 'https://api.fursight.ai';
    this.timeout = config.timeout || 30000;
    this.maxRetries = config.maxRetries || 3;

    // Create axios instance with default configuration
    this.httpClient = axios.create({
      baseURL: this.baseUrl,
      timeout: this.timeout,
      headers: {
        'Authorization': `Bearer ${this.apiKey}`,
        'Content-Type': 'application/json',
        'User-Agent': 'FurSight-SDK-JavaScript/1.0.0'
      }
    });

    // Add response interceptor for error handling
    this.httpClient.interceptors.response.use(
      (response) => response,
      (error) => this.handleResponseError(error)
    );
  }

  /**
   * Wait for rate limiting
   */
  private async waitForRateLimit(): Promise<void> {
    const elapsed = Date.now() - this.lastRequestTime;
    if (elapsed < this.minRequestInterval) {
      await new Promise(resolve => setTimeout(resolve, this.minRequestInterval - elapsed));
    }
    this.lastRequestTime = Date.now();
  }

  /**
   * Handle HTTP response errors
   */
  private handleResponseError(error: AxiosError): Promise<never> {
    if (error.response) {
      const { status, data } = error.response;
      const message = (data as any)?.detail || `HTTP ${status}`;

      switch (status) {
        case 400:
          throw new ValidationError(message);
        case 401:
          throw new AuthenticationError('Invalid API key');
        case 402:
          throw new InsufficientCreditsError('Insufficient credits');
        case 429:
          const retryAfter = parseInt(error.response.headers['retry-after'] || '60');
          throw new RateLimitError(`Rate limit exceeded. Retry after ${retryAfter} seconds.`, retryAfter);
        default:
          throw new APIError(message, status, data);
      }
    } else if (error.code === 'ECONNABORTED') {
      throw new TimeoutError(`Request timeout after ${this.timeout}ms`);
    } else {
      throw new NetworkError(`Network error: ${error.message}`);
    }
  }

  /**
   * Make HTTP request with retry logic
   */
  private async makeRequest<T>(options: RequestOptions): Promise<T> {
    await this.waitForRateLimit();

    for (let attempt = 0; attempt < this.maxRetries; attempt++) {
      try {
        const response: AxiosResponse<T> = await this.httpClient.request({
          method: options.method,
          url: options.url,
          data: options.data,
          params: options.params,
          headers: options.headers
        });

        return response.data;
      } catch (error) {
        if (error instanceof RateLimitError && attempt < this.maxRetries - 1) {
          // Wait for rate limit and retry
          await new Promise(resolve => setTimeout(resolve, (error.retryAfter || 60) * 1000));
          continue;
        }

        if (error instanceof TimeoutError || error instanceof NetworkError) {
          if (attempt < this.maxRetries - 1) {
            // Exponential backoff for network errors
            await new Promise(resolve => setTimeout(resolve, Math.pow(2, attempt) * 1000));
            continue;
          }
        }

        throw error;
      }
    }

    throw new FurSightError('Max retries exceeded');
  }

  /**
   * Make a single pet adoption prediction
   * 
   * @param adopterData - Adopter information
   * @param dogData - Dog information
   * @param includeExplanation - Whether to include prediction explanation
   * @returns Prediction response
   */
  async predictSingle(
    adopterData: AdopterProfile,
    dogData: DogProfile,
    includeExplanation: boolean = true
  ): Promise<PredictionResponse> {
    const combinedData: FormData = { ...adopterData, ...dogData };

    return this.makeRequest<PredictionResponse>({
      method: 'POST',
      url: '/predict/single',
      data: combinedData,
      params: { include_explanation: includeExplanation }
    });
  }

  // REMOVED: predictBatch method - endpoint is disabled in current API
  // The /predict/batch endpoint has been temporarily disabled

  /**
   * Get sample form data with all 122 fields
   * 
   * @returns Sample data for testing
   */
  async getSampleData(): Promise<SampleData> {
    const response = await this.makeRequest<{ sample_data: SampleData }>({
      method: 'GET',
      url: '/form/sample-data'
    });

    return response.sample_data;
  }

  // REMOVED: getDropdownValues method - endpoint is disabled in current API
  // The /form/dropdown-values endpoint has been temporarily disabled

  // REMOVED: generateAdopterLetter method - endpoint is disabled in current API
  // The /form/generate-adopter-letter endpoint has been temporarily disabled

  // REMOVED: generateDogProfile method - endpoint is disabled in current API
  // The /form/generate-dog-profile endpoint has been temporarily disabled

  /**
   * Check API health status
   * 
   * @returns Health status information
   */
  async getHealth(): Promise<HealthStatus> {
    return this.makeRequest<HealthStatus>({
      method: 'GET',
      url: '/health'
    });
  }

  /**
   * Get information about the loaded model
   * 
   * @returns Model information and metadata
   */
  async getModelInfo(): Promise<ModelInfo> {
    return this.makeRequest<ModelInfo>({
      method: 'GET',
      url: '/model/info'
    });
  }

  /**
   * Get comprehensive information about the 3-band prediction system
   * 
   * @returns Complete reference guide for the 3-band prediction system (Green/Yellow/Red)
   */
  async getPredictionBands(): Promise<PredictionBandsResponse> {
    return this.makeRequest<PredictionBandsResponse>({
      method: 'GET',
      url: '/prediction/bands'
    });
  }
}
