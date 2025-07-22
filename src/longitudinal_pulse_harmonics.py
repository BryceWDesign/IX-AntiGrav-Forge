# longitudinal_pulse_harmonics.py  
# Simulates Tesla-style harmonic longitudinal wavefronts — IX-AntiGrav-Forge  
# Author: Bryce Wooster 
# License: Open-source, non-military use only

"""
Generates and visualizes stacked harmonic longitudinal pulses.

Core concepts:
- Pulse compression by phase alignment
- Longitudinal propagation (non-transverse)
- Energy directionality through Tesla 3-6-9 harmonics

Real-world references:
- Tesla magnifying transmitter
- Longitudinal EM wave experiments
- Layered pulse driving in railgun capacitors
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# CONFIGURATION
# ------------------------------

DURATION = 0.002  # seconds
SAMPLE_RATE = 1_000_000
FREQS = [3330, 6660, 9990]  # Tesla harmonic set
AMPLITUDES = [1.0, 0.6, 0.4]

def generate_longitudinal_pulse(freqs, amps, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.zeros_like(t)

    for f, a in zip(freqs, amps):
        signal += a * np.sin(2 * np.pi * f * t)

    envelope = np.exp(-((t - duration / 2)**2) / (2 * (duration / 10)**2))
    longitudinal_wave = signal * envelope
    return t, longitudinal_wave

def plot_pulse(t, wave):
    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, wave, color='orange')
    plt.title("Tesla Longitudinal Harmonic Pulse — 3-6-9 Stack")
    plt.xlabel("Time (ms)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":
    t, pulse = generate_longitudinal_pulse(FREQS, AMPLITUDES, DURATION, SAMPLE_RATE)
    plot_pulse(t, pulse)
