# 🐕 BAILEY™ API Usage Guide

**AI-Powered Pet Adoption Intelligence Platform**

## 🚀 Quick Start

### 1. Get Your API Key

**For Individual Developers/Testing:**
- **Test API Key**: `test_key_individual_developer_2024`
- **Rate Limit**: 10 requests per day
- Perfect for learning and building integrations

**For Organizations (Shelters/Rescues):**
- Email `admin@fursight.ai` from your official organization email
- Include your website and use case description
- Receive API key within 1-2 business days

### 2. Base URL
```
https://bailey.fursight.ai
```

### 3. Authentication
All requests require an API key in the Authorization header:
```bash
Authorization: Bearer YOUR_API_KEY
```

## 📋 Core Endpoints

### Health Check
```bash
GET /health
```
Check if the API is running (no auth required).

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-07-27T15:30:00Z",
  "model_loaded": true
}
```

### Single Prediction
```bash
POST /predict/single
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

**Request Body:** (122 fields total - see complete example below)
```json
{
  "adopter_age": 32,
  "adopter_has_kids": "Yes",
  "adopter_housing_type": "House",
  "adopter_experience_level": "Experienced",
  "dog_age": 3,
  "dog_breed": "Labrador Mix",
  "dog_size": "Medium",
  "dog_energy_level": "High",
  "adopter_rewritten_adopter_letter": "I'm looking for an active companion...",
  "dog_enriched_profile": "This friendly lab mix loves to play..."
}
```

**Response:**
```json
{
  "recommendation": "Recommend: Good Match",
  "adoption_probability": 0.78,
  "confidence_score": 0.65,
  "band_info": {
    "band_number": 2,
    "band_name": "Recommend: Good Match",
    "risk_level": "Low"
  },
  "model_version": "2.0.0",
  "timestamp": "2024-07-27T15:30:00Z"
}
```

## 🛠️ Helper Endpoints

### Get Sample Data
```bash
GET /form/sample-data
Authorization: Bearer YOUR_API_KEY
```

Returns complete sample data with all 122 fields filled out - perfect for testing!

### Get Form Field Options
```bash
GET /form/dropdown-values
Authorization: Bearer YOUR_API_KEY
```

Returns all available dropdown values for each field.

## 💻 Code Examples

### Python
```python
import requests

# Configuration
API_KEY = "your_api_key_here"
BASE_URL = "https://bailey.fursight.ai"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Get sample data first
response = requests.get(f"{BASE_URL}/form/sample-data", headers=headers)
sample_data = response.json()["sample_data"]

# Customize the data
sample_data.update({
    "adopter_age": 28,
    "adopter_has_kids": "No",
    "dog_breed": "Golden Retriever",
    "dog_age": 2
})

# Make prediction
response = requests.post(
    f"{BASE_URL}/predict/single",
    headers=headers,
    json=sample_data
)

result = response.json()
print(f"Recommendation: {result['recommendation']}")
print(f"Probability: {result['adoption_probability']:.2f}")
```

### JavaScript
```javascript
const API_KEY = 'your_api_key_here';
const BASE_URL = 'https://bailey.fursight.ai';

const headers = {
    'Authorization': `Bearer ${API_KEY}`,
    'Content-Type': 'application/json'
};

// Get sample data
const sampleResponse = await fetch(`${BASE_URL}/form/sample-data`, { headers });
const sampleData = (await sampleResponse.json()).sample_data;

// Customize data
const customData = {
    ...sampleData,
    adopter_age: 28,
    adopter_has_kids: "No",
    dog_breed: "Golden Retriever",
    dog_age: 2
};

// Make prediction
const response = await fetch(`${BASE_URL}/predict/single`, {
    method: 'POST',
    headers,
    body: JSON.stringify(customData)
});

const result = await response.json();
console.log(`Recommendation: ${result.recommendation}`);
console.log(`Probability: ${result.adoption_probability.toFixed(2)}`);
```

### cURL
```bash
# Get sample data
curl -X GET \
  "https://bailey.fursight.ai/form/sample-data" \
  -H "Authorization: Bearer your_api_key_here"

# Make prediction (use sample data from above, modify as needed)
curl -X POST \
  "https://bailey.fursight.ai/predict/single" \
  -H "Authorization: Bearer your_api_key_here" \
  -H "Content-Type: application/json" \
  -d '{
    "adopter_age": 28,
    "adopter_has_kids": "No",
    "adopter_housing_type": "Apartment",
    "dog_breed": "Golden Retriever",
    "dog_age": 2,
    "dog_size": "Medium",
    "adopter_rewritten_adopter_letter": "Looking for a calm companion...",
    "dog_enriched_profile": "Friendly golden retriever..."
  }'
```

## 🎯 Understanding Results

### 3-Band Recommendation System

| Band | Name | Action |
|------|------|--------|
| 🟢 Green | Good Match | Schedule meet-and-greet |
| 🟡 Yellow | Could Be a Match - Requires Review | Schedule counselor consultation |
| 🔴 Red | Poor Match | Consider alternative pets |

### Adoption Probability
- **0.0 - 0.3**: Poor match, high risk of return
- **0.3 - 0.5**: Uncertain match, needs review
- **0.5 - 0.7**: Good match, likely success
- **0.7 - 1.0**: Excellent match, very likely success

## ⚠️ Important Notes

### Rate Limits
- **Test API Key**: 10 requests per day
- **Organization Keys**: 1000 requests per day

### Required Fields
The API requires all 122 fields. Use the `/form/sample-data` endpoint to get a complete template, then modify the fields you need.

### Error Handling
```json
{
  "detail": "Error message here",
  "error_code": "INVALID_INPUT",
  "timestamp": "2024-07-27T15:30:00Z"
}
```

Common errors:
- `401`: Invalid API key
- `422`: Missing or invalid fields
- `429`: Rate limit exceeded
- `500`: Server error

## 📞 Support

- **Email**: admin@fursight.ai
- **GitHub**: [FurSight-SDK](https://github.com/OpenOvation/FurSight-SDK)

---

**🐕 Helping pets find their perfect families through better technology.**
