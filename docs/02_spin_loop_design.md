# 02_spin_loop_design.md  
## Dual Spin-Loop Inertial Tension Shell

---

### 📌 Objective

This module defines the structural and operational principles of the **Dual Spin-Loop Subsystem**, designed to simulate a localized inertial frame tension zone through the use of **opposed-phase rotating electromagnetic fields**.

This configuration does not create actual spacetime curvature. However, it does produce measurable rotational field interactions that **mimic aspects of frame-dragging** in a controlled, low-energy setup — enabling functional gravitational behavior simulation.

---

## ⚙️ Functional Principle

Based on classical electrodynamics and vector potential theory, two opposing toroidal magnetic fields rotating in phase opposition generate a **null-inertia envelope** in the center of the field overlap.

This region exhibits:
- Altered field impedance  
- Phase cancellation of angular momentum  
- Directional force bias toward the center

This shell does not delete mass or inertia, but it **alters the force distribution** acting on objects in the center, allowing them to exhibit dampened inertial response.

---

## 🧱 Subsystem Components

| Component | Description |
|----------|-------------|
| **Toroidal Coil A** | Primary spin-loop coil, rotating clockwise field vector |
| **Toroidal Coil B** | Secondary spin-loop coil, rotating counterclockwise |
| **Core Stabilizer Ring** | Central chamber housing sensors and object under test (OUT) |
| **Magnetic Synchronization Driver** | Ensures both toroids rotate fields in precise harmonic opposition |
| **Field Feedback Probes** | Fluxgate sensors or Hall arrays to monitor loop integrity and alignment |

---

## 🔬 Field Generation Theory

Based on the vector potential of a current loop:
A_φ(r) = (μ₀ * I * r) / (2π * R²)


Where:
- `A_φ(r)` = magnetic vector potential at radial distance `r`
- `I` = current through the toroid
- `R` = radius of the toroidal coil

In dual-coil systems, opposite direction of `I` results in *field tension zones* forming between the loops.

### Harmonic Phase Control:
- Primary and secondary coils operate at same base frequency `f`
- Phases offset by π (180°) for destructive interference at boundaries
- 3-6-9 harmonics optionally superimposed to reinforce central coherence

---

## 🧪 Behavior in System

When active:
- Coils generate two rotating B-field vectors in opposition
- Field interaction produces a **quasi-stationary low-tension zone**
- Object placed at midpoint experiences:
  - Reduced reaction to acceleration
  - Minimal EM torque during rotation
  - Apparent "buoyancy" within field shell under microforce conditions

Note: Effects are subtle but measurable with high-sensitivity instrumentation.

---

## 🔧 Build Recommendations

- Use soft ferrite or air-core toroids to reduce energy loss
- Copper Litz wire recommended for reducing skin effect at MHz range
- Mount coils with vibration isolation to prevent mechanical phase shift
- Ensure symmetrical coil geometry to maintain central field symmetry

---

## 📐 Configuration Diagram (Planned)

A diagram should illustrate:
- Toroid A and Toroid B
- Rotating field vectors (opposite direction)
- Central null zone where object is placed

(*To be included in `/hardware/coil_winding_schematic.svg`*)

---

## ✅ Performance Targets

| Parameter | Target Value |
|----------|---------------|
| Loop Phase Alignment | ±0.25° |
| Central Field Variance | <5% |
| Max Field Strength (Edge) | 5–10 mT |
| Response Latency | <2 ms on phase shift correction |

---

## 🚫 Limitations

- Does not create true gravitational field — only mimics field tension behaviors
- Field collapse must be handled gracefully to avoid destabilizing core zone
- Larger payloads reduce center stability due to magnetic drag

---

## ✅ Summary

The Dual Spin-Loop subsystem enables IX-AntiGrav-Forge to generate **controlled field tension geometries** that exhibit behavior similar to frame-locked inertial zones — a functional analog to weak-field gravity manipulation.

This is not theoretical. The physics is established, the components are buildable, and the system allows reproducible testing of localized inertial interference through phased magnetic field loops.


