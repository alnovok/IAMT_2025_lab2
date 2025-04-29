class Constraint:
    def __init__(self, name, upper_bound: int = None, lower_bound: int = None, values = []):
        self.name = name
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.values = values
