import pybamm

# ----- First, we chose the inbuilt DFN model or any model from the library. -----
model = pybamm.lithium_ion.DFN()
# pybamm.lithium_ion is the module containing various lithium-ion models.
# DFN is the class representing the DFN model.
# This creates an instance of the DFN model and stores it in the variable "model". 
# This "model" object contains all the mathematical equations (the governing PDEs and ODEs) that describe the battery's behavior.


# ----- Next, we create a simulation object using the defined model for solving it. -----
sim = pybamm.Simulation(model)
# pybamm.Simulation class is a powerful tool that handles all the background work.
# It does 3 things:
# 1. Loads default parameter values for the model.
# 2. Decretizes the model by converting PDE into system of ODEs.
# 3. Choses appropriate solver for solving the ODEs.


# ----- Now, we run the solver for solving the model. -----
sim.solve([0, 3600])
# The argument [0, 3600] specifies the time range for the simulation in seconds.
# So we are telling the solver to solve the model for 1 hour.
# Solver will run until it reaches time limit or termination event.


# ----- Finally, we plot the results. -----
sim.plot()
# This generates a set of default plots for the model.


print(sim.parameter_values.search("current"))
print(model.variables.search("current"))
# This helps us search certain parameters with keywords and print those