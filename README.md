
# IoT-Based Cement Moisture Detection System

## Project Overview

This project monitors cement or concrete surface moisture and automates water sprinkler control using a Raspberry Pi 5, a capacitive moisture sensor, an ADS1115 analog-to-digital converter, and a relay module.

## Objectives

* Monitor moisture readings in real time.
* Process analog sensor data using the ADS1115.
* Activate a sprinkler when the calibrated moisture reading falls below a configured threshold.
* Enable remote monitoring using Blynk IoT.
* Reduce unnecessary water consumption and manual intervention.

## Hardware Components

* Raspberry Pi 5
* Capacitive moisture sensor
* ADS1115 ADC module
* SRD-05VDC-SL-C relay or compatible relay module
* Water pump or sprinkler
* Jumper wires and power supply

## System Architecture

Moisture Sensor → ADS1115 → Raspberry Pi 5 → Relay → Sprinkler

Blynk IoT provides remote monitoring when configured.

## Software

* Python
* Raspberry Pi OS
* Adafruit Blinka
* Adafruit ADS1x15 library
* Blynk IoT

## Current Development Status

Hardware integration, sensor calibration, automated relay control, and IoT monitoring are being developed and tested.

## Safety and Calibration

The 40% threshold is a configurable prototype setting and must be calibrated against appropriate moisture measurements. Sensor output alone does not establish the actual moisture content or curing quality of concrete.

Test the relay without a pump before connecting the complete system.

## Author Contributions

Document each team member's actual hardware, software, testing, and documentation contributions.

## License

To be decided.
