# harmonic_field_lithography.py  
# Beam harmonics for surface resonance imprinting — IX-AntiGrav-Forge  
# Author: Bryce Wooster
# License: Open-source, non-military use only

"""
Generates Tesla 3-6-9 harmonic pulses modulated into a spatial
beam pattern, used to imprint harmonic fields into physical materials.

Application:
- Resonant charging of non-metallic surfaces
- EM field lithography at macro scale
- Beam-driven harmonic structuring of lenses, plates, or EM-transparent films

Compatible With:
- RF beamformers, Tesla coils, laser modulated discharge tips
- Audio-to-voltage converters for acoustic imprinting
- Surface coupling plates (ceramic, oxide, glass, or resonant polymer)
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# CONFIGURATION
# ------------------------------

BASE_FREQ = 3330              # Hz — prime harmonic
HARMONICS = [1, 2, 3]         # 3.33kHz, 6.66kHz, 9.99kHz
DURATION = 0.01               # 10ms
SAMPLE_RATE = 192000
AMPLITUDE = 1.0

def generate_harmonic_pattern(base, harmonics, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    beam = np.zeros_like(t)

    for h in harmonics:
        f = base * h
        beam += np.sin(2 * np.pi * f * t)

    beam /= len(harmonics)
    return t, beam

# ------------------------------
# BEAMFORMING PROFILE (MODULATE)
# ------------------------------

def apply_surface_modulation(signal, spatial_factor=0.4):
    """
    Applies simulated decay or spread across a surface
    to emulate radial lithography absorption
    """
    mod_curve = np.linspace(1, spatial_factor, len(signal))
    return signal * mod_curve

# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":
    t, base_beam = generate_harmonic_pattern(BASE_FREQ, HARMONICS, DURATION, SAMPLE_RATE)
    modulated_beam = apply_surface_modulation(base_beam)

    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, modulated_beam, label="Lithographic Field Pulse", color="purple")
    plt.title("Harmonic Lithography Pattern — Tesla 3-6-9 Beam Imprint")
    plt.xlabel("Time (ms)")
    plt.ylabel("Field Strength")
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()
