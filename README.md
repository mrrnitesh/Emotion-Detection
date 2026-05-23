# Emotion Detection using Watson NLP

A comprehensive Python project for detecting and analyzing emotions in text using IBM Watson NLP library.

## 🎯 Features

- **Single Text Emotion Detection**: Analyze emotions in individual text samples
- **Batch Processing**: Process multiple texts efficiently
- **Emotion Summary**: Get aggregate statistics across multiple texts
- **Detailed Analysis**: Combined sentiment and emotion analysis
- **Confidence Scores**: Get reliability metrics for predictions
- **Multi-Emotion Support**: Detect all five primary emotions:
  - 😢 Sadness
  - 😊 Joy
  - 😨 Fear
  - 🤢 Disgust
  - 😠 Anger

## 📋 Prerequisites

- Python 3.8 or higher
- IBM Watson NLP library
- pip (Python package manager)

## 🚀 Installation

### 1. Clone or Create Project Directory
```bash
mkdir emotion-detection
cd emotion-detection
```

### 2. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify Installation
```bash
python -c "import watson_nlp; print('Watson NLP installed successfully!')"
```

## 📖 Usage Guide

### Basic Usage

```python
from emotion_detector import EmotionDetector

# Initialize the detector
detector = EmotionDetector()

# Detect emotions in a single text
text = "I am so happy about this wonderful news!"
result = detector.detect_emotion(text)

print(f"Dominant Emotion: {result['dominant_emotion']}")
print(f"Confidence: {result['confidence']}")
print(f"All Emotions: {result['emotions']}")
```

### Batch Processing

```python
texts = [
    "This is amazing!",
    "I'm feeling down today",
    "I'm scared of the dark"
]

results = detector.detect_emotions_batch(texts)
for result in results:
    print(f"{result['text']} → {result['dominant_emotion']}")
```

### Get Summary Statistics

```python
summary = detector.get_emotion_summary(texts)
print(f"Overall dominant emotion: {summary['dominant_emotion']}")
print(f"Average emotions: {summary['average_emotions']}")
```

### Detailed Analysis

```python
detailed = detector.analyze_sentiment_emotion(text)
print(f"Primary Emotion: {detailed['primary_emotion']}")
print(f"Confidence Score: {detailed['confidence_score']}")
print(f"Emotion Distribution: {detailed['emotion_distribution']}")
```

## 📊 Output Format

### Single Emotion Detection Result

```json
{
    "text": "I am so happy!",
    "emotions": {
        "sadness": 0.0123,
        "joy": 0.9234,
        "fear": 0.0012,
        "disgust": 0.0234,
        "anger": 0.0145
    },
    "dominant_emotion": "joy",
    "confidence": 0.9234
}
```

### Summary Result

```json
{
    "total_texts_analyzed": 5,
    "average_emotions": {
        "sadness": 0.1234,
        "joy": 0.5678,
        "fear": 0.0123,
        "disgust": 0.0234,
        "anger": 0.0145
    },
    "dominant_emotion": "joy"
}
```

## 🔧 API Reference

### EmotionDetector Class

#### `__init__()`
Initializes the emotion detector and loads the Watson NLP model.

#### `detect_emotion(text: str) -> Dict`
Detects emotions in a single text.

**Parameters:**
- `text` (str): The input text to analyze

**Returns:**
- Dictionary with emotion scores, dominant emotion, and confidence

#### `detect_emotions_batch(texts: List[str]) -> List[Dict]`
Detects emotions for multiple texts.

**Parameters:**
- `texts` (List[str]): List of texts to analyze

**Returns:**
- List of emotion detection results

#### `get_emotion_summary(texts: List[str]) -> Dict`
Gets summary statistics of emotions across multiple texts.

**Parameters:**
- `texts` (List[str]): List of texts to analyze

**Returns:**
- Dictionary with summary statistics

#### `analyze_sentiment_emotion(text: str) -> Dict`
Analyzes both sentiment and emotion for comprehensive understanding.

**Parameters:**
- `text` (str): The input text to analyze

**Returns:**
- Dictionary with combined sentiment and emotion analysis

## 🎓 Examples

### Example 1: Social Media Sentiment Analysis
```python
detector = EmotionDetector()

tweets = [
    "Just got promoted! Over the moon! 🎉",
    "This is the worst day ever 😞",
    "Excited for the concert tonight!",
]

for tweet in tweets:
    result = detector.detect_emotion(tweet)
    print(f"{tweet}")
    print(f"  Emotion: {result['dominant_emotion']} ({result['confidence']})")
```

### Example 2: Customer Feedback Analysis
```python
feedback = [
    "Your service is excellent, very satisfied!",
    "Poor quality, disappointed with purchase",
    "Average product, nothing special",
]

summary = detector.get_emotion_summary(feedback)
print(f"Customer Satisfaction (Joy): {summary['average_emotions']['joy']}")
print(f"Customer Dissatisfaction (Anger): {summary['average_emotions']['anger']}")
```

### Example 3: Mental Health Monitoring
```python
journal_entries = [
    "Had a great day, feeling optimistic",
    "Struggling with anxiety today",
    "Feeling better, hopeful for tomorrow",
]

results = detector.detect_emotions_batch(journal_entries)
for i, result in enumerate(results, 1):
    print(f"Entry {i}: {result['dominant_emotion']}")
```

## 📁 Project Structure

```
emotion-detection/
├── emotion_detector.py      # Main emotion detection module
├── requirements.txt         # Project dependencies
├── README.md               # This file
├── example_usage.py        # Example usage script
└── test_emotion.py         # Unit tests (optional)
```

## 🐛 Troubleshooting

### Issue: Watson NLP model not found
**Solution:** Ensure you have installed watson-nlp correctly:
```bash
pip install --upgrade watson-nlp
```

### Issue: Memory error during model loading
**Solution:** The emotion model requires RAM. Ensure you have at least 4GB free memory.

### Issue: Import error for watson_nlp
**Solution:** Reinstall the package:
```bash
pip uninstall watson-nlp
pip install watson-nlp[watson-runtime]
```

## 📚 Watson Emotions Explained

1. **Joy**: Positive emotion expressing happiness and delight
2. **Sadness**: Negative emotion expressing sorrow or unhappiness
3. **Anger**: Negative emotion expressing irritation or hostility
4. **Fear**: Negative emotion expressing anxiety or worry
5. **Disgust**: Negative emotion expressing aversion or repulsion

## 🔗 Resources

- [Watson NLP Documentation](https://github.com/IBM/watson-nlp)
- [IBM Watson Natural Language Understanding](https://cloud.ibm.com/docs/natural-language-understanding)
- [Emotion Detection Model](https://github.com/IBM/watson-nlp/blob/master/packages/watson_nlp/model_cards/emotion.md)

## 📄 License

This project is provided as-is for educational and development purposes.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest enhancements
- Submit pull requests

## 📞 Support

For issues with Watson NLP, visit:
- [IBM Watson GitHub](https://github.com/IBM/watson-nlp)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/watson-nlp)

---

**Created with ❤️ for emotion detection tasks**
