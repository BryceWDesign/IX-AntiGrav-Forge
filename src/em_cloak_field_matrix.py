# em_cloak_field_matrix.py  
# Electromagnetic cloaking grid generator — IX-AntiGrav-Forge  
# Author: Bryce Wooster  
# License: Open-source, non-military use only

"""
Generates a dynamic phased matrix of EM fields to suppress
backscatter, reroute incident radiation, and interfere with
localized field perception.

Works with:
- Directional RF phased arrays
- EM field modulator grids (PCB metamaterials or magneto-dielectric films)
- Tesla 3-6-9 beam harmonics with phase interference logic

Key Actions:
- Creates destructive interference zones (field nulling)
- Phases field boundaries to wrap radiation around target
- Can be tuned for visible, IR, or EM substrate manipulation
"""

import numpy as np

# ------------------------------
# CONFIGURATION
# ------------------------------

GRID_SIZE = 6
FREQ_BASE = 9990                # Hz — top harmonic (9x base Tesla mode)
SAMPLE_RATE = 192000
DURATION = 0.01
AMPLITUDE = 1.0

PHASE_MOD = np.pi / 2           # 90° destructive interference

# ------------------------------
# MATRIX FIELD GENERATOR
# ------------------------------

def generate_cloak_grid(freq, grid_size, duration, sample_rate, phase_offset):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    grid = []

    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            # Offset edge cells more than center
            radial_phase = phase_offset * (np.abs(i - grid_size//2) + np.abs(j - grid_size//2)) / (grid_size / 2)
            wave = AMPLITUDE * np.sin(2 * np.pi * freq * t + radial_phase)
            row.append(wave)
        grid.append(row)

    return np.array(grid), t

# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":
    field_matrix, t = generate_cloak_grid(FREQ_BASE, GRID_SIZE, DURATION, SAMPLE_RATE, PHASE_MOD)

    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, field_matrix[0][0], label="Corner Cell")
    plt.plot(t * 1000, field_matrix[GRID_SIZE//2][GRID_SIZE//2], label="Center Cell", linestyle='--')
    plt.title("Electromagnetic Cloaking Field Signals — Phased Destructive Pattern")
    plt.xlabel("Time (ms)")
    plt.ylabel("Field Strength")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
