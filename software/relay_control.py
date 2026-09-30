```python
"""
Relay Control Test
Cement Moisture Detection and Automated Curing System

Controller:
    Raspberry Pi 5

Relay:
    GPIO17 (Physical Pin 11)

Purpose:
    Test relay ON/OFF control before connecting
    the water pump or sprinkler.

IMPORTANT:
    Test the relay first without connecting the pump.
"""

import time
import board
import digitalio


# ------------------------------------------------------------
# Relay Configuration
# ------------------------------------------------------------

RELAY_PIN = board.D17


# ------------------------------------------------------------
# Initialize GPIO
# ------------------------------------------------------------

relay = digitalio.DigitalInOut(RELAY_PIN)
relay.direction = digitalio.Direction.OUTPUT


# ------------------------------------------------------------
# Relay Functions
# ------------------------------------------------------------

def relay_on():
    """Activate the relay."""
    relay.value = True
    print("Relay: ON")


def relay_off():
    """Deactivate the relay."""
    relay.value = False
    print("Relay: OFF")


# ------------------------------------------------------------
# Main Test
# ------------------------------------------------------------

print("=" * 50)
print("RELAY CONTROL TEST")
print("=" * 50)
print("GPIO17 / Physical Pin 11")
print("Press Ctrl+C to stop.")
print()


try:

    while True:

        # Turn relay ON
        relay_on()
        time.sleep(3)

        # Turn relay OFF
        relay_off()
        time.sleep(3)


except KeyboardInterrupt:

    print("\nRelay test stopped.")


finally:

    # Make sure relay is OFF when program exits
    relay_off()
    relay.deinit()

    print("Relay safely switched OFF.")
```
