# field_harmonic_generator.py
# Tesla-style harmonic waveform generator for IX-AntiGrav-Forge
# Author: Bryce Wooster
# License: Open-source, non-military use only

"""
This module generates phase-aligned harmonic waveforms
based on 3-6-9 resonance logic, suitable for driving:

- EM coil arrays (e.g., spin loop or inertia module)
- Acoustic phased arrays
- Casimir injection coils
- Vacuum cavity field injection

Output can be routed to DACs, PWM drivers, or digital
bus lines using microcontroller platforms (e.g., STM32, RP2040, Teensy).
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# CONFIGURATION PARAMETERS
# ------------------------------

BASE_FREQUENCY_HZ = 3000       # 3 kHz base Tesla harmonic
SAMPLE_RATE_HZ = 96000         # Audio-grade resolution
DURATION_SEC = 0.01            # 10 ms window
HARMONIC_MULTIPLIERS = [1, 2, 3]  # Corresponds to 3k, 6k, 9k

# ------------------------------
# WAVEFORM SYNTHESIS
# ------------------------------

def generate_369_harmonics(f_base, multipliers, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.zeros_like(t)
    
    for n in multipliers:
        harmonic_freq = f_base * n
        signal += np.sin(2 * np.pi * harmonic_freq * t)

    # Normalize
    signal /= len(multipliers)
    return t, signal

# ------------------------------
# MAIN EXECUTION BLOCK
# ------------------------------

if __name__ == "__main__":
    t, waveform = generate_369_harmonics(
        f_base=BASE_FREQUENCY_HZ,
        multipliers=HARMONIC_MULTIPLIERS,
        sample_rate=SAMPLE_RATE_HZ,
        duration=DURATION_SEC
    )

    # Plotting
    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, waveform, label="3-6-9 Harmonic Signal", color='blue')
    plt.title("Tesla Harmonic Field Drive Signal (3-6-9)")
    plt.xlabel("Time (ms)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
