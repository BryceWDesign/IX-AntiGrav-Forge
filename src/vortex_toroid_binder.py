# vortex_toroid_binder.py  
# Toroidal vortex coherence field binder — IX-AntiGrav-Forge  
# Author: Bryce Wooster 
# License: Open-source, non-military use only

"""
Stabilizes rotating toroidal field structures by locking phase
and amplitude nodes into coherent rotational symmetry using
harmonic reinforcement and phase-latched corrections.

Applications:
- Confinement of rotating harmonic field rings
- Prevention of vortex decoherence under load
- Tesla-based containment of high-frequency pulse loops

Compatible with:
- Multi-layer coil wraps
- Plasma ring cores or hybrid acoustic-EM vortex systems
- Spin-phase locked resonator arrays
"""

import numpy as np

# ------------------------------
# CONFIGURATION
# ------------------------------

FREQ_BASE = 3330
HARMONICS = [1, 2, 3]
PHASE_CORRECTION_GAIN = 0.8
SAMPLE_RATE = 192000
DURATION = 0.02

def generate_base_vortex_wave(freq_base, harmonics, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.zeros_like(t)

    for h in harmonics:
        f = freq_base * h
        signal += np.sin(2 * np.pi * f * t)

    signal /= len(harmonics)
    return t, signal

def apply_phase_binding(signal, phase_gain=PHASE_CORRECTION_GAIN):
    """
    Applies phase-corrective envelope to enforce toroidal symmetry
    """
    length = len(signal)
    envelope = 1 + phase_gain * np.sin(2 * np.pi * np.arange(length) / length)
    return signal * envelope

# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":
    t, base_wave = generate_base_vortex_wave(FREQ_BASE, HARMONICS, DURATION, SAMPLE_RATE)
    bound_wave = apply_phase_binding(base_wave)

    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, bound_wave, label="Toroidal Binder Waveform", color="blue")
    plt.title("Toroid Binder — Phase-Locked Vortex Reinforcement Pattern")
    plt.xlabel("Time (ms)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
