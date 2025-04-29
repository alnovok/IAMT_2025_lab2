from models.optimization_config import OptimizationConfig
from models.objective import Objective
from models.objective_type import ObjectiveType
from models.constraint import Constraint
from models.design_variable import DesignVariable
from typing import List

class OptimizationTask:
    def __init__(self,solver_path = None, solver_script = None, config: OptimizationConfig = None, cae_model = None,
                 objective: Objective = None, constraints: List[Constraint] = [],
                 design_variables: List[DesignVariable]=[], results_path = None, work_path = None):
        self.solver_path = solver_path
        self.solver_script = solver_script
        self.config = config
        self.cae_model = cae_model
        self.objective = objective
        self.constraints = constraints
        self.design_variables = design_variables
        self.results_path = results_path
        self.work_path = work_path
