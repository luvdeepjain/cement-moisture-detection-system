# System Architecture

## Overview

The system continuously monitors moisture conditions using a capacitive moisture sensor. Since the sensor produces an analog signal, an ADS1115 ADC is used to convert the signal into digital data that can be processed by the Raspberry Pi 5.

The Raspberry Pi evaluates the moisture level and controls a relay connected to a water pump or sprinkler.

## Architecture

```text
             ┌─────────────────────────┐
             │ Capacitive Moisture     │
             │ Sensor                  │
             └────────────┬────────────┘
                          │ Analog Signal
                          ▼
             ┌─────────────────────────┐
             │ ADS1115 ADC             │
             └────────────┬────────────┘
                          │ I2C
                          ▼
             ┌─────────────────────────┐
             │ Raspberry Pi 5          │
             │                         │
             │ Moisture Processing     │
             │ Control Logic           │
             │ Data Monitoring         │
             └───────┬─────────┬───────┘
                     │         │
                     │         │ Wi-Fi
                     │         ▼
                     │   ┌─────────────┐
                     │   │ Blynk IoT   │
                     │   └─────────────┘
                     │
                     ▼
             ┌─────────────────────────┐
             │ Relay Module            │
             └────────────┬────────────┘
                          │
                          ▼
             ┌─────────────────────────┐
             │ Water Pump / Sprinkler  │
             └─────────────────────────┘
```

## Main Functions

1. Measure moisture sensor output.
2. Convert the analog signal using ADS1115.
3. Process the reading using Raspberry Pi 5.
4. Estimate moisture using calibration data.
5. Compare the result with the configured threshold.
6. Activate or deactivate the pump through the relay.
7. Send monitoring information to Blynk when enabled.
