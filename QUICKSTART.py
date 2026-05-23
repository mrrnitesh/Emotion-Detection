"""
QUICK START GUIDE - Emotion Detection with Watson NLP
"""

# =============================================================================
# INSTALLATION (Run these commands in your terminal)
# =============================================================================

"""
1. Create a virtual environment:
   python -m venv venv
   
2. Activate it:
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Verify installation:
   python -c "import watson_nlp; print('Ready!')"
"""


# =============================================================================
# BASIC USAGE (Copy & Paste)
# =============================================================================

# Import the detector
from emotion_detector import EmotionDetector

# Create an instance (loads the model)
detector = EmotionDetector()

# Analyze one sentence
text = "I'm absolutely thrilled about this news!"
result = detector.detect_emotion(text)

print(f"Emotion: {result['dominant_emotion']}")
print(f"Confidence: {result['confidence']:.2%}")


# =============================================================================
# QUICK EXAMPLES
# =============================================================================

# EXAMPLE 1: Simple single-text analysis
# --------
print("\n--- Example 1: Single Text ---")
result = detector.detect_emotion("I'm so happy right now!")
print(f"Dominant: {result['dominant_emotion']}")
for emotion, score in result['emotions'].items():
    print(f"  {emotion}: {score:.4f}")


# EXAMPLE 2: Multiple texts
# --------
print("\n--- Example 2: Batch Analysis ---")
texts = [
    "This is amazing!",
    "I'm really disappointed",
    "Feeling scared about the future"
]

results = detector.detect_emotions_batch(texts)
for r in results:
    print(f"'{r['text']}' → {r['dominant_emotion']}")


# EXAMPLE 3: Get summary of multiple texts
# --------
print("\n--- Example 3: Summary Statistics ---")
summary = detector.get_emotion_summary(texts)
print(f"Average dominant emotion: {summary['dominant_emotion']}")
print(f"Total analyzed: {summary['total_texts_analyzed']}")
print("Emotion averages:")
for emotion, score in summary['average_emotions'].items():
    print(f"  {emotion}: {score:.4f}")


# EXAMPLE 4: Detailed analysis
# --------
print("\n--- Example 4: Detailed Analysis ---")
detailed = detector.analyze_sentiment_emotion("I feel wonderful!")
print(f"Primary emotion: {detailed['primary_emotion']}")
print(f"Confidence: {detailed['confidence_score']:.2%}")
print("Distribution:")
for e, s in detailed['emotion_distribution'].items():
    print(f"  {e}: {s:.4f}")


# =============================================================================
# COMMON PATTERNS
# =============================================================================

# Pattern 1: Find the most positive text in a list
# --------
texts_to_analyze = [
    "This is terrible",
    "This is wonderful",
    "This is okay"
]
results = detector.detect_emotions_batch(texts_to_analyze)
most_positive = max(results, key=lambda x: x['emotions']['joy'])
print(f"\nMost positive: {most_positive['text']}")


# Pattern 2: Filter texts by emotion
# --------
results = detector.detect_emotions_batch(texts_to_analyze)
angry_texts = [r['text'] for r in results if r['dominant_emotion'] == 'anger']
happy_texts = [r['text'] for r in results if r['dominant_emotion'] == 'joy']


# Pattern 3: Get emotion confidence scores
# --------
result = detector.detect_emotion("I'm feeling mixed emotions")
if result['confidence'] > 0.7:
    print("Strong emotion detected")
elif result['confidence'] > 0.5:
    print("Moderate emotion detected")
else:
    print("Weak or mixed emotions")


# =============================================================================
# AVAILABLE EMOTIONS
# =============================================================================

"""
The detector recognizes 5 primary emotions:

1. JOY 😊
   - Happiness, delight, pleasure, satisfaction
   - Examples: "I love it!", "Wonderful!", "Fantastic!"

2. SADNESS 😢
   - Sorrow, unhappiness, disappointment
   - Examples: "I'm so sad", "Disappointing", "I miss you"

3. ANGER 😠
   - Irritation, frustration, hostility
   - Examples: "I'm furious!", "Terrible!", "Hate it"

4. FEAR 😨
   - Anxiety, worry, nervousness, dread
   - Examples: "I'm scared", "Nervous", "Worried"

5. DISGUST 🤢
   - Aversion, repulsion, contempt
   - Examples: "Disgusting!", "Yuck", "Repulsive"
"""


# =============================================================================
# RETURN VALUE FORMAT
# =============================================================================

"""
detect_emotion() returns a dictionary:
{
    'text': 'original input text',
    'emotions': {
        'sadness': 0.0123,
        'joy': 0.8456,
        'fear': 0.0234,
        'disgust': 0.0145,
        'anger': 0.1042
    },
    'dominant_emotion': 'joy',
    'confidence': 0.8456,
    'raw_response': {...}  # Raw model output
}

Key insights:
- 'emotions': Scores for each emotion (0 to 1)
- 'dominant_emotion': The emotion with the highest score
- 'confidence': How confident the model is (equals highest emotion score)
"""


# =============================================================================
# TIPS & TRICKS
# =============================================================================

"""
1. LONGER TEXTS ARE MORE ACCURATE
   - Single words: Less reliable
   - Full sentences: Good
   - Paragraphs: Best

2. CONTEXT MATTERS
   - "I'm not happy" might not register as sadness
   - "I love this!" is clearly joy
   - Sarcasm may confuse the model

3. HANDLING MIXED EMOTIONS
   - Look at the emotion scores, not just dominant emotion
   - Check multiple values, not just the top one

4. BATCH PROCESSING
   - Faster than processing one by one
   - Better for large datasets
   - Use summary() for aggregate analysis

5. CONFIDENCE INTERPRETATION
   - 0.9+: Very high confidence
   - 0.7-0.9: High confidence
   - 0.5-0.7: Moderate confidence
   - <0.5: Low confidence, possibly mixed emotions
"""


# =============================================================================
# TROUBLESHOOTING
# =============================================================================

"""
Problem: "ModuleNotFoundError: No module named 'watson_nlp'"
Solution: pip install watson-nlp watson-nlp[watson-runtime]

Problem: "Memory Error"
Solution: Ensure you have at least 4GB free RAM

Problem: Model loads but returns empty results
Solution: Ensure input text is not empty and is a string

Problem: Different results for same text
Solution: This is normal - models have some variance. Use the confidence score.
"""


# =============================================================================
# NEXT STEPS
# =============================================================================

"""
1. Run the example script:
   python example_usage.py

2. Run the tests:
   python test_emotion.py

3. Check the README for detailed documentation:
   cat README.md

4. Read the emotion_detector.py file for full API reference

5. Try modifying the examples for your use case
"""


# =============================================================================
# USEFUL ONE-LINERS
# =============================================================================

# Quick emotion check
detector = EmotionDetector()
print(detector.detect_emotion("I'm happy")['dominant_emotion'])

# Check emotion confidence
result = detector.detect_emotion("text")
high_confidence = result['confidence'] > 0.7

# Get all emotion scores sorted
emotions_sorted = sorted(result['emotions'].items(), key=lambda x: x[1], reverse=True)

# Find texts with specific emotion
texts = ["sad text", "happy text", "angry text"]
results = detector.detect_emotions_batch(texts)
happy_ones = [r for r in results if r['dominant_emotion'] == 'joy']

# Export to JSON
import json
json.dumps(result, indent=2)


print("\n✓ Quick Start Guide Complete!")
print("You're ready to detect emotions. Run example_usage.py to see more!")
