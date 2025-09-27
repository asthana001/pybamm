import pybamm


# PyBaMM comes with several pre-defined parameter sets from various research papers. 
# Untill now we were using default parameter. Now we will see how to modify them.


# First, load a pre-defined parameter set.
# This loads the parameter values for the Chen2020 parameter set into the parameter_values object.
param_vals = pybamm.ParameterValues("Chen2020")
# This forms a dictionary of parameter values.


# We can change specific parameters in the parameter set.
param_vals["Current function [A]"] = 10


# Now continue with the model setup.
model = pybamm.lithium_ion.DFN()


# In the Simulation setup, we can define which parameter values to use.
sim = pybamm.Simulation(model, parameter_values=param_vals)
sim.solve([0, 3600])

sim.plot()



# ----- For a function parameter -----
import numpy as np

# To define function parameters, we can use a function.
def my_current(t):
    return pybamm.sin(2 * np.pi * t / 60)

# Update the parameter value with the function itself (not the result of calling it)
param_vals["Current function [A]"] = my_current

# Run the simulation
sim = pybamm.Simulation(model, parameter_values=param_vals)
t= np.arange(0, 121, 1) # Evaluate every second for 2 minutes
sim.solve(t_eval=t)
sim.plot(["Current [A]", "Voltage [V]"])



# ----- For parameter sweeping -----
parameter_values["Current function [A]"] = "[input]"
# Define the parameter with an input placeholder
sim = pybamm.Simulation(model, parameter_values=parameter_values)

import matplotlib.pyplot as plt

# Then we can pass the input values to this placeholder
for c in [0.1, 0.2, 0.3]:
    soln = sim.solve([0, 3600], inputs={"Current function [A]": c})
    plt.plot(soln["Time [s]"].entries, soln["Voltage [V]"].entries, label=f"{c} A")

plt.xlabel("Time [s]")
plt.ylabel("Terminal voltage [V]")
plt.legend()
plt.show()

