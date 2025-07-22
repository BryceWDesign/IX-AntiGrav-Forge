# vector_force_equalizer.py  
# Directional force balance matrix for rotational field lift — IX-AntiGrav-Forge  
# Author: Bryce Wooster   
# License: Open-source, non-military use only

"""
Equalizes distributed forces across 3D field plane
to prevent drift, spinout, or torque accumulation.

Calculates net vector deviation and counter-injects
correction to maintain stable elevation and directional integrity.

Real-world parallels:
- Thrust vector control (TVC)
- Reaction control systems (RCS)
- Rotor blade pitch alignment in VSTOL aircraft
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# CONFIGURATION
# ------------------------------

SAMPLE_COUNT = 1000
X_FORCE = 1.0
Y_FORCE = 1.2  # imbalance example
Z_FORCE = 0.9

def calculate_vector_balance(x, y, z):
    avg = (x + y + z) / 3.0
    cx = avg - x
    cy = avg - y
    cz = avg - z
    return np.array([cx, cy, cz])

def apply_corrections(forces, corrections):
    return np.array(forces) + corrections

# ------------------------------
# VISUALIZATION
# ------------------------------

def plot_force_equalization(original, corrected):
    labels = ['X', 'Y', 'Z']
    x = np.arange(len(labels))
    
    width = 0.35
    fig, ax = plt.subplots()
    ax.bar(x - width/2, original, width, label='Original')
    ax.bar(x + width/2, corrected, width, label='Corrected', color='orange')
    
    ax.set_ylabel('Force Units')
    ax.set_title('Vector Force Equalization')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    plt.tight_layout()
    plt.show()

# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":
    original_forces = [X_FORCE, Y_FORCE, Z_FORCE]
    corrections = calculate_vector_balance(*original_forces)
    balanced_forces = apply_corrections(original_forces, corrections)
    plot_force_equalization(original_forces, balanced_forces)
