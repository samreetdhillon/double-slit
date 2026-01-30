import os
import matplotlib.pyplot as plt
from src.simulation import simulate_standard, simulate_observed, simulate_zigzag_paths
from src.visualization import (
    plot_geometry_with_strip, 
    plot_2d_interference, 
    animate_wave_propagation, 
    plot_wave_field
)

def menu():
    while True:
        print("\n" + "="*30)
        print(" QUANTUM DOUBLE-SLIT LAB ")
        print("="*30)
        print("1. Standard Interference (Geometry + Strip)")
        print("2. 2D Interference Fringes (Heatmap)")
        print("3. Static Wave-Field (Ripples in Space)")
        print("4. Time-of-Flight Animation")
        print("5. The Observer Effect (Wave vs Particle)")
        print("6. Zig-Zag Path Integral (1000 points)")
        print("q. Quit")
        
        choice = input("\nSelect an experiment: ").strip().lower()

        if choice == '1':
            x, intensity = simulate_standard()
            plot_geometry_with_strip(x, intensity)
            
        elif choice == '2':
            x, intensity = simulate_standard()
            plot_2d_interference(x, intensity)
            
        elif choice == '3':
            plot_wave_field()
            
        elif choice == '4':
            animate_wave_propagation()
            
        elif choice == '5':
            # Run both simulations to see the contrast
            x_q, int_q = simulate_standard()
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
            # Handle the data from the zig-zag simulation
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

if __name__ == "__main__":
    menu()