import numpy as np
from src.constants import *

def calculate_psi_for_slit(x_detector, center):
    """
    Helper function to calculate the complex amplitude for a single slit 
    by summing over multiple path samples (Path Integral).
    """
    psi = np.zeros(len(x_detector), dtype=complex)
    # Define points within the slit width
    slit_points = np.linspace(center - SLIT_WIDTH/2, center + SLIT_WIDTH/2, SAMPLES_PER_SLIT)
    
    for sp in slit_points:
        # Distance from specific path point to detector
        r = np.sqrt(SCREEN_DISTANCE**2 + (x_detector - sp)**2)
        # Standard Path Integral phase contribution
        psi += np.exp(1j * K * r) / r
    return psi

def simulate_standard():
    """
    Simulates the standard Quantum Double Slit experiment.
    Returns: x_detector (m), intensity (array)
    """
    x_detector = np.linspace(-SCREEN_WIDTH/2, SCREEN_WIDTH/2, NUM_POINTS)
    
    # Calculate amplitudes for both slits
    psi1 = calculate_psi_for_slit(x_detector, SLIT_DISTANCE/2)
    psi2 = calculate_psi_for_slit(x_detector, -SLIT_DISTANCE/2)
    
    # QUANTUM SUPERPOSITION: Add amplitudes before squaring
    intensity = np.abs(psi1 + psi2)**2
    return x_detector, intensity

def simulate_observed():
    """
    Simulates the Double Slit experiment under observation (Wavefunction Collapse).
    Returns: x_detector (m), intensity (array)
    """
    x_detector = np.linspace(-SCREEN_WIDTH/2, SCREEN_WIDTH/2, NUM_POINTS)
    
    # Calculate amplitudes for both slits
    psi1 = calculate_psi_for_slit(x_detector, SLIT_DISTANCE/2)
    psi2 = calculate_psi_for_slit(x_detector, -SLIT_DISTANCE/2)
    
    # OBSERVER EFFECT: Add probabilities (intensities) directly
    # Interference fringes vanish, replaced by two classic humps.
    intensity = np.abs(psi1)**2 + np.abs(psi2)**2
    return x_detector, intensity

def simulate_zigzag_paths(num_mid_points=1000):
    """
    Simulates the Path Integral with an intermediate scattering layer.
    """
    mid_x = SCREEN_DISTANCE / 2
    x_detector = np.linspace(-SCREEN_WIDTH/2, SCREEN_WIDTH/2, 500)
    y_mid = np.linspace(-SCREEN_WIDTH, SCREEN_WIDTH, num_mid_points)
    
    total_psi = np.zeros(len(x_detector), dtype=complex)
    slit_centers = [SLIT_DISTANCE/2, -SLIT_DISTANCE/2]
    
    # Sum over ALL combinations: Slit -> Middle Point -> Detector
    for sc in slit_centers:
        for ym in y_mid:
            # Phase from Slit to Middle Point
            r1 = np.sqrt(mid_x**2 + (ym - sc)**2)
            amp1 = np.exp(1j * K * r1) / np.sqrt(r1)
            
            # Phase from Middle Point to Detector
            r2 = np.sqrt((SCREEN_DISTANCE - mid_x)**2 + (x_detector - ym)**2)
            amp2 = np.exp(1j * K * r2) / np.sqrt(r2)
            
            total_psi += amp1 * amp2

    intensity = np.abs(total_psi)**2
    return x_detector, intensity