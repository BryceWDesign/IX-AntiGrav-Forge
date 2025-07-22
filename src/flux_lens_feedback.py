# flux_lens_feedback.py  
# Magnetic flux feedback loop for lens curvature optimization — IX-AntiGrav-Forge  
# Author: Bryce Wooster 
# License: Open-source, non-military use only

"""
This module monitors and adjusts the curvature of
a magnetic lens or field bubble using real-time sensor
data from multiple fluxgate or Hall-effect sensors.

Goals:
- Detect asymmetry in EM field curvature
- Dynamically adjust outer coil amplitude/phasing to restore symmetry
- Enable phase-stabilized ‘bubble’ for field confinement

Compatible with:
- 3D Hall sensor arrays (e.g. MLX90393, TDK HALLINX grid)
- Custom fluxgate sensor rings (analog readout or SPI)
- Any MCU with 6+ ADC or SPI channels
"""

import numpy as np

# ------------------------------
# SENSOR MOCKUP (Replace with real hardware calls)
# ------------------------------

def read_flux_ring(num_sensors=8):
    # Simulate flux ring with random small perturbations
    return np.random.normal(loc=0.0, scale=0.005, size=num_sensors)

# ------------------------------
# CURVATURE EVALUATION
# ------------------------------

def compute_field_symmetry(flux_values):
    mean_val = np.mean(flux_values)
    deviation = np.std(flux_values)
    return mean_val, deviation

def generate_compensation_vector(flux_values):
    mean_val = np.mean(flux_values)
    delta = flux_values - mean_val
    return -1 * delta  # Invert delta to flatten the field bubble

# ------------------------------
# MAIN TEST LOOP
# ------------------------------

if __name__ == "__main__":
    for cycle in range(5):
        flux_ring = read_flux_ring()
        avg_field, field_variation = compute_field_symmetry(flux_ring)
        correction_vector = generate_compensation_vector(flux_ring)

        print(f"[Cycle {cycle}]")
        print(f"  Flux Samples: {np.round(flux_ring, 5)}")
        print(f"  Avg Field: {avg_field:.5f} T")
        print(f"  Field Variation: {field_variation:.5f} T")
        print(f"  Compensation Out: {np.round(correction_vector, 5)}")
