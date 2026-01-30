# Double-Slit Path-Integral Simulator 🔬

A compact Python project that simulates and visualizes the quantum double-slit experiment using a path-integral summation approach. The repository provides interactive demos (terminal-driven) and library functions to reproduce interference patterns, demonstrate the observer effect, and explore more advanced path-integral variants (e.g., zig-zag intermediate scattering points).

---

## Highlights

- **Path integral based** amplitude summation for single- and double-slit setups
- Demos: standard interference, observer effect (collapse), wave-field, animated propagation, and zig-zag path integral
- Minimal dependencies: **numpy** and **matplotlib**

---

## Project structure

- `.gitignore` — ignores `venv/`, caches and common build artifacts
- `main.py` — Terminal menu to run interactive demos (current, stable CLI)
- `main/interface.py` — Alternative CLI (out-of-date; see Developer Notes)
- `requirements.txt` — project dependencies
- `src/constants.py` — physical and simulation constants
- `src/simulation.py` — core simulation functions
- `src/visualization.py` — plotting and animation utilities

---

## Quick start

Requirements: Python 3.8+ and a display capable of showing Matplotlib windows.

1. Create & activate virtual environment (recommended):

```bash
python -m venv venv
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (cmd.exe)
venv\Scripts\activate.bat
# macOS / Linux
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Launch the interactive menu:

```bash
python main.py
```

Pick an option (1–6) to run a demo; Matplotlib windows will open for visualizations.

---

## Usage as a library

You can import and use simulation/visualization functions directly:

```python
from src.simulation import simulate_standard, simulate_observed
from src.visualization import plot_2d_interference

x, intensity = simulate_standard()
plot_2d_interference(x, intensity)
```

For manual comparisons and plotting, normalize intensities and plot with Matplotlib (see examples in `main.py`).

---

## Configuration

Change simulation parameters in `src/constants.py`:

- `WAVELENGTH`, `SLIT_DISTANCE`, `SLIT_WIDTH`, `SCREEN_DISTANCE`, `SCREEN_WIDTH`
- `NUM_POINTS`, `SAMPLES_PER_SLIT` (numerical resolution)

Tip: Large values for `SAMPLES_PER_SLIT` or `num_mid_points` in `simulate_zigzag_paths` can produce slow runs; decrease values for quicker iteration.

---

## Developer notes & known issues

- Interface mismatch: `main/interface.py` imports `animation` and calls functions like `simulate_double_slit(observed=...)`, `compute_wave_field()`, and `visualization.plot_geometry_with_strip_fixed(...)`. These names do not match the functions currently implemented in `src/simulation.py` and `src/visualization.py` (e.g. `simulate_standard`, `simulate_observed`, `plot_geometry_with_strip`). Either update `main/interface.py` to use the current APIs or add compatibility wrappers in `src`.

- No tests yet: adding unit tests for basic numeric correctness and regression (e.g., energy conservation, single-slit envelope) is strongly recommended.

- Performance: `simulate_zigzag_paths` is computationally heavy (nested loops over many mid-points). Consider vectorization, numba, or multiprocessing if you need faster runs.

- Headless environments: if running on a server without display, set Matplotlib backend (e.g. `Agg`) or save figures to files instead of showing windows.

---

## Contribution ideas

- Add unit tests and a CI pipeline (GitHub Actions)
- Sync `main/interface.py` with the `src` API or deprecate it and add a replacement CLI module
- Add an `examples/` folder with saved figures and short notebooks demonstrating each demo
- Add a permissive LICENSE (MIT suggested) and CONTRIBUTING guide
