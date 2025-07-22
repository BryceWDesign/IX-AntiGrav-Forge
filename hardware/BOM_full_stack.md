# BOM_full_stack.md  
## Bill of Materials — IX-AntiGrav-Forge Full System Stack

---

### 📌 Objective

This document outlines all required components, subcomponents, and materials necessary to physically construct the full IX-AntiGrav-Forge system.  
It is broken down by subsystem, includes reference models, and emphasizes **non-exotic**, commercially available parts only.

No black-box components. No proprietary systems. All items can be sourced or fabricated within standard open-source or research-grade fabrication environments.

---

## 🧱 Subsystem Index

1. EM Inertia Cancellation Module  
2. Dual Spin-Loop Shell  
3. Vacuum Interaction Cell  
4. Acoustic & EM Lift Shell  
5. Harmonic Control Loop  
6. Power + Safety System  
7. Enclosure & Structural Mounting

---

## 🔧 1. EM Inertia Cancellation Module

| Qty | Component | Notes |
|-----|-----------|-------|
| 6 | Helmholtz coil sets (X/Y/Z) | Litz-wound copper, 12–24 AWG |
| 3 | 3-axis MEMS accelerometer/gyroscope units | e.g., Bosch BMI088 or ADIS16448 |
| 3 | Precision DAC + H-Bridge drivers | Analog current modulation, 2A minimum |
| 1 | Microcontroller or FPGA board | With 3+ ADC channels, PWM control |
| 6 | High-frequency Hall sensors | Optional, for field calibration |

---

## 🔁 2. Dual Spin-Loop Shell

| Qty | Component | Notes |
|-----|-----------|-------|
| 2 | Toroidal coil cores | Soft ferrite or air core, ~8–12 cm OD |
| 2 | High-speed field rotation drivers | Phase-inverted current drivers |
| 1 | Magnetic flux probe array | For loop monitoring and phase tracking |
| 1 | Mounting bracket set | Coil isolation to prevent mechanical resonance |

---

## 🌌 3. Vacuum Interaction Cell

| Qty | Component | Notes |
|-----|-----------|-------|
| 2 | Graphene-coated conductive plates | Optional: optically flat aluminum or gold |
| 2 | Piezo actuator arms | Nanometer-scale precision |
| 1 | Vacuum chamber (miniature) | ≤10⁻³ Torr, 10–15 cm internal clearance |
| 1 | Vacuum pump | Rotary vane or diaphragm, 2–5 L/min |
| 1 | Force probe sensor | MEMS, µN resolution |
| 1 | EM coil injection pair | 1–10 MHz sweep capable, low-power |

---

## 🔊 4. Acoustic & EM Lift Shell

| Qty | Component | Notes |
|-----|-----------|-------|
| 16+ | Ultrasonic transducers (40–100 kHz) | Phase-lockable, e.g., Murata MA40S4S |
| 1 | FPGA or DSP array driver board | Multichannel PWM or delay line synthesis |
| 1 | Infrared distance sensor | e.g., VL53L0X or similar |
| 1 | Paramagnetic fluid (MnCl₂, Gd-based) | 50–100 mL; sealed container |
| 2 | Large flat magnetic coils | EM dome shaping, 10–50 mT field strength |

---

## 🎛 5. Harmonic Control Loop

| Qty | Component | Notes |
|-----|-----------|-------|
| 1 | Stable crystal oscillator | ±5 ppm frequency drift or better |
| 1 | Master timing microcontroller | Should support real-time clock interrupt |
| 1 | Digital phase-locked loop (optional) | For fine-phase correction |
| 1 | Display (optional) | Oscilloscope or spectrum analyzer for field visualization |

---

## ⚡ 6. Power + Safety

| Qty | Component | Notes |
|-----|-----------|-------|
| 1 | Isolated bench power supply | 12–24V, 5–10A total system load |
| 3 | Current-limited DC-DC converters | One per subsystem block |
| 2 | EMI filters | Mains-side + module-level for RF integrity |
| 1 | Grounding and fusing panel | Ground loop suppression, rapid-fuse cutoff |

---

## 🧩 7. Structure + Mounting

| Qty | Component | Notes |
|-----|-----------|-------|
| 1 | Aluminum or carbon frame | Modular extrusion preferred (e.g., 2020 T-slot) |
| 4 | Acrylic or polycarbonate shield panels | For airflow control and visual access |
| 1 | Mounting ring for transducers and toroids | CAD design in `/hardware/CAD_mounting_ring.stl` |
| 1 | Isolation mat for vibration control | Optional but recommended for Casimir system |

---

## 📦 Suggested Vendors

| Vendor | Suitable Items |
|--------|----------------|
| Digikey / Mouser | Coils, sensors, power components |
| McMaster-Carr | Mechanical frame, mounts, isolation |
| SparkFun / Adafruit | Microcontrollers, drivers, sensors |
| Thorlabs | Precision piezo and optical mounting |
| OpenBuilds | Modular frame kits |
| eBay / AliExpress (optional) | Acoustic arrays, graphene substrates, coils (validate specs) |

---

## 🧠 Total System Budget (Estimate)

| Type | Approx. Cost |
|------|---------------|
| Minimum R&D Lab Build | $1,000–$1,500 USD |
| Fully Instrumented Build | $2,500–$4,000 USD |
| Field-Ready Optimized Version | $5,000+ USD (scalable) |

---

## ✅ Summary

This BOM represents a **fully buildable stack**, using **off-the-shelf hardware**, grounded in **verified physics**, designed to explore **real-world gravitational and inertial behavior modulation**.

Each part has been selected for:
- Accessibility
- Reproducibility
- Scientific fidelity

No proprietary gear. No exotic matter.  
Just structured engineering aligned to one outcome: demonstrating what gravity *doesn’t* want us to do — with real tools.

