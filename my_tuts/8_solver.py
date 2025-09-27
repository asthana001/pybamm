import pybamm


# First we specify which solver do we want to use
my_solver = pybamm.IDAKLUSolver(rtol=1e-8, atol=1e-12)
# Then re specify the relative tolerance and absolute tolerance for the solcer
# Relative tolerance = mearue of error relative to magnitude of solution
# Absolute tolerance = thershold for error


model = pybamm.lithium_ion.DFN()
sim = pybamm.Simulation(model, solver=my_solver)
# Then specifu solver in the sim obejct


sim.solve([0, 3600])