/**
 * FurSight SDK - JavaScript Example
 * 
 * Simple example demonstrating how to use the FurSight JavaScript SDK
 * to make pet adoption predictions.
 */

async function main() {
  // Get API key from environment or use test key
  const apiKey = process.env.FURSIGHT_API_KEY || 'test_key_individual_developer_2024';
  const baseUrl = 'https://bailey.fursight.ai';
  
  const headers = {
    'Authorization': `Bearer ${apiKey}`,
    'Content-Type': 'application/json'
  };

  console.log('🐕 FurSight SDK JavaScript Example');
  console.log('=' .repeat(40));

  try {
    // 1. Check API Health
    console.log('\n1. Checking API Health...');
    const healthResponse = await fetch(`${baseUrl}/health`);
    const health = await healthResponse.json();
    console.log(`   Status: ${health.status}`);
    console.log(`   Model Loaded: ${health.model_loaded}`);

    // 2. Get Sample Data
    console.log('\n2. Getting Sample Data...');
    const sampleResponse = await fetch(`${baseUrl}/form/sample-data`, { headers });
    const sampleData = (await sampleResponse.json()).sample_data;
    console.log(`   Sample data loaded with ${Object.keys(sampleData).length} fields`);

    // 3. Customize Data and Make Prediction
    console.log('\n3. Making Prediction...');
    
    // Customize some fields
    const customData = {
      ...sampleData,
      adopter_age: 28,
      adopter_has_kids: "No",
      adopter_housing_type: "Apartment",
      dog_breed: "Golden Retriever",
      dog_age: 2,
      dog_size: "Medium"
    };

    // Make prediction
    const response = await fetch(`${baseUrl}/predict/single`, {
      method: 'POST',
      headers,
      body: JSON.stringify(customData)
    });

    if (response.ok) {
      const result = await response.json();
      console.log(`   Recommendation: ${result.recommendation}`);
      console.log(`   Probability: ${result.adoption_probability.toFixed(3)}`);
      console.log(`   Confidence: ${result.confidence_score.toFixed(3)}`);
      
      if (result.band_info) {
        console.log(`   Band: ${result.band_info.band_name}`);
      }
    } else {
      const errorText = await response.text();
      console.log(`   Error: ${response.status} - ${errorText}`);
    }

    console.log('\n✅ Example completed successfully!');

  } catch (error) {
    console.error(`❌ Error: ${error.message}`);
  }
}

// Run the example
main().catch(console.error);
