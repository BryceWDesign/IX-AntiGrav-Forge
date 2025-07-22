# inertial_dampening_matrix.py  
# Phase-interference inertial suppression matrix — IX-AntiGrav-Forge  
# Author: Bryce Wooster   
# License: Open-source, non-military use only

"""
Generates a phase-coherent pulse matrix designed to cancel
inertial reaction forces via destructive interference.

Does NOT "remove mass" — instead, it suppresses
reaction acceleration using harmonic nulling.

Inspired by:
- EM inertia modulation via Tesla coil rebound effect
- Dual-phase sound field cancellation
- Superconductive lattice echo suppression (Casimir overlap logic)
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# CONFIGURATION
# ------------------------------

GRID_SIZE = 8
FREQ_BASE = 3330
SAMPLE_RATE = 192000
DURATION = 0.015
PHASE_NULL = np.pi  # 180° cancellation

# ------------------------------
# MATRIX GENERATION
# ------------------------------

def generate_dampening_matrix(grid_size, freq, duration, sample_rate, phase_shift):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    matrix = []

    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            phase = phase_shift * ((i + j) % 2)  # alternating cancel fields
            wave = np.sin(2 * np.pi * freq * t + phase)
            row.append(wave)
        matrix.append(row)

    return np.array(matrix), t

# ------------------------------
# VISUALIZATION
# ------------------------------

def plot_matrix_slice(matrix, t):
    center_wave = matrix[GRID_SIZE//2][GRID_SIZE//2]
    edge_wave = matrix[0][0]

    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, center_wave, label="Center Pulse")
    plt.plot(t * 1000, edge_wave, label="Edge Pulse", linestyle='--')
    plt.title("Inertial Dampening Pulse — Phase Cancel Matrix")
    plt.xlabel("Time (ms)")
    plt.ylabel("Field Strength")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":
    field_matrix, t = generate_dampening_matrix(GRID_SIZE, FREQ_BASE, DURATION, SAMPLE_RATE, PHASE_NULL)
    plot_matrix_slice(field_matrix, t)
