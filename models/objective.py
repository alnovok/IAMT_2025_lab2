from models.objective_type import ObjectiveType

class Objective:
    def __init__(self, name, type: ObjectiveType, values):
        self.name = name
        self.type = type
        self.values = values
