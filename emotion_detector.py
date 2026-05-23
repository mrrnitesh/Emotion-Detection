"""
Emotion Detection Module using Watson NLP
This module provides functionality to detect emotions from text using IBM Watson NLP
"""

import watson_nlp
from typing import Dict, List, Optional
import json


class EmotionDetector:
    """
    A class to detect emotions in text using Watson NLP library
    """
    
    def __init__(self):
        """Initialize the emotion detector with Watson NLP models"""
        try:
            # Load the emotion detection model
            self.emotion_model = watson_nlp.load(
                model_id='emotion_aggregated-workflow_lang_en_stock',
                cache_directory=None
            )
            print("✓ Watson NLP Emotion Detection model loaded successfully")
        except Exception as e:
            print(f"Error loading emotion model: {e}")
            raise
    
    def detect_emotion(self, text: str) -> Dict:
        """
        Detect emotions in the given text
        
        Args:
            text (str): The input text to analyze
            
        Returns:
            dict: A dictionary containing emotion scores and the dominant emotion
        """
        if not text or not isinstance(text, str):
            raise ValueError("Input text must be a non-empty string")
        
        try:
            # Run emotion detection
            result = self.emotion_model.run(text)
            
            # Extract emotion predictions
            emotions = result.get('emotion', {})
            
            # Process and format the results
            emotion_scores = {
                'sadness': emotions.get('sadness', 0),
                'joy': emotions.get('joy', 0),
                'fear': emotions.get('fear', 0),
                'disgust': emotions.get('disgust', 0),
                'anger': emotions.get('anger', 0)
            }
            
            # Find the dominant emotion
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            dominant_score = emotion_scores[dominant_emotion]
            
            return {
                'text': text,
                'emotions': emotion_scores,
                'dominant_emotion': dominant_emotion,
                'confidence': round(dominant_score, 4),
                'raw_response': result
            }
        
        except Exception as e:
            print(f"Error during emotion detection: {e}")
            raise
    
    def detect_emotions_batch(self, texts: List[str]) -> List[Dict]:
        """
        Detect emotions for multiple texts
        
        Args:
            texts (List[str]): List of texts to analyze
            
        Returns:
            List[Dict]: List of emotion detection results
        """
        results = []
        for text in texts:
            try:
                result = self.detect_emotion(text)
                results.append(result)
            except Exception as e:
                results.append({
                    'text': text,
                    'error': str(e)
                })
        
        return results
    
    def get_emotion_summary(self, texts: List[str]) -> Dict:
        """
        Get a summary of emotions across multiple texts
        
        Args:
            texts (List[str]): List of texts to analyze
            
        Returns:
            dict: Summary statistics of emotions
        """
        emotions_detected = {
            'sadness': 0,
            'joy': 0,
            'fear': 0,
            'disgust': 0,
            'anger': 0
        }
        
        results = self.detect_emotions_batch(texts)
        
        for result in results:
            if 'emotions' in result:
                for emotion, score in result['emotions'].items():
                    emotions_detected[emotion] += score
        
        # Calculate averages
        num_texts = len(texts)
        for emotion in emotions_detected:
            emotions_detected[emotion] = round(emotions_detected[emotion] / num_texts, 4)
        
        return {
            'total_texts_analyzed': num_texts,
            'average_emotions': emotions_detected,
            'dominant_emotion': max(emotions_detected, key=emotions_detected.get)
        }
    
    def analyze_sentiment_emotion(self, text: str) -> Dict:
        """
        Analyze both sentiment and emotion for comprehensive understanding
        
        Args:
            text (str): The input text to analyze
            
        Returns:
            dict: Combined sentiment and emotion analysis
        """
        emotion_result = self.detect_emotion(text)
        
        return {
            'text': text,
            'emotion_analysis': emotion_result,
            'emotion_distribution': emotion_result['emotions'],
            'primary_emotion': emotion_result['dominant_emotion'],
            'confidence_score': emotion_result['confidence']
        }


def main():
    """Example usage of the EmotionDetector class"""
    
    # Initialize the detector
    detector = EmotionDetector()
    
    # Example 1: Single text emotion detection
    print("\n" + "="*60)
    print("SINGLE TEXT EMOTION DETECTION")
    print("="*60)
    
    text1 = "I am so happy and excited about this amazing news!"
    result1 = detector.detect_emotion(text1)
    print(f"\nText: {result1['text']}")
    print(f"Emotions: {result1['emotions']}")
    print(f"Dominant Emotion: {result1['dominant_emotion']}")
    print(f"Confidence: {result1['confidence']}")
    
    # Example 2: Multiple texts
    print("\n" + "="*60)
    print("MULTIPLE TEXTS EMOTION DETECTION")
    print("="*60)
    
    texts = [
        "This is terrible, I hate waiting!",
        "What a wonderful day, I feel blessed!",
        "I'm scared and nervous about the presentation",
        "This is absolutely disgusting and unacceptable",
    ]
    
    batch_results = detector.detect_emotions_batch(texts)
    for i, result in enumerate(batch_results, 1):
        print(f"\n[{i}] {result['text']}")
        print(f"    → {result['dominant_emotion'].upper()} (confidence: {result['confidence']})")
    
    # Example 3: Summary statistics
    print("\n" + "="*60)
    print("EMOTION SUMMARY STATISTICS")
    print("="*60)
    
    summary = detector.get_emotion_summary(texts)
    print(f"\nTotal texts analyzed: {summary['total_texts_analyzed']}")
    print(f"Average emotions across all texts:")
    for emotion, score in summary['average_emotions'].items():
        print(f"  • {emotion}: {score}")
    print(f"\nOverall dominant emotion: {summary['dominant_emotion']}")
    
    # Example 4: Detailed analysis
    print("\n" + "="*60)
    print("DETAILED SENTIMENT-EMOTION ANALYSIS")
    print("="*60)
    
    text4 = "I'm feeling anxious about the uncertain future"
    detailed = detector.analyze_sentiment_emotion(text4)
    print(f"\nText: {detailed['text']}")
    print(f"Primary Emotion: {detailed['primary_emotion']}")
    print(f"Confidence Score: {detailed['confidence_score']}")
    print("Emotion Distribution:")
    for emotion, score in detailed['emotion_distribution'].items():
        print(f"  • {emotion}: {score:.4f}")


if __name__ == "__main__":
    main()
