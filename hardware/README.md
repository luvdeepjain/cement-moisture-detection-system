# Hardware

## Main Components

| Component                  | Purpose                      |
| -------------------------- | ---------------------------- |
| Raspberry Pi 5             | Main controller              |
| ADS1115                    | Analog-to-digital conversion |
| Capacitive Moisture Sensor | Moisture sensing             |
| Relay Module               | Pump control                 |
| Water Pump                 | Automated water supply       |
| Sprinkler                  | Water distribution           |
| Breadboard                 | Prototype connections        |
| Jumper Wires               | Electrical connections       |

## System Hardware Flow

Capacitive Moisture Sensor
↓
ADS1115 ADC
↓
Raspberry Pi 5
↓
Relay Module
↓
Water Pump
↓
Sprinkler

## Hardware Status

Hardware integration is currently pending.

The Raspberry Pi and prototype hardware will be used for physical testing, calibration, and validation.

## Safety

The pump must not be connected directly to a Raspberry Pi GPIO.

The relay must be correctly rated for the pump and its power supply. Mains-powered equipment should only be handled with appropriate electrical isolation and safety precautions.
