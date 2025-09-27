import pybamm

models = [
    pybamm.lithium_ion.SPM(),
    pybamm.lithium_ion.SPMe(),
    pybamm.lithium_ion.DFN(),
]
# This creates a list of models to compare

sims = []
# Create an empty list to store the solved simulations

# Now loop over all the models and solve them
for model in models:
    sim = pybamm.Simulation(model)
    sim.solve([0, 3600])
    sims.append(sim)


pybamm.dynamic_plot(sims)
# This function is specifically designed to take a list of simulations and plot them all on the same figure for direct comparison.