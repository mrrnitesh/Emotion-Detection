# Emotion Detection Configuration

# Model Configuration
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
CACHE_DIRECTORY = None  # Set to a path to cache models locally

# Emotion Labels
EMOTIONS = {
    'sadness': '😢',
    'joy': '😊',
    'fear': '😨',
    'disgust': '🤢',
    'anger': '😠'
}

# Confidence Threshold (0.0 to 1.0)
# Results with confidence below this threshold may be considered uncertain
CONFIDENCE_THRESHOLD = 0.3

# Logging Configuration
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = "emotion_detection.log"

# Output Configuration
OUTPUT_FORMAT = "json"  # json, csv, or text
SAVE_RESULTS = False
RESULTS_FILE = "emotion_results.json"

# Batch Processing
BATCH_SIZE = 10
MAX_TEXT_LENGTH = 5000  # Maximum characters per text

# Advanced Settings
USE_GPU = False  # Enable GPU acceleration if available
NUM_WORKERS = 1  # Number of parallel workers for batch processing
