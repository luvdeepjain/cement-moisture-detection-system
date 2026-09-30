"""
Configuration Settings
Cement Moisture Detection and Automated Curing System

Central location for hardware pins, thresholds,
sensor calibration, and monitoring intervals.
"""

# ============================================================

# MOISTURE SENSOR SETTINGS

# ============================================================

# ADS1115 analog input channel

MOISTURE_CHANNEL = 0  # A0

# Placeholder calibration values (volts)

# Replace after measuring the actual sensor.

DRY_VOLTAGE = 1.50
WET_VOLTAGE = 1.30

# Prototype moisture threshold (%)

MOISTURE_THRESHOLD = 40.0

# ============================================================

# RASPBERRY PI SETTINGS

# ============================================================

# BCM GPIO numbering

RELAY_GPIO = 17

# Default assumption only; verify the relay module.

RELAY_ACTIVE_HIGH = True

# ============================================================

# AUTOMATION SETTINGS

# ============================================================

# Delay between sensor readings (seconds)

READ_INTERVAL = 2

# Future safety setting: maximum continuous pump runtime.

# Set to None until a suitable limit is established.

MAX_PUMP_RUNTIME_SECONDS = None

# ============================================================

# BLYNK IOT SETTINGS

# ============================================================

# Configure these when setting up your Blynk template.

BLYNK_ENABLED = False

# Never put a real authentication token in this file.

# Use an environment variable when Blynk is configured.

BLYNK_AUTH_TOKEN_ENV = "BLYNK_AUTH_TOKEN"

# Suggested virtual pin assignments

BLYNK_MOISTURE_PIN = "V1"
BLYNK_VOLTAGE_PIN = "V2"
BLYNK_PUMP_STATUS_PIN = "V3"
