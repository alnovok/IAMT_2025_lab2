class OptimizationConfig:
    def __init__(self, population_size, cross_probapility, mutation_probability, max_iteration, error):
        self.population_size = population_size
        self.cross_probability = cross_probapility
        self.mutation_probability = mutation_probability
        self.max_iteration = max_iteration
        self.error = error