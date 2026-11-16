# SX1262 Notes

## Documents used
- Datasheet: (name, version, date)
- Reference design: (name, version, date)

## Pin table (fill from datasheet pinout figure)
| Pin # | Name | Function | Connects to | Notes |
|-------|------|----------|-------------|-------|
| | NSS | SPI chip select | MCU GPIO | |
| | SCK | SPI clock | MCU SCK | |
| | MOSI | SPI data in | MCU MOSI | |
| | MISO | SPI data out | MCU MISO | |
| | BUSY | Busy flag | MCU GPIO | wait low before commands |
| | NRESET | Reset (active low) | MCU GPIO | |
| | DIO1 | Interrupt | MCU GPIO (interrupt) | |
| | DIO2 | RF switch control | Switch control pin | high = TX |
| | DIO3 | TCXO supply | TCXO supply pin | |
| | XTA | Clock input | TCXO via resistor + capacitor | |
| | XTB | Crystal pin | (see datasheet for TCXO case) | |
| | RFO | PA output | TX match/filter | |
| | RFI_P / RFI_N | Differential RX input | RX match | |
| | VBAT / VBAT_IO / VDD_IN | Supplies | 3.3 V + decoupling | |
| | DCC_SW | DC-DC switch node | Inductor | |
| | VREG | Regulator output | Capacitor to GND | |
| | VR_PA | PA regulator output | Capacitor to GND | |
| | GND / exposed pad | Ground | Ground plane | |

## Decisions
- Regulator: DC-DC or LDO? Why: DC-DC because it is more efficient
- Inductor: value / part / shielded? DC resistance:
- Clock: TXCO because of the ppm requirement for the sx1262 of +/- 5ppm. Part, frequency, ppm:
- DIO3 TCXO voltage setting:
- RF topology: split TX/RX with switch, or direct tie? Why: split TX/RX as it is more flexible and gives test points
- MCU: ESP32 or STM32? Part: ESP32 was chosen due to familiarity, already having the part, and easier to use.

## Reference design components (copy values, then explain each)
| Ref | Value | Purpose | Why this value |
|-----|-------|---------|----------------|
| | | | |

## Open questions
-
