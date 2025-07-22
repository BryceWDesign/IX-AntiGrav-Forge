# tesla_loop_modulator.py  
# Tesla 3-6-9 waveform reinforcement + modulator — IX-AntiGrav-Forge  
# Author: Bryce Wooster   
# License: Open-source, non-military use only

"""
Modulates and reinforces a waveform loop with Tesla-based
harmonic logic. Dynamically injects amplitude and phase shifts
based on 3-6-9 patterning, enabling entrainment of EM field systems.

Applications:
- Tesla coil pulse timing modulation
- EM cavity phase locking
- Acoustic harmonic feedback reinforcement
"""

import numpy as np

# ------------------------------
# CONFIGURATION
# ------------------------------

BASE_FREQ = 3330  # Hz
DURATION = 0.015   # 15ms loop
SAMPLE_RATE = 192000
HARMONIC_WEIGHTS = [1.0, 0.7, 0.5]  # For 3x, 6x, 9x modulation

def generate_369_loop(freq, weights, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.zeros_like(t)

    for idx, mult in enumerate([1, 2, 3]):
        harmonic_freq = freq * mult
        signal += weights[idx] * np.sin(2 * np.pi * harmonic_freq * t)

    signal /= sum(weights)
    return t, signal

def reinforce_signal(signal, gain=0.2):
    """
    Applies reinforcement loop to simulate energy return
    from feedback path (e.g. acoustic or EM phase echo)
    """
    feedback = np.roll(signal, len(signal) // 6) * gain
    return signal + feedback

# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":
    t, base_wave = generate_369_loop(BASE_FREQ, HARMONIC_WEIGHTS, DURATION, SAMPLE_RATE)
    modulated_wave = reinforce_signal(base_wave)

    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, modulated_wave, label="Reinforced Tesla 3-6-9 Loop", color="red")
    plt.title("Tesla Harmonic Loop Modulator — 3-6-9 Phase Reinforcement")
    plt.xlabel("Time (ms)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
