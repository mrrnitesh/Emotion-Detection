"""
Main Application - Emotion Detection CLI Interface
Interactive command-line tool for emotion detection
"""

import sys
from emotion_detector import EmotionDetector
import json
from typing import List


class EmotionDetectionApp:
    """Interactive CLI application for emotion detection"""
    
    def __init__(self):
        """Initialize the application"""
        self.detector = None
        self.history = []
        self.initialize()
    
    def initialize(self):
        """Initialize the emotion detector"""
        print("\n" + "="*70)
        print("EMOTION DETECTION APPLICATION")
        print("="*70)
        print("\nInitializing Watson NLP Emotion Detector...")
        
        try:
            self.detector = EmotionDetector()
            print("✓ Detector initialized successfully!\n")
        except Exception as e:
            print(f"✗ Error initializing detector: {e}")
            sys.exit(1)
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "-"*70)
        print("MENU - Select an option:")
        print("-"*70)
        print("1. Analyze single text")
        print("2. Analyze multiple texts (batch)")
        print("3. Get emotion summary")
        print("4. View analysis history")
        print("5. Export results to JSON")
        print("6. Help & Documentation")
        print("7. Exit")
        print("-"*70)
    
    def option_single_text(self):
        """Option 1: Analyze a single text"""
        print("\n" + "="*70)
        print("ANALYZE SINGLE TEXT")
        print("="*70)
        
        text = input("\nEnter text to analyze: ").strip()
        
        if not text:
            print("✗ No text provided!")
            return
        
        try:
            result = self.detector.detect_emotion(text)
            self.history.append(result)
            self.display_single_result(result)
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def option_batch_texts(self):
        """Option 2: Analyze multiple texts"""
        print("\n" + "="*70)
        print("ANALYZE MULTIPLE TEXTS")
        print("="*70)
        
        texts = []
        print("\nEnter texts one by one (empty line to finish):")
        
        while True:
            text = input(f"Text {len(texts)+1}: ").strip()
            if not text:
                break
            texts.append(text)
        
        if not texts:
            print("✗ No texts provided!")
            return
        
        try:
            results = self.detector.detect_emotions_batch(texts)
            
            print("\n" + "="*70)
            print("BATCH ANALYSIS RESULTS")
            print("="*70)
            
            for i, result in enumerate(results, 1):
                print(f"\n[{i}] {result['text'][:50]}...")
                self.display_emotion_bars(result['emotions'])
                print(f"    Dominant: {result['dominant_emotion'].upper()} "
                      f"({result['confidence']:.2%})")
            
            self.history.extend(results)
            
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def option_emotion_summary(self):
        """Option 3: Get emotion summary"""
        print("\n" + "="*70)
        print("EMOTION SUMMARY")
        print("="*70)
        
        texts = []
        print("\nEnter texts for summary (empty line to finish):")
        
        while True:
            text = input(f"Text {len(texts)+1}: ").strip()
            if not text:
                break
            texts.append(text)
        
        if not texts:
            print("✗ No texts provided!")
            return
        
        try:
            summary = self.detector.get_emotion_summary(texts)
            
            print("\n" + "="*70)
            print("SUMMARY STATISTICS")
            print("="*70)
            print(f"\nTotal texts analyzed: {summary['total_texts_analyzed']}")
            print(f"Overall dominant emotion: {summary['dominant_emotion'].upper()}")
            print("\nAverage emotion distribution:")
            
            self.display_emotion_bars(summary['average_emotions'])
            
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def option_view_history(self):
        """Option 4: View analysis history"""
        print("\n" + "="*70)
        print("ANALYSIS HISTORY")
        print("="*70)
        
        if not self.history:
            print("\nNo analysis history yet.")
            return
        
        print(f"\nTotal analyses: {len(self.history)}\n")
        
        for i, result in enumerate(self.history, 1):
            text = result.get('text', 'Unknown')[:50]
            emotion = result.get('dominant_emotion', 'unknown')
            confidence = result.get('confidence', 0)
            
            print(f"[{i}] {text}...")
            print(f"    → {emotion} ({confidence:.2%})\n")
    
    def option_export_results(self):
        """Option 5: Export results to JSON"""
        if not self.history:
            print("\n✗ No analysis history to export!")
            return
        
        filename = input("\nEnter filename to save (without extension): ").strip()
        if not filename:
            filename = "emotion_results"
        
        try:
            filepath = f"{filename}.json"
            
            # Prepare data for export
            export_data = []
            for result in self.history:
                export_data.append({
                    'text': result.get('text', ''),
                    'dominant_emotion': result.get('dominant_emotion', ''),
                    'confidence': result.get('confidence', 0),
                    'emotions': result.get('emotions', {})
                })
            
            with open(filepath, 'w') as f:
                json.dump(export_data, f, indent=2)
            
            print(f"\n✓ Results exported to {filepath}")
        
        except Exception as e:
            print(f"✗ Error exporting: {e}")
    
    def option_help(self):
        """Option 6: Display help and documentation"""
        print("\n" + "="*70)
        print("HELP & DOCUMENTATION")
        print("="*70)
        
        help_text = """
EMOTION DETECTION APPLICATION HELP

FEATURES:
- Analyze single texts for emotions
- Process multiple texts in batch
- Get summary statistics
- View analysis history
- Export results to JSON

EMOTIONS DETECTED:
• JOY (😊): Happiness, delight, satisfaction
• SADNESS (😢): Sorrow, unhappiness
• ANGER (😠): Irritation, frustration
• FEAR (😨): Anxiety, worry, nervousness
• DISGUST (🤢): Aversion, repulsion

TIPS:
1. Longer texts generally provide better accuracy
2. Confidence score indicates reliability (0.0-1.0)
3. High confidence: > 0.7
4. Low confidence: < 0.5 (may indicate mixed emotions)

CONFIDENCE INTERPRETATION:
- 0.9+: Very high confidence
- 0.7-0.9: High confidence
- 0.5-0.7: Moderate confidence
- <0.5: Low confidence / mixed emotions

EXAMPLES:
Good: "I absolutely love this amazing product!"
Less accurate: "Good"
Sarcasm may confuse the model

For more information, see README.md
"""
        print(help_text)
    
    def display_single_result(self, result):
        """Display results for a single text analysis"""
        print("\n" + "="*70)
        print("ANALYSIS RESULT")
        print("="*70)
        
        print(f"\nText: {result['text']}")
        print(f"\nDominant Emotion: {result['dominant_emotion'].upper()}")
        print(f"Confidence: {result['confidence']:.2%}")
        
        print("\nEmotion Scores:")
        self.display_emotion_bars(result['emotions'])
    
    def display_emotion_bars(self, emotions):
        """Display emotion scores as visual bars"""
        for emotion, score in emotions.items():
            bar_length = int(score * 30)
            bar = "█" * bar_length + "░" * (30 - bar_length)
            print(f"  {emotion:10} [{bar}] {score:.4f}")
    
    def run(self):
        """Run the main application loop"""
        while True:
            self.display_menu()
            choice = input("\nSelect option (1-7): ").strip()
            
            try:
                if choice == '1':
                    self.option_single_text()
                elif choice == '2':
                    self.option_batch_texts()
                elif choice == '3':
                    self.option_emotion_summary()
                elif choice == '4':
                    self.option_view_history()
                elif choice == '5':
                    self.option_export_results()
                elif choice == '6':
                    self.option_help()
                elif choice == '7':
                    print("\n✓ Thank you for using Emotion Detection App!")
                    print("="*70 + "\n")
                    break
                else:
                    print("✗ Invalid option. Please select 1-7.")
            
            except KeyboardInterrupt:
                print("\n\n✓ Application terminated by user.")
                break
            except Exception as e:
                print(f"✗ Unexpected error: {e}")


def main():
    """Main entry point"""
    try:
        app = EmotionDetectionApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n✓ Application terminated by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
