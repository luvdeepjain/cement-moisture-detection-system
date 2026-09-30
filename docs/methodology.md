# Project Methodology

## 1. Problem Identification

Manual monitoring of moisture during curing can require repeated inspection and manual water application.

## 2. System Design

A sensor-based automated monitoring system was proposed using Raspberry Pi 5, ADS1115, relay control, and IoT monitoring.

## 3. Hardware Integration

The capacitive moisture sensor is connected to the ADS1115 ADC. The ADS1115 communicates with the Raspberry Pi through the I2C interface.

The Raspberry Pi controls the water pump through a relay module.

## 4. Software Development

The software is divided into independent modules:

* `main.py` — main application
* `moisture_sensor.py` — sensor testing
* `relay_control.py` — relay testing
* `config.py` — system configuration
* `control_logic.py` — moisture control logic
* `blynk_monitor.py` — IoT monitoring

## 5. Calibration

Sensor readings will be collected under controlled dry and wet conditions.

The calibration values will then be updated in the software.

## 6. Testing

Testing will include:

* Sensor response testing
* ADC reading verification
* Relay switching test
* Moisture threshold test
* Pump control test
* Blynk communication test
* Continuous operation test

## 7. Validation

The complete prototype will be evaluated using measured sensor readings and observed system behavior.

## Current Status

Software architecture and documentation are prepared.

Physical hardware integration and experimental validation are pending.
