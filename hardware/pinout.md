# Raspberry Pi 5 Pinout

## ADS1115 Connections

| Raspberry Pi 5      | ADS1115 |
| ------------------- | ------- |
| 3.3V — Pin 1        | VDD     |
| GND — Pin 6         | GND     |
| GPIO2 / SDA — Pin 3 | SDA     |
| GPIO3 / SCL — Pin 5 | SCL     |

## Moisture Sensor

| Sensor | ADS1115 / Raspberry Pi |
| ------ | ---------------------- |
| VCC    | 3.3V                   |
| GND    | Common GND             |
| AOUT   | ADS1115 A0             |

## Relay

| Relay Module | Raspberry Pi                    |
| ------------ | ------------------------------- |
| IN           | GPIO17 — Pin 11                 |
| GND          | Common GND                      |
| VCC          | Appropriate relay-module supply |

## Important

The exact relay module pinout, activation polarity, and power requirements must be verified from the physical module before connecting the pump.

The pump should have its own suitable power supply and must not be powered directly from a Raspberry Pi GPIO.
