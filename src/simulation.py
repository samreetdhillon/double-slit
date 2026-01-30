import numpy as np
from src.constants import *

def calculate_psi_for_slit(x_detector, center, D_val, K_val, samples_val):    
    # Helper function to calculate the complex amplitude for a single slit.
    psi = np.zeros(len(x_detector), dtype=complex)
    slit_points = np.linspace(center - SLIT_WIDTH/2, center + SLIT_WIDTH/2, int(samples_val))
    
    for sp in slit_points:
        # Distance from specific path point to detector using custom D
        r = np.sqrt(D_val**2 + (x_detector - sp)**2)
        # Standard Path Integral phase contribution
        psi += np.exp(1j * K_val * r) / r
    return psi

def simulate_standard_custom(a, D):
    x_detector = np.linspace(-SCREEN_WIDTH/2, SCREEN_WIDTH/2, NUM_POINTS)
    psi1 = calculate_psi_for_slit(x_detector, a/2, D, K, SAMPLES_PER_SLIT)
    psi2 = calculate_psi_for_slit(x_detector, -a/2, D, K, SAMPLES_PER_SLIT)
    intensity = np.abs(psi1 + psi2)**2
    return x_detector, intensity

def simulate_observed_custom(a, D):
    x_detector = np.linspace(-SCREEN_WIDTH/2, SCREEN_WIDTH/2, NUM_POINTS)
    psi1 = calculate_psi_for_slit(x_detector, a/2, D, K, SAMPLES_PER_SLIT)
    psi2 = calculate_psi_for_slit(x_detector, -a/2, D, K, SAMPLES_PER_SLIT)
    # Observer effect: Sum intensities, not amplitudes
    intensity = np.abs(psi1)**2 + np.abs(psi2)**2
    return x_detector, intensity

def simulate_zigzag_custom(a, D, num_mid_points=1000):
    mid_x = D / 2
    x_detector = np.linspace(-SCREEN_WIDTH/2, SCREEN_WIDTH/2, 500)
    y_mid = np.linspace(-SCREEN_WIDTH, SCREEN_WIDTH, num_mid_points)
    total_psi = np.zeros(len(x_detector), dtype=complex)
    slit_centers = [a/2, -a/2]
    
    for sc in slit_centers:
        for ym in y_mid:
            r1 = np.sqrt(mid_x**2 + (ym - sc)**2)
            amp1 = np.exp(1j * K * r1) / np.sqrt(r1)
            r2 = np.sqrt((D - mid_x)**2 + (x_detector - ym)**2)
            amp2 = np.exp(1j * K * r2) / np.sqrt(r2)
            total_psi += amp1 * amp2
    return x_detector, np.abs(total_psi)**2