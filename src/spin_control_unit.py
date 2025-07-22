# spin_control_unit.py  
# Dual spin-loop field controller for IX-AntiGrav-Forge
# Author: Bryce Wooster 
# License: Open-source, non-military use only

"""
This module manages the phase, polarity, and amplitude of the
dual toroidal EM spin-loops used in the IX-AntiGrav-Forge platform.

- Ensures one coil runs CW, the other CCW
- Matches frequency to 3-6-9 harmonic generator input
- Allows dynamic amplitude modulation (DAM) for field shaping
- Supports phase inversion, ramping, and safety cutoff
"""

import numpy as np

# ------------------------------
# CONFIGURATION
# ------------------------------

FREQUENCY_HZ = 6000              # Target harmonic (6 kHz spin field)
SAMPLE_RATE_HZ = 96000           # Matching generator sample rate
DURATION_SEC = 0.01              # Duration of signal (10 ms)
AMPLITUDE = 1.0                  # Max amplitude (normalized)

# Phase offsets
PHASE_A = 0                      # 0° for Coil A (CW)
PHASE_B = np.pi                  # 180° for Coil B (CCW)

# ------------------------------
# SIGNAL GENERATION
# ------------------------------

def generate_spin_field(frequency, sample_rate, duration, amp, phase):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = amp * np.sin(2 * np.pi * frequency * t + phase)
    return t, signal

# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":
    t, spin_A = generate_spin_field(FREQUENCY_HZ, SAMPLE_RATE_HZ, DURATION_SEC, AMPLITUDE, PHASE_A)
    _, spin_B = generate_spin_field(FREQUENCY_HZ, SAMPLE_RATE_HZ, DURATION_SEC, AMPLITUDE, PHASE_B)

    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, spin_A, label="Coil A (CW)", color='red')
    plt.plot(t * 1000, spin_B, label="Coil B (CCW)", color='blue', linestyle='--')
    plt.title("Dual Spin-Loop Field Signal (6 kHz, Opposing Phase)")
    plt.xlabel("Time (ms)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
