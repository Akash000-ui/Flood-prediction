"""
Configuration File
Project settings and constants
"""

import os
from pathlib import Path


def _get_bool_env(name, default=False):
    """Parse a boolean environment variable safely."""
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {'1', 'true', 'yes', 'on'}

# Project Root
PROJECT_ROOT = Path(__file__).parent.parent

# Data Paths
DATA_DIR = PROJECT_ROOT / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
OUTPUTS_DIR = DATA_DIR / 'outputs'

# Model Paths
MODELS_DIR = PROJECT_ROOT / 'models'
MODEL_PATH = MODELS_DIR / 'random_forest_flood_model.pkl'

# Feature Configuration
FEATURE_COLUMNS = [
    'rainfall_7d_mm',
    'soil_moisture',
    'elevation_m',
    'slope_deg'
]

TARGET_COLUMN = 'flood_label'

# GEE Configuration
GEE_PROJECT = 'student-study-app-468414'  # Your GEE Cloud Project
GEE_BUFFER_METERS = 10000  # 10 km buffer around point
GEE_SAFE_DAYS_BACK = 30     # Use data from 30 days ago
GEE_WINDOW_DAYS = 7         # 7-day window for rainfall

# Datasets
CHIRPS_DATASET = 'UCSB-CHG/CHIRPS/DAILY'
ERA5_DATASET = 'ECMWF/ERA5_LAND/DAILY_AGGR'
SRTM_DATASET = 'USGS/SRTMGL1_003'

# Model Hyperparameters
RF_N_ESTIMATORS = 100
RF_MAX_DEPTH = 10
RF_MIN_SAMPLES_SPLIT = 5
RF_MIN_SAMPLES_LEAF = 2
RF_RANDOM_STATE = 42

# Train-Test Split
TEST_SIZE = 0.2
RANDOM_STATE = 42

# API Configuration
API_HOST = os.getenv('API_HOST', '0.0.0.0')
API_PORT = int(os.getenv('PORT', os.getenv('API_PORT', '5000')))
DEBUG_MODE = _get_bool_env('DEBUG_MODE', default=False)
FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'dev-only-change-this-secret')

# Comma-separated values, e.g. "https://your-app.onrender.com,http://localhost:5000"
CORS_ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        'CORS_ALLOWED_ORIGINS',
        'http://localhost:5000,http://127.0.0.1:5000'
    ).split(',')
    if origin.strip()
]

# Risk Level Thresholds
RISK_THRESHOLDS = {
    'HIGH': 0.7,
    'MEDIUM': 0.4,
    'LOW': 0.0
}

# Email Notification Configuration
EMAIL_NOTIFICATIONS_ENABLED = _get_bool_env('EMAIL_NOTIFICATIONS_ENABLED', default=False)
EMAIL_ALERT_THRESHOLD = float(os.getenv('EMAIL_ALERT_THRESHOLD', '0.5'))

# SMTP Configuration (Gmail example)
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
SMTP_USERNAME = os.getenv('SMTP_USERNAME', '')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', '')
SMTP_FROM_EMAIL = os.getenv('SMTP_FROM_EMAIL', SMTP_USERNAME)
SMTP_FROM_NAME = os.getenv('SMTP_FROM_NAME', 'Flood Prediction System')

# Default recipient email (can be overridden by user settings)
DEFAULT_ALERT_EMAIL = os.getenv('DEFAULT_ALERT_EMAIL', '')

# Google Earth Engine settings for server deployments
GEE_PROJECT = os.getenv('GEE_PROJECT', GEE_PROJECT)
GEE_SERVICE_ACCOUNT_EMAIL = os.getenv('GEE_SERVICE_ACCOUNT_EMAIL', '')
GEE_SERVICE_ACCOUNT_KEY = os.getenv('GEE_SERVICE_ACCOUNT_KEY', '')

# Optional weather API settings
USE_WEATHER_API = _get_bool_env('USE_WEATHER_API', default=False)
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', '')
WEATHER_API_DAYS_BACK = int(os.getenv('WEATHER_API_DAYS_BACK', '7'))

print(f"✓ Configuration loaded from {__file__}")
