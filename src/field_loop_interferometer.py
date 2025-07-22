# field_loop_interferometer.py  
# Harmonic phase-loop interferometer — IX-AntiGrav-Forge  
# Author: Bryce Wooster 
# License: Open-source, non-military use only

"""
Detects micro-changes in field coherence by passing harmonic
loops through physical or field-based paths and analyzing
phase distortion upon recombination.

Principle: Phase-loop interferometry (Michelson-style logic)

Used for:
- Scanning for harmonic field warping
- Real-time detection of space curvature or density echo
- Field lens calibration feedback

Compatible with:
- EM beam loops
- Acoustic phased loops
- Harmonic lithography alignment correction
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# CONFIGURATION
# ------------------------------

BASE_FREQ = 3330
DELAY_DIFF = 0.000002  # 2 µs path difference
DURATION = 0.005
SAMPLE_RATE = 192000

def generate_loop_wave(freq, delay_offset, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    ref_wave = np.sin(2 * np.pi * freq * t)
    test_wave = np.sin(2 * np.pi * freq * (t + delay_offset))
    return t, ref_wave, test_wave

def analyze_interference(ref, test):
    return ref + test  # superposition (interference output)

# ------------------------------
# VISUALIZATION
# ------------------------------

def plot_interference(t, ref, test, output):
    plt.figure(figsize=(10, 5))
    plt.plot(t * 1000, ref, label="Reference Path", alpha=0.5)
    plt.plot(t * 1000, test, label="Test Path", alpha=0.5)
    plt.plot(t * 1000, output, label="Interference Output", color="red")
    plt.title("Harmonic Field Loop Interferometer")
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
    t, ref, test = generate_loop_wave(BASE_FREQ, DELAY_DIFF, DURATION, SAMPLE_RATE)
    interference = analyze_interference(ref, test)
    plot_interference(t, ref, test, interference)
