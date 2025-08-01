# 🐕 BAILEY™ Python SDK

**AI-Powered Pet Adoption Intelligence Platform**

Official Python SDK for the BAILEY™ Pet Adoption API

## 🚀 Quick Start

### Installation

```bash
pip install git+https://github.com/OpenOvation/FurSight-SDK.git#subdirectory=python
```

### Basic Usage

```python
from fursight import FurSightClient

# Initialize the client
client = FurSightClient(api_key="your_api_key_here")

# Get sample data with all required fields
sample_data = client.get_sample_data()

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
result = client.predict_single(sample_data)

print(f"Recommendation: {result.recommendation}")
print(f"Adoption Probability: {result.adoption_probability:.2%}")
print(f"Confidence Score: {result.confidence_score:.2%}")
```

## 📚 Core Features

- **Simple API**: Easy-to-use client for making predictions
- **Type Safety**: Full type hints and Pydantic models
- **Error Handling**: Comprehensive error handling
- **Helper Methods**: Get sample data and dropdown values

## 🔧 API Methods

### Client Methods

```python
# Health check
health = client.health_check()

# Get sample data (all 122 fields)
sample_data = client.get_sample_data()

# Get dropdown values for form fields
dropdown_values = client.get_dropdown_values()

# Make prediction
result = client.predict_single(prediction_data)
```

### Error Handling

```python
from fursight.exceptions import (
    FurSightAPIError,
    AuthenticationError,
    ValidationError,
    RateLimitError
)

try:
    result = client.predict_single(prediction_data)
except AuthenticationError:
    print("Invalid API key")
except ValidationError as e:
    print(f"Invalid input data: {e}")
except RateLimitError:
    print("Rate limit exceeded")
except FurSightAPIError as e:
    print(f"API error: {e}")
```

## 🧪 Testing

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run with coverage
pytest --cov=fursight
```

## 📄 License

MIT License - see [LICENSE](../LICENSE) for details.

## 📞 Support

- **GitHub Issues**: [Report bugs and request features](https://github.com/OpenOvation/FurSight-SDK/issues)
- **Email Support**: admin@fursight.ai

---

**🐕 Helping pets find their perfect families through better technology.**
