import pybamm


# Define all required options for the model as a dictionary
my_opt = {"thermal": "lumped"}
# other options are:
# 1. {"particle mechanics": "swelling and cracking"}
# 2. {"lithium plating": "irreversible"}
# 3. {"loss of active material": "reaction-driven"}
# 4. {"particle size": "distribution"}
# 5. Composite model
# 6. Coupled degradation model


# Include the model dictionary while selecting model
model = pybamm.lithium_ion.SPMe(options=my_opt)
sim = pybamm.Simulation(model)
sim.solve([0, 3600])

sim.plot(
    [
        "Cell temperature [K]",
        "Total heating [W.m-3]",
        "Current [A]",
        "Voltage [V]"
    ]
)