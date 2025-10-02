# PyBaMM Cell Modeling

Welcome to my collection of battery cell modeling projects! This repository serves as my personal playground and learning space for exploring the capabilities of PyBAMM (Python Battery Mathematical Modelling), an open-source library for the simulation of lithium-ion batteries.

Here, you'll find various examples, from fundamental models to more complex simulations, as I deepen my understanding of battery physics and electrochemical modeling.

## About This Repository
The goal of this repository is to document my journey in learning and applying battery simulation techniques. Each folder or file represents a specific practice case, model, or feature exploration within the PyBAMM framework.

---

## Repository Structure


### [`my_tuts/`](my_tuts/) - PyBaMM Learning Tutorials

| File | Description |
|------|-------------|
| [`1_basic.py`](my_tuts/1_basic.py) | Introduction to PyBaMM: running a basic DFN model, creating simulations, solving and plotting results |
| [`2_comp_models.py`](my_tuts/2_comp_models.py) | Comparing multiple models (SPM, SPMe, DFN) using dynamic plotting for side-by-side comparison |
| [`3_adv_plot.py`](my_tuts/3_adv_plot.py) | Advanced plotting techniques: selecting specific variables and using voltage component plots |
| [`4_params.py`](my_tuts/4_params.py) | Working with parameter values: loading parameter sets, modifying parameters, using function parameters, and parameter sweeping |
| [`5_exp.py`](my_tuts/5_exp.py) | Creating and running experiments with multiple steps (discharge, rest, charge, hold) and cycling |
| [`6_saving.py`](my_tuts/6_saving.py) | Saving simulation data: extracting processed variables, interpolation, and exporting to CSV/MATLAB formats |
| [`7_model_opt.py`](my_tuts/7_model_opt.py) | Using model options like thermal effects, particle mechanics, lithium plating, and degradation mechanisms |
| [`8_solver.py`](my_tuts/8_solver.py) | Configuring solver options: choosing solvers and setting relative/absolute tolerances |
| [`9_mesh.py`](my_tuts/9_mesh.py) | Mesh configuration and refinement studies: customizing spatial discretization for improved accuracy |

---

### [`practice/`](practice/) - PyBaMM Practice Simulations

| File | Description |
|------|-------------|
| [`practice1.ipynb`](practice/practice1.ipynb) | Comparison of different SEI (Solid Electrolyte Interphase) models and their impact on SEI thickness and lithium inventory loss |
| [`practice2.ipynb`](practice/practice2.ipynb) | Comparison of lithium plating models using OKane2022 parameters |
| [`practice3.ipynb`](practice/practice3.ipynb) | Study of State of Charge (SoC) effects on CCCV charging curves for fully charged, half charged, and empty batteries |

---

### [`matlab_tut/`](matlab_tut/) - MATLAB ODE/PDE Problems

| File | Description |
|------|-------------|
| [`ode.ipynb`](matlab_tut/ode.ipynb) | Basic ODE solving exercises and examples in MATLAB |
| [`ode_oscillator.ipynb`](matlab_tut/ode_oscillator.ipynb) | ODE problems related to oscillator systems |
| [`ode_spm.ipynb`](matlab_tut/ode_spm.ipynb) | Single Particle Model (SPM) diffusion - modeling average lithium concentration in spherical particles during discharge |
| [`ode_thermal.ipynb`](matlab_tut/ode_thermal.ipynb) | Thermal modeling ODE problems |
| [`pde.ipynb`](matlab_tut/pde.ipynb) | Basic PDE solving exercises and examples in MATLAB |
| [`pde_diffusion.ipynb`](matlab_tut/pde_diffusion.ipynb) | Diffusion PDE problems in MATLAB |
| [`pde_heat.ipynb`](matlab_tut/pde_heat.ipynb) | Heat transfer PDE problems |
| [`pdetb.ipynb`](matlab_tut/pdetb.ipynb) | Basic 2D PDE solving using PDE Toolbox Code |
| [`pdetb_heat.ipynb`](matlab_tut/pdetb_heat.ipynb) | 2D heat transfer using PDE Toolbox |

---


## Resources

- [PyBaMM Documentation](https://docs.pybamm.org/)
- [PyBaMM GitHub Repository](https://github.com/pybamm-team/PyBaMM)