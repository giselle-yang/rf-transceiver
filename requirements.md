# SX1262 Board: Draft Requirements (draft v0.1)

Goal: a 915 MHz transceiver board built around the Semtech SX1262, sending 10 kbps GFSK data about 1 km line of sight, mainly designed for testing.

## R1: Frequency
- **Requirement:** Operates 902-928 MHz, nominal 915 MHz. Reference frequency error no worse than +/-5 ppm.
- **Rationale:** ISM band for Canada. 5 ppm of 915 MHz is about 4.6 kHz, small compared with the 5 kHz deviation. Drives the crystal vs. TCXO choice.
- **Verification:** Measure an unmodulated carrier on a calibrated SDR.

## R2: Output power
- **Requirement:** Conducted output at the SMA connector programmable up to at least +20 dBm, and at least +17 dBm at the maximum setting.
- **Rationale:** Chip maximum is about +22 dBm, minus an estimated 2 dB of board loss (filter, switch, matching), leaving 2-3 dB of slack. Legal limit to be confirmed in RSS-247.
- **Verification:** Through a 30 dB attenuator into a power meter or spectrum analyzer.

## R3: Data rate and modulation
- **Requirement:** 10 kbps GFSK, 5 kHz deviation (about 20 kHz occupied bandwidth).
- **Rationale:** Original goal. Carson's rule: 2 x (5 + 5) = 20 kHz.
- **Verification:** Spectrum capture on the SDR, and decode on the receiving board.

## R4: Receiver sensitivity
- **Requirement:** Packet error rate (PER) of 1% or better at -110 dBm or stronger input, 10 kbps GFSK.
- **Rationale:** Datasheet interpolates to about -115 dBm at 10 kbps. About 2 dB of expected board loss plus 3 dB of slack.
- **Verification:** Conducted attenuator sweep with at least 300 packets per level.

## R5: Range
- **Requirement:** At least 1 km line-of-sight range with at least 10 dB of link margin.
- **Rationale:** Link budget gives 42 dB margin in free space and about 12 dB at path-loss exponent n = 3.
- **Verification:** Outdoor range test, logging RSSI and PER.

## R6: Antenna port match
- **Requirement:** Return loss of at least 10 dB at the SMA connector across 902-928 MHz.
- **Rationale:** 10 dB return loss means 10% of power reflected, about 0.46 dB mismatch loss.
- **Verification:** Calibrated NanoVNA S11 sweep.

## R7: Harmonics and spurious emissions
- **Requirement:** Unwanted emissions within ISED limits. Limit: TBD from RSS-247 and RSS-Gen.
- **Rationale:** Regulatory compliance. Second harmonic is at 1830 MHz, third at 2745 MHz.
- **Verification:** Spectrum analyzer, conducted, through attenuation.

## R8: Power supply
- **Requirement:** 3.3 V supply. Voltage droop at the SX1262 of no more than 100 mV during a transmit burst.
- **Rationale:** Chip needs 3.3 V for full output power, and transmit current is around 120 mA. The 100 mV target is my own engineering choice, not a datasheet value.
- **Verification:** Oscilloscope on the supply pin, triggered on transmit start.

## R9: Board and test access
- **Requirement:** 4-layer PCB, no larger than 50 x 50 mm, with an SMA connector, a pi-network footprint on the RF line, and test points for supply, reset, and SPI.
- **Rationale:** Solid ground plane under the RF path for predictable 50 ohm routing. Tunable pads and test points make tuning and bring-up possible.
- **Verification:** Design review against this list.

## Open items
- Crystal vs. TCXO (decided by R1)
- ESP32 vs. STM32
- Exact limits from RSS-247 and RSS-Gen (R2, R7)
- Real insertion losses of the chosen switch and filter (R2, R4)
