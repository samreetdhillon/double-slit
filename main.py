
import os
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from src.constants import SLIT_DISTANCE, SCREEN_DISTANCE
from src.simulation import *
from src.visualization import *

def get_input(prompt, default):
    user_val = input(f"{prompt} (Default {default}): ").strip()
    return float(user_val) if user_val else default

'''
def menu():
    while True:
        print("\n" + "="*30)
        print(" QUANTUM DOUBLE-SLIT LAB ")
        print("="*30)
        print("1. Standard Interference (Geometry + Strip) [CUSTOMIZABLE]")
        print("2. 2D Interference Fringes (Heatmap)")
        print("3. Static Wave-Field (Ripples in Space)")
        print("4. Time-of-Flight Animation")
        print("5. The Observer Effect (Wave vs Particle)")
        print("6. Zig-Zag Path Integral (1000 points)")
        print("q. Quit")
        
        choice = input("\nSelect an experiment: ").strip().lower()

        if choice == '1':
            print("\n--- Configure Experiment ---")
            # Convert units: mm -> m, cm -> m
            a_val = get_input("Slit separation 'a' in mm", 1.0) * 1e-3
            d_val = get_input("Source distance 'd' in cm", 20.0) * 1e-2
            D_val = get_input("Screen distance 'D' in meters", 1.0)
            
            x, intensity = simulate_standard_custom(a_val, D_val)
            # Make sure your visualization.py function matches these arguments!
            plot_geometry_custom(x, intensity, a_val, d_val, D_val)
            
        elif choice == '2':
            # Using custom with default values to act as "Standard"
            from src.constants import SLIT_DISTANCE, SCREEN_DISTANCE
            x, intensity = simulate_standard_custom(SLIT_DISTANCE, SCREEN_DISTANCE)
            plot_2d_interference(x, intensity)
            
        elif choice == '3':
            plot_wave_field()
            
        elif choice == '4':
            animate_wave_propagation()
            
        elif choice == '5':
            from src.constants import SLIT_DISTANCE, SCREEN_DISTANCE
            x_q, int_q = simulate_standard_custom(SLIT_DISTANCE, SCREEN_DISTANCE)
            x_o, int_o = simulate_observed()
            
            plt.figure(figsize=(12, 6))
            plt.plot(x_q * 1000, int_q / int_q.max(), 'g-', label="Quantum (Wave)")
            plt.plot(x_o * 1000, int_o / int_o.max(), 'r--', label="Observed (Particle)")
            plt.title("Observer Effect: Wave-Particle Duality")
            plt.xlabel("Position on Screen (mm)")
            plt.ylabel("Normalized Intensity")
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.show()
            
        elif choice == '6':
            x, intensity = simulate_zigzag_paths(num_mid_points=1000)
            plt.figure(figsize=(10, 6))
            plt.plot(x * 1000, intensity / intensity.max(), color='purple')
            plt.title("Zig-Zag Path Integral (1000 Intermediate Points)")
            plt.xlabel("Position on Screen (mm)")
            plt.ylabel("Normalized Intensity")
            plt.show()
            
        elif choice == 'q':
            print("Exiting Lab...")
            break
        else:
            print("Invalid choice, try again.")
'''

def menu():
    print("\n" + "="*40)
    print(" WELCOME TO THE UNIVERSAL QUANTUM LAB ")
    print("="*40)
    
    # SET GLOBAL PARAMS AT START
    a = get_input("Slit separation 'a' in mm", 1.0) * 1e-3
    d = get_input("Source distance 'd' in cm", 20.0) * 1e-2
    D = get_input("Screen distance 'D' in meters", 1.0)

    while True:
        print(f"\nCURRENT CONFIG: a={a*1000:.2f}mm, d={d*100:.1f}cm, D={D:.2f}m")
        print("-" * 40)
        print("1. Geometry + Intensity Strip")
        print("2. 2D Heatmap")
        print("3. Static Wave-Field")
        print("4. Time Animation")
        print("5. Observer Effect (Comparison)")
        print("6. Zig-Zag (1000 paths)")
        print("c. Change Parameters")
        print("q. Quit")
        
        choice = input("\nSelect experiment: ").strip().lower()

        if choice == '1':
            x, intensity = simulate_standard_custom(a, D)
            plot_geometry_custom(x, intensity, a, d, D)
        elif choice == '2':
            x, intensity = simulate_standard_custom(a, D)
            plot_2d_interference(x, intensity)
        elif choice == '3':
            plot_wave_field_custom(a, D)
        elif choice == '4':
            animate_wave_propagation_custom(a, D)
        elif choice == '5':
            # 1. Get Data
            x_q, int_q = simulate_standard_custom(a, D)
            x_o, int_o = simulate_observed_custom(a, D)
            
            # 2. Create Plot
            plt.figure(figsize=(12, 6))
            # Multiply x by 1000 to show mm on the axis
            plt.plot(x_q * 1000, int_q / int_q.max(), 'g-', label="Quantum (Wave)")
            plt.plot(x_o * 1000, int_o / int_o.max(), 'r--', label="Observed (Particle)")
            
            plt.title(f"Observer Effect: a={a*1000:.2f}mm, D={D:.2f}m")
            plt.xlabel("Position on Screen (mm)")
            plt.ylabel("Normalized Intensity")
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.show() # <--- This was missing!

        elif choice == '6':
            print("Calculating 1000 zig-zag paths... please wait...")
            # 1. Get Data
            x, intensity = simulate_zigzag_custom(a, D)
            
            # 2. Create Plot
            plt.figure(figsize=(10, 6))
            plt.plot(x * 1000, intensity / intensity.max(), color='purple', lw=1.5)
            
            plt.title(f"Zig-Zag Path Integral (1000 Intermediate Points)\na={a*1000:.2f}mm, D={D:.2f}m")
            plt.xlabel("Position on Screen (mm)")
            plt.ylabel("Normalized Intensity")
            plt.grid(True, linestyle=':', alpha=0.6)
            plt.show() # <--- This was missing!
        elif choice == 'c':
            a = get_input("New 'a' (mm)", a*1000) * 1e-3
            d = get_input("New 'd' (cm)", d*100) * 1e-2
            D = get_input("New 'D' (m)", D)
        elif choice == 'q':
            break

if __name__ == "__main__":
    menu()