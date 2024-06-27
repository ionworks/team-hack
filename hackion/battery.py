import pybamm


class Battery:
    def __init__(
        self,
        initial_soc=1.0,
        temperature=25,
        model=pybamm.lithium_ion.SPM(),
        chemistry="Chen2020",
    ):
        self.model = model
        self.parameter_values = pybamm.ParameterValues(chemistry)
        self.parameter_values.set_initial_stoichiometries(initial_soc)

        self.temperature = temperature
        self.initial_soc = initial_soc
        self.current_state = None

    def determine_final_soc(self, power_profile):
        experiment = pybamm.Experiment(
            [pybamm.step.power(power_profile)], temperature=f"{self.temperature}oC"
        )

        sim = pybamm.Simulation(
            self.model, parameter_values=self.parameter_values, experiment=experiment
        )
        sim.solve(starting_solution=self.current_state)

        self.current_state = sim.solution.last_state

        x0, x100, y100, y0 = pybamm.lithium_ion.get_min_max_stoichiometries(
            self.parameter_values
        )

        x = sim.solution["Average negative particle stoichiometry"].data[-1]

        SOC = (x - x0) / (x100 - x0)

        return SOC
