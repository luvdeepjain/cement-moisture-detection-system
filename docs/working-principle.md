# Working Principle

The system operates as a closed-loop moisture monitoring and water control system.

## Step 1 — Moisture Sensing

The capacitive moisture sensor detects changes in the moisture condition of the test material and produces an analog output voltage.

## Step 2 — Analog-to-Digital Conversion

The ADS1115 receives the analog sensor output and converts it into a digital value that can be processed by the Raspberry Pi 5.

## Step 3 — Data Processing

The Raspberry Pi reads the sensor voltage and applies the configured calibration relationship to estimate a moisture percentage.

## Step 4 — Threshold Comparison

The estimated moisture level is compared with the configured threshold.

The current prototype uses **40% as a configurable threshold**.

## Step 5 — Automatic Water Control

If the estimated moisture level falls below the threshold, the Raspberry Pi commands the relay to activate the water pump.

When the moisture level reaches or exceeds the threshold, the pump is switched off.

## Step 6 — IoT Monitoring

When Blynk IoT is enabled, the system can transmit:

* Estimated moisture percentage
* Sensor voltage
* Pump status

## Important Calibration Note

The moisture percentage is only an estimate until the sensor is calibrated using actual measurements from the intended cement/concrete application.

The 40% value is therefore treated as a configurable prototype threshold rather than a validated concrete-curing standard.
