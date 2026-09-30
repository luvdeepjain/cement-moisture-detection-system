"""
Blynk IoT Monitoring Module
Cement Moisture Detection and Automated Curing System

Virtual pins:
V1 -> Moisture percentage
V2 -> Sensor voltage
V3 -> Pump status

Blynk integration can be enabled after configuring
the Blynk template and obtaining an authentication token.
"""

import os

try:
import BlynkLib
except ImportError:
BlynkLib = None

class BlynkMonitor:

```
def __init__(self, enabled=False):
    self.enabled = enabled
    self.blynk = None

    if not self.enabled:
        print("Blynk monitoring disabled.")
        return

    if BlynkLib is None:
        print("Blynk library not installed.")
        self.enabled = False
        return

    token = os.getenv("BLYNK_AUTH_TOKEN")

    if not token:
        print("BLYNK_AUTH_TOKEN environment variable not set.")
        self.enabled = False
        return

    try:
        self.blynk = BlynkLib.Blynk(token)
        print("Blynk client initialized.")
    except Exception as error:
        print(f"Blynk initialization failed: {error}")
        self.enabled = False

def update(self, moisture, voltage, pump_on):
    """Publish the latest readings and pump status."""

    if not self.enabled or self.blynk is None:
        return

    try:
        self.blynk.virtual_write("V1", round(moisture, 2))
        self.blynk.virtual_write("V2", round(voltage, 3))
        self.blynk.virtual_write("V3", 1 if pump_on else 0)
        self.blynk.run()

    except Exception as error:
        print(f"Blynk update failed: {error}")

def run(self):
    """Process Blynk communication events."""

    if self.enabled and self.blynk is not None:
        try:
            self.blynk.run()
        except Exception as error:
            print(f"Blynk communication error: {error}")
```
