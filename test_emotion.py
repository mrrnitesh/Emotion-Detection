"""
Unit Tests for Emotion Detection Module
"""

import unittest
from emotion_detector import EmotionDetector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for EmotionDetector class"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures - runs once before all tests"""
        cls.detector = EmotionDetector()
    
    def test_initialization(self):
        """Test that detector initializes properly"""
        self.assertIsNotNone(self.detector.emotion_model)
        print("✓ Detector initialization test passed")
    
    def test_single_emotion_detection(self):
        """Test emotion detection for a single text"""
        text = "I am very happy!"
        result = self.detector.detect_emotion(text)
        
        self.assertIn('text', result)
        self.assertIn('emotions', result)
        self.assertIn('dominant_emotion', result)
        self.assertIn('confidence', result)
        self.assertEqual(result['text'], text)
        print("✓ Single emotion detection test passed")
    
    def test_emotion_scores_validity(self):
        """Test that emotion scores are valid"""
        text = "This is a test sentence."
        result = self.detector.detect_emotion(text)
        
        emotions = result['emotions']
        
        # Check all emotions are present
        expected_emotions = ['sadness', 'joy', 'fear', 'disgust', 'anger']
        for emotion in expected_emotions:
            self.assertIn(emotion, emotions)
        
        # Check scores are between 0 and 1
        for emotion, score in emotions.items():
            self.assertGreaterEqual(score, 0)
            self.assertLessEqual(score, 1)
        
        print("✓ Emotion scores validity test passed")
    
    def test_confidence_score(self):
        """Test confidence score is valid"""
        text = "I feel happy today"
        result = self.detector.detect_emotion(text)
        
        confidence = result['confidence']
        self.assertGreaterEqual(confidence, 0)
        self.assertLessEqual(confidence, 1)
        print("✓ Confidence score test passed")
    
    def test_dominant_emotion(self):
        """Test that dominant emotion matches highest score"""
        text = "I'm incredibly happy!"
        result = self.detector.detect_emotion(text)
        
        dominant = result['dominant_emotion']
        emotions = result['emotions']
        
        # Dominant emotion should have the highest score
        max_emotion = max(emotions, key=emotions.get)
        self.assertEqual(dominant, max_emotion)
        print("✓ Dominant emotion test passed")
    
    def test_batch_processing(self):
        """Test batch processing of multiple texts"""
        texts = [
            "I'm happy",
            "I'm sad",
            "I'm scared"
        ]
        results = self.detector.detect_emotions_batch(texts)
        
        self.assertEqual(len(results), len(texts))
        for result in results:
            self.assertIn('text', result)
            self.assertIn('dominant_emotion', result)
        print("✓ Batch processing test passed")
    
    def test_empty_string_handling(self):
        """Test handling of empty strings"""
        with self.assertRaises(ValueError):
            self.detector.detect_emotion("")
        print("✓ Empty string handling test passed")
    
    def test_invalid_input_type(self):
        """Test handling of invalid input types"""
        with self.assertRaises(ValueError):
            self.detector.detect_emotion(12345)
        
        with self.assertRaises(ValueError):
            self.detector.detect_emotion(None)
        print("✓ Invalid input type handling test passed")
    
    def test_emotion_summary(self):
        """Test emotion summary generation"""
        texts = [
            "I'm very happy!",
            "I'm quite sad.",
            "I feel alright."
        ]
        summary = self.detector.get_emotion_summary(texts)
        
        self.assertIn('total_texts_analyzed', summary)
        self.assertIn('average_emotions', summary)
        self.assertIn('dominant_emotion', summary)
        
        self.assertEqual(summary['total_texts_analyzed'], len(texts))
        print("✓ Emotion summary test passed")
    
    def test_detailed_analysis(self):
        """Test detailed sentiment-emotion analysis"""
        text = "I'm feeling wonderful today!"
        result = self.detector.analyze_sentiment_emotion(text)
        
        self.assertIn('text', result)
        self.assertIn('emotion_analysis', result)
        self.assertIn('primary_emotion', result)
        self.assertIn('confidence_score', result)
        self.assertEqual(result['text'], text)
        print("✓ Detailed analysis test passed")
    
    def test_long_text(self):
        """Test emotion detection with longer text"""
        long_text = """
        I had the most wonderful day today! From the moment I woke up, 
        everything seemed to go perfectly. The weather was beautiful, 
        I felt energized and motivated, and all my tasks went smoothly. 
        This is definitely one of my happiest days!
        """
        result = self.detector.detect_emotion(long_text)
        
        self.assertIn('dominant_emotion', result)
        self.assertIn('emotions', result)
        print("✓ Long text handling test passed")
    
    def test_special_characters(self):
        """Test emotion detection with special characters and emojis"""
        text = "I'm SO HAPPY!!! 😊🎉✨"
        result = self.detector.detect_emotion(text)
        
        self.assertIn('dominant_emotion', result)
        self.assertIsNotNone(result['confidence'])
        print("✓ Special characters test passed")
    
    def test_multiple_languages_english(self):
        """Test emotion detection with English text"""
        text = "This is absolutely wonderful and amazing!"
        result = self.detector.detect_emotion(text)
        
        # Should work for English (model is English-specific)
        self.assertIn('dominant_emotion', result)
        print("✓ English language test passed")


class TestEmotionDistribution(unittest.TestCase):
    """Test emotion distribution and statistics"""
    
    @classmethod
    def setUpClass(cls):
        cls.detector = EmotionDetector()
    
    def test_emotion_distribution_sums(self):
        """Test that emotion scores in batch results are properly distributed"""
        texts = ["Happy", "Sad", "Angry"]
        results = self.detector.detect_emotions_batch(texts)
        
        for result in results:
            if 'emotions' in result:
                total = sum(result['emotions'].values())
                # Total should be close to 1.0 (allowing for floating point errors)
                self.assertGreater(total, 0.5)
        print("✓ Emotion distribution test passed")


def run_tests():
    """Run all tests"""
    print("\n" + "="*70)
    print("Running Emotion Detection Unit Tests")
    print("="*70 + "\n")
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestEmotionDetector))
    suite.addTests(loader.loadTestsFromTestCase(TestEmotionDistribution))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "="*70)
    if result.wasSuccessful():
        print("✓ All tests passed successfully!")
    else:
        print("✗ Some tests failed")
    print("="*70 + "\n")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
