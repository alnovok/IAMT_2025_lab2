from models.optimization_task import OptimizationTask
from models.optimization_config import OptimizationConfig
from models.objective import Objective
from models.objective_type import ObjectiveType
from models.constraint import Constraint
from models.design_variable import DesignVariable
from utils.optimizer import Optimizer

my_task = OptimizationTask()
my_task.results_path = 'D:\\ANSWORK\\Novokshenov\\IAMT_2025\\results.txt'
my_task.cae_model = 'D:\\ANSWORK\\Novokshenov\\IAMT_2025\\kirsh.txt'
my_task.config = OptimizationConfig(10,0.5,0.5,30,0.001)
my_task.objective = Objective('mass', ObjectiveType.MIN, [])
my_task.constraints.append(Constraint('stress',220e6,None,[]))
my_task.design_variables.append(DesignVariable('radius_a',0.1,0.9,0.1,[]))
my_task.design_variables.append(DesignVariable('radius_b',0.1,0.9,0.1,[]))
my_task.solver_path = 'C:\\Program Files\\ANSYS Inc\\v172\\ANSYS\\bin\\winx64\\ANSYS172.exe'
my_task.work_path = 'D:\\ANSWORK\\Novokshenov\\IAMT_2025'
my_task.solver_script = 'kirsh'


optimizer = Optimizer()
optimizer.optimize(my_task)