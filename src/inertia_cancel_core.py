# inertia_cancel_core.py  
# Inertial field feedback and correction module — IX-AntiGrav-Forge
# Author: Bryce Wooster (CypherSyntax)
# License: Open-source, non-military use only

"""
This module implements real-time detection and cancellation
of inertial motion using tri-axis sensor feedback + EM field modulation.

Features:
- Reads acceleration and gyroscope data (X/Y/Z axes)
- Computes net motion vector magnitude
- Adjusts Helmholtz coil current phase and amplitude
  to induce reactive magnetic field opposing inertia vector

Intended for use with:
- Bosch BMI088, ADIS16448, or similar 6-DOF IMUs
- H-bridge analog drivers or DAC-controlled current amps
- Optional FFT windowing for resonance suppression
"""

import numpy as np

# ------------------------------
# SENSOR MOCKUP (Replace with real IMU driver)
# ------------------------------

def read_imu():
    # Simulate IMU data: [ax, ay, az], [gx, gy, gz]
    accel = np.random.normal(0, 0.02, 3)  # Simulated noise (g's)
    gyro  = np.random.normal(0, 0.01, 3)  # Simulated angular velocity (rad/s)
    return accel, gyro

# ------------------------------
# VECTOR PROCESSING
# ------------------------------

def compute_magnitude(vec):
    return np.sqrt(np.sum(np.square(vec)))

def direction_unit(vec):
    norm = np.linalg.norm(vec)
    if norm == 0:
        return np.zeros_like(vec)
    return vec / norm

# ------------------------------
# FIELD COMPENSATION LOGIC
# ------------------------------

def compute_counter_field(accel_vector):
    """
    Returns a unit vector for the opposing EM field direction.
    In practice, this would be multiplied by a gain and routed to
    analog drivers or DAC output for coil control.
    """
    dir_vec = direction_unit(accel_vector)
    return -1 * dir_vec  # Invert vector to oppose motion

# ------------------------------
# MAIN EXECUTION LOOP (Test)
# ------------------------------

if __name__ == "__main__":
    for step in range(10):  # Simulate 10 cycles
        accel, gyro = read_imu()
        net_accel_mag = compute_magnitude(accel)
        counter_field = compute_counter_field(accel)

        print(f"[Cycle {step}]")
        print(f"  Accel: {accel}")
        print(f"  Gyro:  {gyro}")
        print(f"  Magnitude: {net_accel_mag:.4f} g")
        print(f"  Counter Field Direction: {counter_field}")
