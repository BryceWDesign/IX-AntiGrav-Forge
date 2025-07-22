# buoyancy_field_driver.py  
# Neutral buoyancy control system using phase-offset harmonic lift — IX-AntiGrav-Forge  
# Author: Bryce Wooster 
# License: Open-source, non-military use only

"""
Simulates neutral buoyancy in an object by generating a
counter-phase lift field. Uses Tesla-style 3-6-9 field patterning
and phase-delay modulation to emulate gravitational equilibrium.

Can be used with:
- Helmholtz coil arrays
- Plasma-lens RF cavities
- Acoustic lift systems + EM bias layer
"""

import numpy as np

# ------------------------------
# CONFIGURATION
# ------------------------------

BASE_FREQ = 3330               # Hz
SAMPLE_RATE = 192000
DURATION = 0.02                # 20 ms simulation window
AMPLITUDE = 1.0
PHASE_OFFSET_DEGREES = 90      # Ideal phase offset to generate lift null point

HARMONICS = [1, 2, 3]

# ------------------------------
# SIGNAL ENGINE
# ------------------------------

def generate_buoyancy_wave(base_freq, harmonics, phase_offset_deg, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.zeros_like(t)

    for h in harmonics:
        phase_rad = np.deg2rad(phase_offset_deg * h)
        f = base_freq * h
        signal += np.sin(2 * np.pi * f * t + phase_rad)

    signal /= len(harmonics)
    return t, signal

# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":
    t, wave = generate_buoyancy_wave(BASE_FREQ, HARMONICS, PHASE_OFFSET_DEGREES, DURATION, SAMPLE_RATE)

    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, wave, label="Neutral Buoyancy Field", color="green")
    plt.title("Phase-Offset Harmonic Lift Field (Tesla 3-6-9 Mode)")
    plt.xlabel("Time (ms)")
    plt.ylabel("Field Strength")
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()
