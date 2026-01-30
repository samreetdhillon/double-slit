import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from src.constants import *

def plot_2d_interference(x_detector, intensity):
    height = 500  
    intensity_2d = np.tile(intensity, (height, 1))
    plt.figure(figsize=(12, 4))
    extent = [x_detector.min()*1000, x_detector.max()*1000, -2, 2]
    plt.imshow(intensity_2d, extent=extent, cmap='nipy_spectral', aspect='auto')
    plt.colorbar(label='Intensity')
    plt.title("2D Path Integral Simulation: Double Slit Interference")
    plt.xlabel("Position on Screen (mm)")
    plt.ylabel("Screen Height (mm)")
    plt.show()

def plot_geometry_with_strip(x_detector, intensity):
    source_x, source_y = -0.2, 0
    mask_x, screen_x = 0, SCREEN_DISTANCE
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7), gridspec_kw={'width_ratios': [20, 1]})
    plt.subplots_adjust(wspace=0.05)

    # Drawing the Metal Sheet
    gap_vis, wall_h = SLIT_WIDTH * 2, 0.006 
    ax1.plot([mask_x, mask_x], [-wall_h, -SLIT_DISTANCE/2 - gap_vis], 'k-', lw=6)
    ax1.plot([mask_x, mask_x], [-SLIT_DISTANCE/2 + gap_vis, SLIT_DISTANCE/2 - gap_vis], 'k-', lw=6)
    ax1.plot([mask_x, mask_x], [SLIT_DISTANCE/2 + gap_vis, wall_h], 'k-', lw=6, label="Metal Sheet")
    
    # Screen and Source
    ax1.plot(source_x, source_y, 'ro', markersize=12, label="Light Source")
    ax1.plot([screen_x, screen_x], [-SCREEN_WIDTH/2, SCREEN_WIDTH/2], 'b-', lw=3, label="Screen")

    # Annotations and Labels
    ax1.set_title("Experimental Setup: Top-Down Perspective")
    ax1.set_ylim(-wall_h, wall_h)
    ax1.set_xlim(source_x - 0.1, screen_x + 0.1)
    ax1.legend(loc='upper left')
    ax1.grid(True, linestyle=':', alpha=0.5)

    # Intensity Strip
    intensity_strip = intensity.reshape(-1, 1)
    ax2.imshow(intensity_strip, cmap='nipy_spectral', aspect='auto', extent=[0, 1, x_detector.min(), x_detector.max()])
    ax2.set_xticks([]); ax2.yaxis.tick_right(); ax2.set_title("Result")
    plt.show()

def plot_wave_field():
    x_space = np.linspace(0.001, SCREEN_DISTANCE, 500) 
    y_space = np.linspace(-SCREEN_WIDTH/2, SCREEN_WIDTH/2, 500)
    X, Y = np.meshgrid(x_space, y_space)
    psi_field = np.zeros(X.shape, dtype=complex)
    centers = [SLIT_DISTANCE/2, -SLIT_DISTANCE/2]
    
    for center in centers:
        slit_points = np.linspace(center - SLIT_WIDTH/2, center + SLIT_WIDTH/2, 10)
        for sp in slit_points:
            r = np.sqrt(X**2 + (Y - sp)**2)
            psi_field += np.exp(1j * K * r) / np.sqrt(r + 1e-9)

    intensity_field = np.abs(psi_field)**2
    vmax_val = np.percentile(intensity_field, 95) 
    plt.figure(figsize=(12, 6))
    plt.imshow(intensity_field, extent=[0, SCREEN_DISTANCE, -SCREEN_WIDTH/2, SCREEN_WIDTH/2], cmap='magma', origin='lower', aspect='auto', vmax=vmax_val)
    plt.title("Wave-Field Propagation: Interference Ripples in Space")
    plt.colorbar(label='Relative Intensity')
    plt.show()

def animate_wave_propagation():
    x_space = np.linspace(0.001, SCREEN_DISTANCE, 200)
    y_space = np.linspace(-SCREEN_WIDTH/2, SCREEN_WIDTH/2, 200)
    X, Y = np.meshgrid(x_space, y_space)
    fig, ax = plt.subplots(figsize=(10, 6))
    centers = [SLIT_DISTANCE/2, -SLIT_DISTANCE/2]
    all_r = [np.sqrt(X**2 + (Y - sp)**2) for c in centers for sp in np.linspace(c - SLIT_WIDTH/2, c + SLIT_WIDTH/2, 5)]
    im = ax.imshow(np.zeros_like(X), extent=[0, SCREEN_DISTANCE, -SCREEN_WIDTH/2, SCREEN_WIDTH/2], cmap='RdBu', origin='lower', aspect='auto', animated=True, vmin=-0.5, vmax=0.5)
    
    def update(frame):
        t = frame * 0.5e-15 
        psi_total = sum(np.exp(1j * (K * r - OMEGA * t)) / np.sqrt(r) for r in all_r)
        im.set_array(np.real(psi_total))
        return [im]

    ani = FuncAnimation(fig, update, frames=200, interval=30, blit=True)
    plt.show()