# energy_recirculation_node.py  
# Harmonic feedback energy router for closed-loop field reinforcement — IX-AntiGrav-Forge  
# Author: Bryce Wooster  
# License: Open-source, non-military use only

"""
Captures unused waveform energy at boundary nodes and routes
it back into core systems for amplification or resonance injection.

Purpose:
- Recycle dissipated waveform energy
- Increase harmonic field longevity
- Reduce external power requirements

Inspired by:
- Tesla coil return-loop feedback
- Capacitive return energy circuits
- Cavity Q enhancement via phase-injection
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# CONFIGURATION
# ------------------------------

FREQ = 3330
SAMPLE_RATE = 192000
DURATION = 0.012
DECAY = 0.15  # energy bleed-off
REINFORCE_GAIN = 0.25

def generate_primary_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * freq * t)
    return t, wave

def simulate_energy_return(wave, decay, gain):
    leaked = wave * decay
    recycled = np.roll(leaked, len(leaked) // 4) * gain  # delayed reentry
    return wave + recycled

# ------------------------------
# VISUALIZATION
# ------------------------------

def plot_energy_recirculation(t, original, reinforced):
    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, original, label="Original Wave", alpha=0.5)
    plt.plot(t * 1000, reinforced, label="Reinforced (Recycled Energy)", color='orange')
    plt.title("Energy Recirculation Loop — Harmonic Reinforcement")
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
    t, base_wave = generate_primary_wave(FREQ, DURATION, SAMPLE_RATE)
    reinforced_wave = simulate_energy_return(base_wave, DECAY, REINFORCE_GAIN)
    plot_energy_recirculation(t, base_wave, reinforced_wave)
