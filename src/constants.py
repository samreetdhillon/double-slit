import numpy as np

# --- WAVE PHYSICS ---
WAVELENGTH = 500e-9 
K = 2 * np.pi / WAVELENGTH
SPEED_OF_LIGHT = 3e8
FREQ = SPEED_OF_LIGHT / WAVELENGTH
OMEGA = 2 * np.pi * FREQ

# --- SIMULATION SETTINGS ---
SLIT_WIDTH = 0.05e-3  # Width of each slit
SCREEN_WIDTH = 0.02   # 2cm wide detector
NUM_POINTS = 1000     # Pixels on screen
SAMPLES_PER_SLIT = 40 # Path integral resolution