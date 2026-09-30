# Testing Plan

## Software Testing

The control algorithm can be tested on a Windows computer using simulated sensor values.

### Test Cases

| Test                  | Expected Result    |
| --------------------- | ------------------ |
| Dry calibration value | Approximately 0%   |
| Wet calibration value | Approximately 100% |
| Midpoint value        | Approximately 50%  |
| Moisture below 40%    | Pump command ON    |
| Moisture at 40%       | Pump command OFF   |
| Moisture above 40%    | Pump command OFF   |
| Invalid calibration   | Error generated    |

## Hardware Testing

To be performed when the Raspberry Pi and hardware are available.

### Planned Tests

1. Verify ADS1115 I2C communication.
2. Verify sensor voltage readings.
3. Record dry-condition readings.
4. Record wet-condition readings.
5. Calibrate the sensor.
6. Test relay without pump.
7. Verify pump switching.
8. Test automatic moisture control.
9. Test Blynk communication.
10. Perform continuous operation testing.

## Validation Status

| Test Category          | Status   |
| ---------------------- | -------- |
| Software control logic | Prepared |
| Windows simulation     | Prepared |
| ADS1115 hardware test  | Pending  |
| Sensor calibration     | Pending  |
| Relay test             | Pending  |
| Pump test              | Pending  |
| Blynk test             | Pending  |
| Full system validation | Pending  |
