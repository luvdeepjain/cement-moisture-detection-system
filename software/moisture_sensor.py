```python
"""
Cement Moisture Sensor Test

Hardware:
    Raspberry Pi 5
    ADS1115 ADC
    Capacitive Moisture Sensor

Connection:
    Sensor AOUT -> ADS1115 A0
    ADS1115 SDA -> Raspberry Pi GPIO2
    ADS1115 SCL -> Raspberry Pi GPIO3
"""

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


# ------------------------------------------------------------
# Initialize I2C
# ------------------------------------------------------------

i2c = busio.I2C(board.SCL, board.SDA)

# Initialize ADS1115
ads = ADS.ADS1115(i2c)

# Use ADS1115 channel A0
channel = AnalogIn(ads, ADS.P0)


# ------------------------------------------------------------
# Display sensor readings
# ------------------------------------------------------------

print("=" * 50)
print("CEMENT MOISTURE SENSOR TEST")
print("=" * 50)
print("Reading ADS1115 Channel A0...")
print("Press Ctrl+C to stop.")
print()


try:

    while True:

        raw_value = channel.value
        voltage = channel.voltage

        print(f"Raw ADC Value : {raw_value}")
        print(f"Sensor Voltage: {voltage:.3f} V")
        print("-" * 50)

        time.sleep(1)


except KeyboardInterrupt:

    print("\nSensor test stopped.")
```
