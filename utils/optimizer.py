from models.optimization_task import OptimizationTask
import numpy as np
import utils.ansys as ansys



class Optimizer:
    def __init__(self):
        pass

    def optimize(self, ot: OptimizationTask):
        population = self.generate_initial_population(ot)
        self.calculate_dresps(ot,population)

        for i in range(ot.config.max_iteration):
            self.crossbending(population,ot)
            self.mutation(ot)
            self.selection(ot)
            self.check_convergence(ot)
            self.plot_results(ot)

    def generate_initial_population(self, ot: OptimizationTask):
        num_pars= len(ot.design_variables)
        #individuals = np.random.rand(num_pars, ot.config.population_size)
        individuals = np.random.rand(ot.config.population_size,num_pars)
        return individuals

    def crossbending(self, population, ot:OptimizationTask):
        pass

    def mutation(self, ot:OptimizationTask):
        pass
    def selection(self, ot:OptimizationTask):
        pass

    def check_convergence(self, ot:OptimizationTask):
        pass

    def plot_results(self, ot:OptimizationTask):
        pass

    def calculate_dresps(self,ot: OptimizationTask, population):
        #stress_results = np.array([])
        stress_results = np.zeros(ot.config.population_size)
        i = 0
        for individual in population:
            self.change_input(individual, ot)
            ansys.runAPDL(scriptFilename=ot.solver_script,
                          ansyscall=ot.solver_path, workingdir=ot.work_path)
            with open(ot.results_path, encoding='utf-8') as f:
                lines = f.readlines()
            stress_results[i] = lines[0]
            i+=1
        return stress_results



    def change_input(self, individual, ot: OptimizationTask):
        with open(ot.cae_model) as f:
            lines = f.readlines()
        lines[0] = "a="+ str(individual[0])+"\n"
        lines[1] = "b="+ str(individual[1])+"\n"
        with open(ot.cae_model, "w") as f:
            f.writelines(lines)




