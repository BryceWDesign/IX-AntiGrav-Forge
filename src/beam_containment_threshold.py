# beam_containment_threshold.py  
# Defines safe field strength & failure points — IX-AntiGrav-Forge  
# Author: Bryce Wooster 
# License: Open-source, non-military use only

"""
Calculates the critical containment threshold for Tesla-harmonic beams
based on real-time amplitude, node coherence, and vector field stability.

This module ensures:
- The beam doesn't self-destruct
- Critical feedback is avoided
- Harmonic nodes stay phase-locked

References:
- Fusion tokamak quench thresholds
- Harmonic field overload patterns (CERN beam dump studies)
- Tesla coil resonance node breakup modeling
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# CONFIGURATION
# ------------------------------

FREQ = 3690
NODE_COUNT = 3
MAX_FIELD_AMPLITUDE = 1.25  # arbitrary units
NODE_VARIANCE_LIMIT = 0.12
COHERENCE_THRESHOLD = 0.85

def calculate_stability(amplitudes, phase_diff, coherence):
    amp_max = np.max(np.abs(amplitudes))
    amp_fail = amp_max > MAX_FIELD_AMPLITUDE
    var_fail = np.std(amplitudes) > NODE_VARIANCE_LIMIT
    phase_fail = np.max(np.abs(phase_diff)) > 0.6 * np.pi
    coherence_fail = coherence < COHERENCE_THRESHOLD

    return amp_fail or var_fail or phase_fail or coherence_fail

def simulate_test_case():
    # Hypothetical values pulled from live field telemetry
    amplitudes = np.array([1.1, 1.15, 1.17])  # Amplitude of each node
    phase_diff = np.array([0.1*np.pi, 0.2*np.pi, 0.4*np.pi])  # Relative phases
    coherence = 0.81

    failure = calculate_stability(amplitudes, phase_diff, coherence)

    if failure:
        print("❌ Beam containment threshold EXCEEDED. Shutdown recommended.")
    else:
        print("✅ Beam stable and within safe operating parameters.")

# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":
    simulate_test_case()
