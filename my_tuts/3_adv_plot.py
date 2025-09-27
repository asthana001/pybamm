import pybamm

model = pybamm.lithium_ion.DFN()
sim = pybamm.Simulation(model)
sim.solve([0, 3600])

#sim.plot()
# This is a good option for basic plotting. But we can also plot specific variables.


plot_vars = ["Electrolyte concentration [mol.m-3]", "Voltage [V]", ['Positive current collector temperature [K]', 'Negative current collector temperature [K]']]
sim.plot(output_variables=plot_vars)
# But we can specify certain variables as a list and send it to sim.plot()

sim.plot_voltage_components(split_by_electrode=True)
# Special function which plots the voltage components separately.
