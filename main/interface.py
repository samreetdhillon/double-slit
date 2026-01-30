"""Simple terminal interface for running the double-slit demos."""
import os
import sys

# When executed directly as a script, Python sets the import path such that
# sibling packages like `src` may not be found. Ensure project root is on sys.path
# so `from src import ...` works both when run as `python -m main.interface`
# and as `python main/interface.py`.
if __package__ is None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

from src import simulation, visualization, animation, constants
import matplotlib.pyplot as plt


def welcome():
    print("\nWelcome to the Path-Integral Double-Slit Simulator ✅")
    print("This tool demonstrates double-slit interference via path-integral summation.")
    print("You will be prompted for which demo to run and a few options.\n")


def ask_yes_no(prompt: str) -> bool:
    while True:
        r = input(f"{prompt} [y/n]: ").strip().lower()
        if r in ("y", "yes"):
            return True
        if r in ("n", "no"):
            return False
        print("Please answer 'y' or 'n'.")


def main():
    welcome()

    while True:
        print("Options:\n1) Full demo\n2) Double-slit (observed/unobserved)\n3) Wave field\n4) Animate propagation\n5) Zig-zag path integral\n6) Exit")
        choice = input("Choose an option [1-6]: ").strip()

        if choice == "1":
            print("Running full demo... 🔧")
            x_i, int_i = simulation.simulate_double_slit(observed=False)
            visualization.plot_geometry_with_strip_fixed(x_i, int_i, constants)

            X, Y, field = simulation.compute_wave_field()
            visualization.plot_wave_field(X, Y, field)

            animation.animate_wave_propagation()

            # Comparison plot (Observed vs Unobserved)
            x_q, int_q = simulation.simulate_double_slit(observed=False)
            x_o, int_o = simulation.simulate_double_slit(observed=True)
            plt.figure(figsize=(12, 6))
            plt.plot(x_q * 1000, int_q, 'g-', label="Quantum (Unobserved)")
            plt.plot(x_o * 1000, int_o, 'r--', label="Observed (Particle behavior)")
            plt.title("The Observer Effect: Wave-Particle Duality")
            plt.xlabel("Position on Screen (mm)")
            plt.ylabel("Intensity")
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.show()

        elif choice == "2":
            obs = ask_yes_no("Simulate with which-path information (observed)?")
            x, intensity = simulation.simulate_double_slit(observed=obs)
            visualization.plot_2d_interference(x, intensity)

        elif choice == "3":
            print("Computing and plotting wave field...")
            X, Y, field = simulation.compute_wave_field()
            visualization.plot_wave_field(X, Y, field)

        elif choice == "4":
            print("Starting animation (close the window to return to menu)...")
            animation.animate_wave_propagation()

        elif choice == "5":
            print("Computing zig-zag path integral...")
            x, intensity = simulation.simulate_zigzag_paths()
            plt.figure(figsize=(10, 6))
            plt.plot(x * 1000, intensity / intensity.max(), color='purple', label="Zig-Zag Path Integral")
            plt.title("Path Integral with Intermediate Scattering Layer")
            plt.xlabel("Position on Screen (mm)")
            plt.ylabel("Normalized Intensity")
            plt.legend()
            plt.show()

        elif choice == "6":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
