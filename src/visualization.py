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

def plot_geometry_custom(x_detector, intensity, a, d, D):
    source_x, source_y = -d, 0
    mask_x, screen_x = 0, D
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7), 
                                    gridspec_kw={'width_ratios': [20, 1]})
    plt.subplots_adjust(wspace=0.05)

    # --- Geometry Setup ---
    gap_vis = SLIT_WIDTH * 2 
    wall_h = 0.006 
    
    # Draw Metal Sheet (Slits)
    ax1.plot([mask_x, mask_x], [-wall_h, -a/2 - gap_vis], 'k-', lw=6)
    ax1.plot([mask_x, mask_x], [-a/2 + gap_vis, a/2 - gap_vis], 'k-', lw=6)
    ax1.plot([mask_x, mask_x], [a/2 + gap_vis, wall_h], 'k-', lw=6, label="Metal Sheet")

    # Draw Source and Screen
    ax1.plot(source_x, source_y, 'ro', markersize=12, label="Light Source")
    ax1.plot([screen_x, screen_x], [-SCREEN_WIDTH/2, SCREEN_WIDTH/2], 'b-', lw=3, label="Screen")

    # --- LABELS (d, a, D, S1, S2) ---
    # Position S1 and S2 based on 'a'
    ax1.text(mask_x + 0.02, a/2, r'$S_1$', fontsize=12)
    ax1.text(mask_x + 0.02, -a/2, r'$S_2$', fontsize=12)

    # Distance 'd' and 'D'
    ax1.annotate('', xy=(mask_x, -0.005), xytext=(source_x, -0.005), arrowprops=dict(arrowstyle='<->'))
    ax1.text((source_x + mask_x)/2, -0.0058, 'd', fontsize=12, ha='center')
    
    ax1.annotate('', xy=(mask_x, -0.005), xytext=(screen_x, -0.005), arrowprops=dict(arrowstyle='<->'))
    ax1.text((mask_x + screen_x)/2, -0.0058, 'D', fontsize=12, ha='center')

    # Slit Separation 'a'
    ax1.annotate('', xy=(-0.05, -a/2), xytext=(-0.05, a/2), arrowprops=dict(arrowstyle='<->', color='blue'))
    ax1.text(-0.08, 0, 'a', fontsize=12, va='center', color='blue')

    # --- POINT P AND PATHS ---
    y_p = SCREEN_WIDTH * 0.25 
    ax1.plot(screen_x, y_p, 'k*', markersize=10) 
    ax1.text(screen_x + 0.02, y_p, r'$P$', fontsize=14, fontweight='bold')

    # Label distance y
    ax1.annotate('', xy=(screen_x + 0.05, 0), xytext=(screen_x + 0.05, y_p),
                 arrowprops=dict(arrowstyle='<->', color='purple'))
    ax1.text(screen_x + 0.07, y_p/2, r'$y$', color='purple', fontsize=14, va='center')

    # Converging Paths to P
    ax1.plot([mask_x, screen_x], [a/2, y_p], 'g--', alpha=0.6, lw=1.5)
    ax1.plot([mask_x, screen_x], [-a/2, y_p], 'g--', alpha=0.6, lw=1.5, label="Secondary Paths")

    # Initial Paths
    ax1.annotate('', xy=(mask_x, a/2), xytext=(source_x, source_y), arrowprops=dict(arrowstyle="->", color='gray', alpha=0.4))
    ax1.annotate('', xy=(mask_x, -a/2), xytext=(source_x, source_y), arrowprops=dict(arrowstyle="->", color='gray', alpha=0.4))

    # --- Formatting ---
    ax1.set_title("Live Geometry: a={:.2f}mm, D={:.2f}m".format(a*1000, D), fontsize=14)
    ax1.set_ylim(-wall_h, wall_h)
    ax1.set_xlim(source_x - 0.1, screen_x + 0.15) 
    ax1.legend(loc='upper left')

    # --- Intensity Strip ---
    intensity_strip = intensity.reshape(-1, 1)
    ax2.imshow(intensity_strip, cmap='nipy_spectral', aspect='auto', extent=[0, 1, x_detector.min(), x_detector.max()])
    ax2.set_xticks([]); ax2.yaxis.tick_right()
    
    plt.show()

def plot_wave_field_custom(a, D):
    x_space = np.linspace(0.001, D, 500) 
    y_space = np.linspace(-SCREEN_WIDTH/2, SCREEN_WIDTH/2, 500)
    X, Y = np.meshgrid(x_space, y_space)
    psi_field = np.zeros(X.shape, dtype=complex)
    centers = [a/2, -a/2]
    
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

def animate_wave_propagation_custom(a, D):
    x_space = np.linspace(0.001, D, 200)
    y_space = np.linspace(-SCREEN_WIDTH/2, SCREEN_WIDTH/2, 200)
    X, Y = np.meshgrid(x_space, y_space)
    fig, ax = plt.subplots(figsize=(10, 6))
    centers = [a/2, -a/2]
    all_r = [np.sqrt(X**2 + (Y - sp)**2) for c in centers for sp in np.linspace(c - SLIT_WIDTH/2, c + SLIT_WIDTH/2, 5)]
    im = ax.imshow(np.zeros_like(X), extent=[0, D, -SCREEN_WIDTH/2, SCREEN_WIDTH/2], cmap='RdBu', origin='lower', aspect='auto', animated=True, vmin=-0.5, vmax=0.5)
    
    def update(frame):
        t = frame * 0.5e-15 
        psi_total = sum(np.exp(1j * (K * r - OMEGA * t)) / np.sqrt(r) for r in all_r)
        im.set_array(np.real(psi_total))
        return [im]

    ani = FuncAnimation(fig, update, frames=200, interval=30, blit=True)
    plt.show()