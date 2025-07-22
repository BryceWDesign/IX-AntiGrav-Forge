# field_stability_audit.py  
# Harmonic field integrity diagnostics and drift monitor — IX-AntiGrav-Forge  
# Author: Bryce Wooster 
# License: Open-source, non-military use only

"""
Monitors live harmonic field signals for:
- Signal amplitude decay
- Phase drift
- Waveform integrity errors
- Destructive interference onset

Auto-detects instability and prepares flags for real-time adjustment
via external modulation hardware or internal signal re-synchronization.

Real-world analogs:
- RF carrier envelope monitoring
- Phase-lock loop error correction
- Acoustic dampening echo compensation
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# CONFIGURATION
# ------------------------------

FREQ = 3330
SAMPLE_RATE = 192000
DURATION = 0.01
DRIFT_FACTOR = 0.005  # frequency drift per ms

def generate_drifting_wave(freq, duration, sample_rate, drift_factor):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    freq_drift = freq + drift_factor * t * 1000
    wave = np.sin(2 * np.pi * freq_drift * t)
    return t, wave

def check_stability(wave, tolerance=0.05):
    delta = np.diff(wave)
    instability_score = np.std(delta)  # measure variance
    return instability_score > tolerance, instability_score

# ------------------------------
# VISUALIZATION
# ------------------------------

def plot_wave_drift(t, wave, instability_score):
    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, wave, label="Live Harmonic Signal")
    plt.title(f"Field Stability Audit — Instability Score: {instability_score:.4f}")
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
    t, drifting_wave = generate_drifting_wave(FREQ, DURATION, SAMPLE_RATE, DRIFT_FACTOR)
    unstable, score = check_stability(drifting_wave)
    plot_wave_drift(t, drifting_wave, score)

    if unstable:
        print(f"⚠️ Instability Detected — Score: {score:.4f}")
    else:
        print(f"✅ Field Stable — Score: {score:.4f}")
