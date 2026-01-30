# Double-Slit Path-Integral Simulator

A small Python project that simulates and visualizes the quantum double-slit experiment using a simple path-integral summation approach. The project demonstrates interference vs. particle-like (observed) behavior, wave-field propagation, and more advanced path-integral ideas ("zig-zag" intermediate scattering points).

---

## Highlights

- **Path integral based** amplitude summation for single- and double-slit setups
- Multiple demos: standard interference, observer effect (collapse), wave-field, animated propagation, and zig-zag path integral
- Lightweight and dependency-minimal: uses **numpy** and **matplotlib**

---

## Project structure

- `main.py` — Terminal menu to run interactive demos
- `main/interface.py` — Alternative CLI helper (kept for developer convenience)
- `src/constants.py` — Physical and simulation constants (wavelength, slit geometry, sampling count, etc.)
- `src/simulation.py` — Core simulation routines
  - `calculate_psi_for_slit(x_detector, center)` — helper to compute complex amplitude from a slit
  - `simulate_standard()` — quantum interference (add amplitudes then square)
  - `simulate_observed()` — observed/which-path case (add intensities)
  - `simulate_zigzag_paths(num_mid_points=1000)` — path integral with intermediate scattering layer
- `src/visualization.py` — plotting & animation utilities
  - `plot_geometry_with_strip(x_detector, intensity)`
  - `plot_2d_interference(x_detector, intensity)`
  - `plot_wave_field()`
  - `animate_wave_propagation()`

---

## Quick start

Prerequisites: Python 3.8+ and a display capable of showing Matplotlib windows.

1. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the interactive terminal menu:

```bash
python main.py
```

Choose a demo from the menu (1–6). Each demo will open Matplotlib windows with the corresponding visualization.

---

## Usage examples (as a library)

You can also import the functions and use them directly from code or from an interactive Python session:

```python
from src.simulation import simulate_standard, simulate_observed
from src.visualization import plot_2d_interference

x, intensity = simulate_standard()
plot_2d_interference(x, intensity)

# Compare observed vs unobserved
x_q, int_q = simulate_standard()
x_o, int_o = simulate_observed()

import matplotlib.pyplot as plt
plt.plot(x_q * 1000, int_q / int_q.max(), label='Quantum')
plt.plot(x_o * 1000, int_o / int_o.max(), label='Observed', linestyle='--')
plt.legend(); plt.show()
```

---

## Configuration & parameters

Edit `src/constants.py` to modify physical or numerical parameters, for example:

- `WAVELENGTH` — light wavelength in meters
- `SLIT_DISTANCE`, `SLIT_WIDTH` — geometry of the slit mask
- `SCREEN_DISTANCE`, `SCREEN_WIDTH` — detection screen geometry
- `NUM_POINTS`, `SAMPLES_PER_SLIT` — numerical resolution (increase for higher accuracy at cost of speed)

Note: Some heavy simulations (e.g., `simulate_zigzag_paths` with many mid points) can become slow. Reduce resolution or increase CPU resources when exploring large parameter values.

---

## Developer notes & known issues

- `main/interface.py` contains an alternative CLI but references different function names and additional modules (e.g., `animation`) that are not present in the current `src` implementation. If you plan to use `main/interface.py`, either update it to call the functions defined in `src/simulation.py` / `src/visualization.py` or add the missing wrappers.

- No automated tests are included yet. Adding unit tests around simulation numeric properties and analytic limits (e.g., far-field single-slit envelope) is recommended.

- Consider vectorizing or parallelizing heavy loops (e.g., in `simulate_zigzag_paths`) if you need better performance.

---

## Contribution

Contributions are welcome! Suggested next steps:

1. Add unit tests and CI (GitHub Actions)
2. Improve modularity (separate animation module, add command-line flags)
3. Add a small example gallery of figures and GIFs

Please open issues or submit pull requests with clear descriptions and tests.
