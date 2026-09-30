"""
Cement Moisture Detection and Automated Curing System
Main Application

Hardware:
Raspberry Pi 5
ADS1115 ADC
Capacitive moisture sensor
Relay-controlled sprinkler

Modules:
config.py
blynk_monitor.py
"""

import time
import board
import busio
import digitalio

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import config
from blynk_monitor import BlynkMonitor

def calculate_moisture(voltage):
"""
Estimate moisture percentage using calibration values.

```
This calculation is only a placeholder until the sensor
is calibrated for the actual cement/concrete application.
"""

voltage_range = config.DRY_VOLTAGE - config.WET_VOLTAGE

if voltage_range <= 0:
    raise ValueError(
        "DRY_VOLTAGE must be greater than WET_VOLTAGE."
    )

moisture = (
    (config.DRY_VOLTAGE - voltage) / voltage_range
) * 100.0

return max(0.0, min(100.0, moisture))
```

def set_pump(relay, pump_on):
"""Set the relay output according to its configured polarity."""

```
if config.RELAY_ACTIVE_HIGH:
    relay.value = pump_on
else:
    relay.value = not pump_on
```

def main():
i2c = None
relay = None
pump_on = False

```
try:
    print("=" * 55)
    print("CEMENT MOISTURE AUTOMATION SYSTEM")
    print("=" * 55)

    # Initialize ADS1115 sensor interface
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    sensor = AnalogIn(ads, ADS.P0)

    # Initialize relay and set it to OFF
    relay = digitalio.DigitalInOut(board.D17)
    relay.direction = digitalio.Direction.OUTPUT
    set_pump(relay, False)

    # Initialize optional Blynk monitoring
    monitor = BlynkMonitor(enabled=config.BLYNK_ENABLED)

    print("Sensor initialized on ADS1115 A0.")
    print(f"Moisture threshold: {config.MOISTURE_THRESHOLD}%")
    print("Press Ctrl+C to stop.\n")

    while True:
        voltage = sensor.voltage
        moisture = calculate_moisture(voltage)

        # Automatic control
        if moisture < config.MOISTURE_THRESHOLD:
            desired_pump_state = True
        else:
            desired_pump_state = False

        # Update relay only when the desired state changes
        if desired_pump_state != pump_on:
            pump_on = desired_pump_state
            set_pump(relay, pump_on)

        # Display current readings
        print(
            f"Voltage: {voltage:.3f} V | "
            f"Estimated moisture: {moisture:.1f}% | "
            f"Pump: {'ON' if pump_on else 'OFF'}"
        )

        # Send readings to Blynk if enabled
        monitor.update(voltage=voltage, moisture=moisture,
                       pump_on=pump_on)

        time.sleep(config.READ_INTERVAL)

except KeyboardInterrupt:
    print("\nShutdown requested.")

except Exception as error:
    print(f"System error: {error}")

finally:
    # Attempt to leave the pump switched OFF
    if relay is not None:
        try:
            set_pump(relay, False)
            relay.deinit()
        except Exception:
            pass

    if i2c is not None:
        try:
            i2c.deinit()
        except Exception:
            pass

    print("Shutdown complete.")
```

if **name** == "**main**":
main()
