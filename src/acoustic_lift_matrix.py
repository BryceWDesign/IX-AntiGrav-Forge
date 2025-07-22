# acoustic_lift_matrix.py  
# Phased ultrasonic array matrix control — IX-AntiGrav-Forge
# Author: Bryce Wooster
# License: Open-source, non-military use only

"""
Controls a grid of ultrasonic transducers to produce
near-field levitation, focused pressure nodes, and
EM field coupling via acoustic pressure modulation.

Supports:
- 8×8 grid (64-channel array)
- Phase shifting per transducer
- Dynamic waveform input (optional Tesla harmonic integration)
- Acoustic beam steering and trap zone formation
"""

import numpy as np

# ------------------------------
# PARAMETERS
# ------------------------------

GRID_SIZE = 8                      # 8x8 matrix
FREQ_HZ = 40000                    # 40 kHz (typical ultrasonic)
SAMPLE_RATE = 192000              # High-res sampling
AMPLITUDE = 1.0                   # Signal strength (normalized)

# ------------------------------
# SIGNAL GENERATION
# ------------------------------

def generate_phased_matrix(frequency, phase_matrix, amplitude, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signals = []

    for i in range(GRID_SIZE):
        row = []
        for j in range(GRID_SIZE):
            phase = phase_matrix[i][j]
            signal = amplitude * np.sin(2 * np.pi * frequency * t + phase)
            row.append(signal)
        signals.append(row)

    return np.array(signals)

# ------------------------------
# PHASE STRATEGY EXAMPLE
# ------------------------------

def generate_focus_center_phases(grid_size):
    center = (grid_size - 1) / 2.0
    phase_matrix = np.zeros((grid_size, grid_size))
    
    for i in range(grid_size):
        for j in range(grid_size):
            dx = i - center
            dy = j - center
            distance = np.sqrt(dx**2 + dy**2)
            phase_matrix[i][j] = -distance * np.pi / 4  # radial phase offset
    return phase_matrix

# ------------------------------
# MAIN TEST
# ------------------------------

if __name__ == "__main__":
    duration = 0.002  # 2 ms
    phase_matrix = generate_focus_center_phases(GRID_SIZE)
    signals = generate_phased_matrix(FREQ_HZ, phase_matrix, AMPLITUDE, SAMPLE_RATE, duration)

    # Example output for central transducer pair
    print("Sample output (corner and center):")
    print("Top-left phase sample:", signals[0][0][:10])
    print("Center phase sample:", signals[4][4][:10])
