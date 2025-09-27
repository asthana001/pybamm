import pybamm

# Until now we have only done single step simulations - like discharging at constant current, etc.
# Experiments string together multiple steps to simulate complex cycling.

experiment = pybamm.Experiment(
    [
            "Discharge at C/10 for 10 hours or until 3.3 V",
            "Rest for 1 hour",
            "Charge at 1 A until 4.1 V",
            "Hold at 4.1 V until 50 mA",
            "Rest for 1 hour",
    ]
    * 3  # Repeat the cycle in the tuple 3 times
    + [
        "Discharge at 1C until 3.3 V", # Add a final discharge step
    ]
)

model = pybamm.lithium_ion.DFN()
sim = pybamm.Simulation(model, experiment=experiment)
# To run the experiment, we pass the experiment to the simulation object.


sim.solve()
# We do not pass a time interval to sove() as the experiment itself defines the duration.
#sim.plot()


# We can also plot a specific cycle
sim.solution.cycles[0].plot()