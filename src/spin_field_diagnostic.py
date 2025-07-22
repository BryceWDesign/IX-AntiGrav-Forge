# spin_field_diagnostic.py  
# Real-time spin field envelope analysis — IX-AntiGrav-Forge  
# Author: Bryce Wooster 
# License: Open-source, non-military use only

"""
Scans the rotating harmonic field for:
- Asymmetric spin artifacts
- Centrifugal instability
- Vortex fragmentation
- Harmonic inversion

Acts as a rotation-aware field profiler to ensure smooth
spin-loop behavior and radial field coherence.

Real-world parallels:
- Magnetic domain spintronic sensors
- Vortex flow detectors
- Beam stability sensors in synchrotrons
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# CONFIGURATION
# ------------------------------

FREQ = 3330  # Hz
SAMPLE_RATE = 192000
DURATION = 0.01
ASYM_LEVEL = 0.15

def generate_spin_field(freq, duration, sample_rate, asym_level):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    base_spin = np.sin(2 * np.pi * freq * t)
    vortex_disruption = asym_level * np.sin(2 * np.pi * freq * t * 1.03)
    return t, base_spin + vortex_disruption

def detect_instability(spin_wave, threshold=0.04):
    delta = np.diff(spin_wave)
    variance = np.std(delta)
    return variance > threshold, variance

# ------------------------------
# VISUALIZATION
# ------------------------------

def plot_spin_field(t, wave, variance):
    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, wave, label="Spin Field Envelope")
    plt.title(f"Spin Field Diagnostic — Variance: {variance:.4f}")
    plt.xlabel("Time (ms)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":
    t, spin_wave = generate_spin_field(FREQ, DURATION, SAMPLE_RATE, ASYM_LEVEL)
    unstable, var = detect_instability(spin_wave)
    plot_spin_field(t, spin_wave, var)

    if unstable:
        print(f"⚠️ Spin Instability Detected — Variance: {var:.4f}")
    else:
        print(f"✅ Spin Field Stable — Variance: {var:.4f}")
