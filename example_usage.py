"""
Example Usage Script for Emotion Detection
Demonstrates various use cases and scenarios
"""

from emotion_detector import EmotionDetector
import json


def example_1_single_sentence():
    """Example 1: Analyze a single sentence"""
    print("\n" + "="*70)
    print("EXAMPLE 1: Single Sentence Analysis")
    print("="*70)
    
    detector = EmotionDetector()
    
    sentences = [
        "I absolutely love this product, it's amazing!",
        "I'm disappointed with the quality",
        "I feel nervous about the upcoming exam",
    ]
    
    for sentence in sentences:
        result = detector.detect_emotion(sentence)
        print(f"\nText: {sentence}")
        print(f"Dominant Emotion: {result['dominant_emotion'].upper()}")
        print(f"Confidence: {result['confidence']:.2%}")
        print(f"Emotion Scores:")
        for emotion, score in result['emotions'].items():
            bar = "█" * int(score * 20)
            print(f"  {emotion:10} [{bar:<20}] {score:.4f}")


def example_2_social_media_analysis():
    """Example 2: Analyze social media posts"""
    print("\n" + "="*70)
    print("EXAMPLE 2: Social Media Posts Analysis")
    print("="*70)
    
    detector = EmotionDetector()
    
    posts = {
        "user_123": "Just finished my project! Feeling so accomplished 🎉",
        "user_456": "Can't believe they cancelled the event... so disappointed 😞",
        "user_789": "Weather is perfect, everyone's happy today!",
        "user_012": "This new policy is terrible, really angry about it 😤",
        "user_345": "Really nervous about the interview tomorrow...",
    }
    
    results = {}
    for user, post in posts.items():
        result = detector.detect_emotion(post)
        results[user] = {
            'post': post,
            'emotion': result['dominant_emotion'],
            'confidence': result['confidence']
        }
        print(f"\n{user}: {post}")
        print(f"└─ Emotion: {result['dominant_emotion']} (Confidence: {result['confidence']:.2%})")


def example_3_customer_feedback():
    """Example 3: Analyze customer feedback"""
    print("\n" + "="*70)
    print("EXAMPLE 3: Customer Feedback Analysis")
    print("="*70)
    
    detector = EmotionDetector()
    
    feedback = [
        "Excellent service, very professional staff. Highly recommend!",
        "The product broke after one week. Very poor quality.",
        "Good value for money, satisfied with my purchase.",
        "Customer service was rude and unhelpful. Terrible experience.",
        "Product is okay, nothing special but does the job.",
        "Exceeded my expectations! Best purchase ever!",
    ]
    
    print("\nAnalyzing customer feedback...\n")
    
    # Analyze each feedback
    results = detector.detect_emotions_batch(feedback)
    
    # Display individual results
    for i, result in enumerate(results, 1):
        print(f"Feedback {i}: {result['text'][:50]}...")
        print(f"  → Emotion: {result['dominant_emotion']} ({result['confidence']:.2%})")
    
    # Get summary
    summary = detector.get_emotion_summary(feedback)
    print(f"\n" + "-"*70)
    print("Summary Statistics:")
    print(f"Total feedback analyzed: {summary['total_texts_analyzed']}")
    print(f"Overall dominant emotion: {summary['dominant_emotion']}")
    print(f"\nAverage emotion distribution:")
    for emotion, score in summary['average_emotions'].items():
        print(f"  {emotion:10}: {score:.2%}")


def example_4_sentiment_tracking():
    """Example 4: Track sentiment over time (simulated)"""
    print("\n" + "="*70)
    print("EXAMPLE 4: Sentiment Tracking Over Time")
    print("="*70)
    
    detector = EmotionDetector()
    
    # Simulated diary entries over a week
    diary = {
        "Monday": "Started the week feeling positive and motivated!",
        "Tuesday": "Had a difficult meeting, feeling stressed.",
        "Wednesday": "Worked through my issues, feeling better now.",
        "Thursday": "Great progress on my goals, very satisfied!",
        "Friday": "Looking forward to the weekend, feeling excited!",
    }
    
    print("\nTracking emotional journey through the week:\n")
    
    for day, entry in diary.items():
        result = detector.detect_emotion(entry)
        emotion = result['dominant_emotion']
        confidence = result['confidence']
        
        # Create a visual representation
        emoji_map = {
            'joy': '😊',
            'sadness': '😢',
            'fear': '😨',
            'anger': '😠',
            'disgust': '🤢'
        }
        
        emoji = emoji_map.get(emotion, '😐')
        print(f"{day:10} {emoji} {emotion.upper():10} {confidence:.0%} - {entry}")


def example_5_text_classification():
    """Example 5: Classify texts by emotion for categorization"""
    print("\n" + "="*70)
    print("EXAMPLE 5: Text Classification by Emotion")
    print("="*70)
    
    detector = EmotionDetector()
    
    texts = [
        "This is the best day of my life!",
        "I can't stand this anymore, absolutely furious!",
        "What if something goes wrong? I'm so worried.",
        "This is disgusting and unacceptable!",
        "I miss you so much, feeling so sad.",
        "I'm thrilled about the wonderful news!",
    ]
    
    # Classify texts by emotion
    classified = {
        'joy': [],
        'sadness': [],
        'anger': [],
        'fear': [],
        'disgust': []
    }
    
    for text in texts:
        result = detector.detect_emotion(text)
        dominant = result['dominant_emotion']
        classified[dominant].append(text)
    
    print("\nTexts classified by dominant emotion:\n")
    for emotion, texts_list in classified.items():
        if texts_list:
            emoji_map = {
                'joy': '😊', 'sadness': '😢', 'fear': '😨',
                'anger': '😠', 'disgust': '🤢'
            }
            print(f"\n{emoji_map[emotion]} {emotion.upper()}:")
            for text in texts_list:
                print(f"  • {text}")


def example_6_export_results():
    """Example 6: Export results to JSON format"""
    print("\n" + "="*70)
    print("EXAMPLE 6: Export Results to JSON")
    print("="*70)
    
    detector = EmotionDetector()
    
    texts = [
        "I'm delighted with the results!",
        "Deeply disappointed by this outcome.",
        "Feeling uncertain about the future.",
    ]
    
    results = []
    for text in texts:
        result = detector.detect_emotion(text)
        results.append({
            'text': result['text'],
            'dominant_emotion': result['dominant_emotion'],
            'confidence': result['confidence'],
            'emotion_scores': result['emotions']
        })
    
    # Display JSON output
    json_output = json.dumps(results, indent=2)
    print("\nJSON Output:")
    print(json_output)
    
    # Optional: Save to file
    # with open('emotion_results.json', 'w') as f:
    #     json.dump(results, f, indent=2)
    # print("\n✓ Results saved to emotion_results.json")


def example_7_comparative_analysis():
    """Example 7: Compare emotions between groups of texts"""
    print("\n" + "="*70)
    print("EXAMPLE 7: Comparative Analysis")
    print("="*70)
    
    detector = EmotionDetector()
    
    # Two groups of texts to compare
    positive_texts = [
        "I love this so much!",
        "Fantastic news, I'm thrilled!",
        "Best day ever!",
    ]
    
    negative_texts = [
        "This is terrible!",
        "I hate this situation.",
        "Absolutely awful experience.",
    ]
    
    print("\nPositive Texts:")
    positive_summary = detector.get_emotion_summary(positive_texts)
    print(f"Dominant Emotion: {positive_summary['dominant_emotion']}")
    print(f"Joy Score: {positive_summary['average_emotions']['joy']:.4f}")
    print(f"Anger Score: {positive_summary['average_emotions']['anger']:.4f}")
    
    print("\nNegative Texts:")
    negative_summary = detector.get_emotion_summary(negative_texts)
    print(f"Dominant Emotion: {negative_summary['dominant_emotion']}")
    print(f"Joy Score: {negative_summary['average_emotions']['joy']:.4f}")
    print(f"Anger Score: {negative_summary['average_emotions']['anger']:.4f}")
    
    print("\nComparison:")
    joy_diff = positive_summary['average_emotions']['joy'] - negative_summary['average_emotions']['joy']
    print(f"Joy difference (positive - negative): {joy_diff:+.4f}")


def main():
    """Run all examples"""
    print("\n" + "="*70)
    print("EMOTION DETECTION EXAMPLES")
    print("="*70)
    
    try:
        example_1_single_sentence()
        example_2_social_media_analysis()
        example_3_customer_feedback()
        example_4_sentiment_tracking()
        example_5_text_classification()
        example_6_export_results()
        example_7_comparative_analysis()
        
        print("\n" + "="*70)
        print("✓ All examples completed successfully!")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\n✗ Error running examples: {e}")
        raise


if __name__ == "__main__":
    main()
