# frequency_gatekeeper.py  
# Harmonic frequency validation and interference blocker — IX-AntiGrav-Forge  
# Author: Bryce Wooster 
# License: Open-source, non-military use only

"""
Ensures only valid Tesla-structured harmonics enter
the central field logic system. Protects against:

- Signal contamination
- External noise injection
- Harmonic misalignment

Acts like a frequency firewall.

Analogous real-world systems:
- Bandpass filter (RF and audio)
- EMI shielding protocols
- Tesla selective resonance tuning
"""

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# ------------------------------
# CONFIGURATION
# ------------------------------

TARGET_FREQ = 3330  # Hz
BANDWIDTH = 60  # Hz around the target
SAMPLE_RATE = 192000
DURATION = 0.01

def generate_mixed_signal():
    t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)
    wave_clean = np.sin(2 * np.pi * TARGET_FREQ * t)
    wave_noise = 0.4 * np.sin(2 * np.pi * 3600 * t)  # interference
    wave_noise += 0.3 * np.sin(2 * np.pi * 3150 * t)  # interference
    return t, wave_clean + wave_noise

def bandpass_filter(signal_in, target_freq, bandwidth, sample_rate):
    nyq = 0.5 * sample_rate
    low = (target_freq - bandwidth) / nyq
    high = (target_freq + bandwidth) / nyq
    b, a = signal.butter(4, [low, high], btype='band')
    return signal.filtfilt(b, a, signal_in)

# ------------------------------
# VISUALIZATION
# ------------------------------

def plot_filter_response(t, original, filtered):
    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, original, label="Incoming Signal (With Noise)", alpha=0.5)
    plt.plot(t * 1000, filtered, label="Filtered Signal", color='green')
    plt.title("Frequency Gatekeeper — Bandpass Filter Response")
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
    t, mixed_signal = generate_mixed_signal()
    filtered_signal = bandpass_filter(mixed_signal, TARGET_FREQ, BANDWIDTH, SAMPLE_RATE)
    plot_filter_response(t, mixed_signal, filtered_signal)
