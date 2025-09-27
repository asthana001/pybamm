import pybamm

model = pybamm.lithium_ion.DFN()

# This shows the defauly mesh values
print(model.default_var_pts)


# We can create our own mesh using a dictionary
var_pts = {
    "x_n": 10,  # negative electrode
    "x_s": 10,  # separator
    "x_p": 10,  # positive electrode
    "r_n": 10,  # negative particle
    "r_p": 10,  # positive particle
}

# And then pass the custom mesh to the simulation
sim = pybamm.Simulation(model, var_pts=var_pts)
sim.solve([0, 3600])
sim.plot()



# To do a mesh refinement study, first specify the mesh points
npts = [4, 8, 16, 32, 64]

# Then iterate through each point and define the mesh and solve the model
model = pybamm.lithium_ion.DFN()
solutions = []
for N in npts:
    var_pts = {
        "x_n": N, "x_s": N, "x_p": N,
        "r_n": N, "r_p": N
    }
    sim = pybamm.Simulation(model, var_pts=var_pts)
    sim.solve([0, 3600])
    solutions.append(sim.solution)

#Finally plot all the solutions
pybamm.dynamic_plot(solutions, ["Voltage [V]"], labels=npts)