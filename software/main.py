```python
"""
Cement Moisture Detection and Automated Curing System

Controller:
    Raspberry Pi 5

Sensor:
    Capacitive moisture sensor -> ADS1115 ADC

Actuator:
    Relay -> Water pump / sprinkler

Logic:
    If moisture falls below the configured threshold,
    the sprinkler is activated.

NOTE:
    Moisture percentage conversion must be calibrated
    using actual sensor readings from the prototype.
"""

import time
import board
import busio
import digitalio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


# ============================================================
# CONFIGURATION
# ============================================================

# ADS1115 channel
MOISTURE_CHANNEL = ADS.P0

# Raspberry Pi GPIO17 -> Relay IN
RELAY_PIN = board.D17

# Prototype threshold
MOISTURE_THRESHOLD = 40.0

# Sensor calibration values
# These values MUST be replaced after real hardware calibration.
DRY_VOLTAGE = 1.50
WET_VOLTAGE = 1.30

# Time between readings
READ_INTERVAL = 2


# ============================================================
# INITIALIZE I2C AND ADS1115
# ============================================================

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)

moisture_sensor = AnalogIn(ads, MOISTURE_CHANNEL)


# ============================================================
# INITIALIZE RELAY
# ============================================================

relay = digitalio.DigitalInOut(RELAY_PIN)
relay.direction = digitalio.Direction.OUTPUT

# Relay OFF at startup
relay.value = False


# ============================================================
# FUNCTIONS
# ============================================================

def read_moisture():
    """
    Read voltage from the capacitive moisture sensor
    and convert it to an estimated percentage.

    IMPORTANT:
    This percentage is only an estimate until the sensor
    is calibrated for the actual cement/concrete application.
    """

    voltage = moisture_sensor.voltage

    # Convert voltage to percentage.
    # Higher voltage = drier condition in this prototype setup.
    moisture = (
        (DRY_VOLTAGE - voltage)
        / (DRY_VOLTAGE - WET_VOLTAGE)
    ) * 100

    # Keep percentage between 0 and 100
    moisture = max(0.0, min(100.0, moisture))

    return voltage, moisture


def sprinkler_on():
    """Turn the water sprinkler ON."""
    relay.value = True
    print("SPRINKLER: ON")


def sprinkler_off():
    """Turn the water sprinkler OFF."""
    relay.value = False
    print("SPRINKLER: OFF")


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("=" * 55)
    print("CEMENT MOISTURE DETECTION & AUTOMATED CURING SYSTEM")
    print("=" * 55)
    print("System started.")
    print("Moisture threshold:", MOISTURE_THRESHOLD, "%")
    print()

    try:

        while True:

            voltage, moisture = read_moisture()

            print(f"Sensor Voltage : {voltage:.3f} V")
            print(f"Moisture       : {moisture:.2f}%")

            # ------------------------------------------------
            # AUTOMATIC SPRINKLER CONTROL
            # ------------------------------------------------

            if moisture < MOISTURE_THRESHOLD:

                print("Moisture below threshold.")
                sprinkler_on()

            else:

                print("Moisture level sufficient.")
                sprinkler_off()

            print("-" * 55)

            time.sleep(READ_INTERVAL)

    except KeyboardInterrupt:

        print("\nProgram stopped by user.")

    finally:

        # Always switch the sprinkler OFF
        # when the program exits.
        sprinkler_off()
        relay.deinit()

        print("System safely shut down.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
```
