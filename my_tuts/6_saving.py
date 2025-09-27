from numpy import size
import pybamm


# Saving the raw data from simulation for further analysis
model = pybamm.lithium_ion.DFN()
sim = pybamm.Simulation(model)


# All results of the simulation are stored in solution object.
# This is a dictionary, so we can access any variable in the solution
solution = sim.solve([0, 3600])



t = solution["Time [s]"]
V = solution["Voltage [V]"]
# Varibale t and V are known as ProcessedVariables.
# To see what variables are stored in the solution, check the variables info from model


# 1. From the Processed variables, we can get the raw data as a NumPy array.
voltage_data = V.entries
time_data = t.entries
# Printing the data
print(f"Time points (s): {time_data[:5]}") 
print(f"Voltage points (V): {voltage_data[:5]}") 


# 2. We can also interpolate the data at certain time
specific_voltages = V([200, 400, 780])
# Values given at argument specify at what time do we want to know the voltage
print(specific_voltages)



# We can also save the whole simulation object 
sim.save("SPMe_simulation.pkl")
# or only the solution object
solution.save("SPMe_solution.pkl")


# and load later
loaded_solution = pybamm.load("SPMe_solution.pkl")
loaded_solution.plot()



# For 0D variables which only change with time (current and voltage), we can also save as .csv and .mat file
# Save voltage and current to a CSV file
solution.save_data("dfn_data.csv",
                    ["Current [A]", "Voltage [V]"],
                    to_format="csv")

# Save to a MATLAB .mat file with shorter, MATLAB-friendly variable names
solution.save_data("dfn_data.mat",
                    ["Current [A]", "Voltage [V]"],
                    to_format="matlab",
                    short_names={"Current [A]": "I", "Voltage [V]": "V"})