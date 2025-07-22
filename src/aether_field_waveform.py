# aether_field_waveform.py  
# Models distortion of surrounding density field from harmonic pulses — IX-AntiGrav-Forge  
# Author: Bryce Wooster   
# License: Open-source, non-military use only

"""
Simulates dynamic modulation of the surrounding 'aetheric' medium
from Tesla-style longitudinal pulses.

Visualizes the resulting pressure bands and impedance gradient flow
which may lead to localized pseudo-buoyancy or inertia redirection.

References:
- Tesla radiant energy capture field effects
- Vacuum impedance modulation theory (NASA TR-R-479)
- Gradient impedance interaction (Casimir-like field response)
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# CONFIGURATION
# ------------------------------

GRID_RES = 200
CENTER = (0.5, 0.5)
FREQ = 3690
AMPLITUDE = 1.0
DURATION = 0.002
SAMPLE_RATE = 1_000_000

def generate_aetheric_wave():
    x = np.linspace(0, 1, GRID_RES)
    y = np.linspace(0, 1, GRID_RES)
    X, Y = np.meshgrid(x, y)

    dx = X - CENTER[0]
    dy = Y - CENTER[1]
    r = np.sqrt(dx**2 + dy**2) + 1e-6  # avoid div by zero

    pulse = AMPLITUDE * np.sin(2 * np.pi * FREQ * r) * np.exp(-20 * r)
    field_mod = np.gradient(pulse)

    return X, Y, pulse, field_mod

def plot_aether_wave(X, Y, pulse, grad):
    plt.figure(figsize=(7, 6))
    plt.contourf(X, Y, pulse, 120, cmap='viridis')
    plt.quiver(X[::8, ::8], Y[::8, ::8], grad[1][::8, ::8], grad[0][::8, ::8], color='white', scale=100, width=0.003)
    plt.title("Aetheric Field Pressure Waveform from Tesla Pulse")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()

# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":
    X, Y, pulse, grad = generate_aetheric_wave()
    plot_aether_wave(X, Y, pulse, grad)
