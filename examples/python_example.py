#!/usr/bin/env python3
"""
FurSight SDK - Python Example

Simple example demonstrating how to use the FurSight Python SDK
to make pet adoption predictions.
"""

import os
import requests

def main():
    """Basic example using the FurSight API"""
    
    # Get API key from environment or use test key
    # Email admin@fursight.ai to request your own API key
    api_key = os.getenv('FURSIGHT_API_KEY', 'test_key_individual_developer_2024')
    base_url = "https://bailey.fursight.ai"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    print("🐕 FurSight SDK Python Example")
    print("=" * 40)
    
    try:
        # 1. Check API Health
        print("\n1. Checking API Health...")
        response = requests.get(f"{base_url}/health")
        health = response.json()
        print(f"   Status: {health['status']}")
        print(f"   Model Loaded: {health['model_loaded']}")
        
        # 2. Get Sample Data
        print("\n2. Getting Sample Data...")
        response = requests.get(f"{base_url}/form/sample-data", headers=headers)
        sample_data = response.json()["sample_data"]
        print(f"   Sample data loaded with {len(sample_data)} fields")
        
        # 3. Customize Data and Make Prediction
        print("\n3. Making Prediction...")
        
        # Customize some fields
        sample_data.update({
            "adopter_age": 28,
            "adopter_has_kids": "No",
            "adopter_housing_type": "Apartment",
            "dog_breed": "Golden Retriever",
            "dog_age": 2,
            "dog_size": "Medium"
        })
        
        # Make prediction
        response = requests.post(
            f"{base_url}/predict/single",
            headers=headers,
            json=sample_data
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"   Recommendation: {result['recommendation']}")
            print(f"   Probability: {result['adoption_probability']:.3f}")
            print(f"   Confidence: {result['confidence_score']:.3f}")
            
            if 'band_info' in result:
                print(f"   Band: {result['band_info']['band_name']}")
        else:
            print(f"   Error: {response.status_code} - {response.text}")
        
        print("\n✅ Example completed successfully!")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Request Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")


if __name__ == '__main__':
    main()
