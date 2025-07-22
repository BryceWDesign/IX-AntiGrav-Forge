# em_inertia_map_model.py  
# Directional inertia redistribution map under EM exposure — IX-AntiGrav-Forge  
# Author: Bryce Wooster 
# License: Open-source, non-military use only

"""
Simulates how dynamic EM field geometries influence:
- Local inertial vector magnitude
- Directional redirection of momentum
- Pseudo-mass displacement in rotating plasma zones

Real-world analogs:
- EM inertial decoupling from Lockheed/Ames patents
- Magneto-Archimedes inertia suppression (in diamagnetic levitation)
- Lorentz-force-induced mass dampening
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# CONFIGURATION
# ------------------------------

GRID_SIZE = 100
CENTER = (0.5, 0.5)
FIELD_STRENGTH = 1.0
DECAY_RADIUS = 0.4
DISTORTION_FACTOR = 1.8

def generate_inertia_field():
    x = np.linspace(0, 1, GRID_SIZE)
    y = np.linspace(0, 1, GRID_SIZE)
    X, Y = np.meshgrid(x, y)

    dx = X - CENTER[0]
    dy = Y - CENTER[1]
    r = np.sqrt(dx**2 + dy**2)

    field_mag = FIELD_STRENGTH * np.exp(-r / DECAY_RADIUS)
    theta = np.arctan2(dy, dx)

    U = field_mag * np.cos(theta + DISTORTION_FACTOR * r)
    V = field_mag * np.sin(theta + DISTORTION_FACTOR * r)

    return X, Y, U, V

def plot_inertia_map(X, Y, U, V):
    plt.figure(figsize=(6, 6))
    plt.streamplot(X, Y, U, V, color=np.sqrt(U**2 + V**2), cmap='magma', density=1.2)
    plt.title("EM-Induced Inertial Flow Field")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(False)
    plt.axis("equal")
    plt.colorbar(label="Inertial Vector Magnitude")
    plt.tight_layout()
    plt.show()

# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":
    X, Y, U, V = generate_inertia_field()
    plot_inertia_map(X, Y, U, V)
