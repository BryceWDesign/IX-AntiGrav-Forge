# plasma_cocoon_modeler.py  
# Simulated plasma sheath formation for inertial drag reduction — IX-AntiGrav-Forge  
# Author: Bryce Wooster 
# License: Open-source, non-military use only

"""
Simulates a toroidal EM cocoon around the emitter core,
serving to:

- Isolate the lift field
- Suppress atmospheric drag
- Redirect inertial wake turbulence
- Aid field shaping at edge-boundary

Real-world analogues:
- Plasma windows (Brookhaven Labs)
- Magneto-aerodynamic shielding
- Ionized drag-reduction sheaths in hypersonics
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# SIMULATION CONFIG
# ------------------------------

RESOLUTION = 400
RADIUS = 0.35
PLASMA_DENSITY = 1.0
EDGE_FADE = 0.08
INTENSITY = 4.0

def generate_cocoon_field():
    x = np.linspace(-1, 1, RESOLUTION)
    y = np.linspace(-1, 1, RESOLUTION)
    X, Y = np.meshgrid(x, y)
    dist = np.sqrt(X**2 + Y**2)

    field = INTENSITY * np.exp(-((dist - RADIUS)**2) / (2 * EDGE_FADE**2))
    return X, Y, field

def plot_cocoon(X, Y, field):
    plt.figure(figsize=(6, 6))
    cocoon = plt.contourf(X, Y, field, levels=80, cmap='plasma')
    plt.title("Plasma Cocoon Field Model")
    plt.xlabel("X (normalized)")
    plt.ylabel("Y (normalized)")
    plt.colorbar(cocoon, label='Relative Plasma Intensity')
    plt.grid(False)
    plt.axis("equal")
    plt.tight_layout()
    plt.show()

# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":
    X, Y, cocoon_field = generate_cocoon_field()
    plot_cocoon(X, Y, cocoon_field)
