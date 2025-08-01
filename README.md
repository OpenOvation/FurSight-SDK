# 🐕 BAILEY™ SDK

**AI-Powered Pet Adoption Intelligence Platform**

Official Software Development Kit for the BAILEY™ Pet Adoption API

## 🚀 Quick Start

### Python
```bash
pip install git+https://github.com/OpenOvation/FurSight-SDK.git#subdirectory=python
```

```python
from fursight import FurSightClient

client = FurSightClient(api_key="your_api_key")
result = client.predict_single(adopter_data, dog_data)
print(f"Recommendation: {result['recommendation']}")
```

### JavaScript/Node.js
```bash
npm install git+https://github.com/OpenOvation/FurSight-SDK.git#subdirectory=javascript
```

```javascript
import { FurSightClient } from '@fursight/sdk';

const client = new FurSightClient('your_api_key');
const result = await client.predictSingle(adopterData, dogData);
console.log(`Recommendation: ${result.recommendation}`);
```

## 🔑 Getting API Keys

### For Individual Developers & Testing
- **Test API Key**: `test_key_individual_developer_2024` *(Email admin@fursight.ai to request your own API key)*
- **Rate Limit**: 10 requests per day
- **Perfect for**: Learning, testing, building integrations

### For Organizations (Shelters/Rescues)
1. **Email admin@fursight.ai** from your official shelter/rescue email
2. **Include your organization's website** for verification
3. **Describe your use case** and integration plans
4. **Allow 1-2 business days** for approval

## 📚 Documentation

- **[API Usage Guide](./docs/API_USAGE_GUIDE.md)** - Complete API reference and examples
- **[Examples](./examples/)** - Code samples for Python and JavaScript

## 📋 Requirements

- **Python**: 3.8+ (for Python SDK)
- **Node.js**: 14+ (for JavaScript SDK)
- **API Key**: Required for all API calls

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 📞 Support

- **GitHub Issues**: [Report bugs and request features](https://github.com/OpenOvation/FurSight-SDK/issues)
- **API Support**: admin@fursight.ai

---

**🐕 Helping pets find their perfect families through better technology.**
