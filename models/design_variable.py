class DesignVariable:
    def __init__(self,name, lower_bound, upper_bound, step, values):
        self.name = name
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.step = step
        self.values = values