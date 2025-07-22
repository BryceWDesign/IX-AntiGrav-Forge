# dynamic_lift_feedback.py  
# Closed-loop controller for real-time lift modulation — IX-AntiGrav-Forge  
# Author: Bryce Wooster 
# License: Open-source, non-military use only

"""
Live monitors lift output, compares against equilibrium
setpoint, and adjusts field gain accordingly.

Prevents overshoot, wobble, drift, or oscillation collapse.

Real-world analogs:
- PID controller (drones, rockets)
- Magnetic suspension feedback loop
- Tesla reactive tuning circuit
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# CONFIGURATION
# ------------------------------

DURATION = 1.5
SAMPLE_RATE = 1000
SETPOINT = 1.0  # Ideal lift amplitude
GAIN_P = 2.0
GAIN_D = 1.2
GAIN_I = 0.5

def simulate_lift_feedback():
    t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION))
    output = np.zeros_like(t)
    error_sum = 0
    prev_error = 0

    for i in range(1, len(t)):
        measured = output[i-1] + 0.02 * np.random.randn()  # simulate sensor noise
        error = SETPOINT - measured
        error_sum += error
        d_error = error - prev_error

        control = GAIN_P * error + GAIN_I * error_sum + GAIN_D * d_error
        output[i] = output[i-1] + 0.01 * control
        prev_error = error

    return t, output

def plot_feedback_response(t, output):
    plt.figure(figsize=(10, 4))
    plt.plot(t, output, label="Lift Field Output")
    plt.axhline(y=SETPOINT, color='red', linestyle='--', label='Setpoint')
    plt.title("Dynamic Lift Feedback Response")
    plt.xlabel("Time (s)")
    plt.ylabel("Field Amplitude")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":
    t, response = simulate_lift_feedback()
    plot_feedback_response(t, response)
