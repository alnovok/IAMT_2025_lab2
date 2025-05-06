from models.optimization_task import OptimizationTask
import numpy as np
import utils.ansys as ansys



class Optimizer:
    def __init__(self):
        pass

    def optimize(self, ot: OptimizationTask):
        population = self.generate_initial_population(ot)
        population_results = self.calculate_dresps(ot,population)
        for i in range(ot.config.max_iteration):
            children  = self.crossbending(population,ot)
            mutated_children = self.mutation(ot, children)
            children_results = self.calculate_dresps(ot, mutated_children)
            population, population_results = self.selection(ot,population, population_results, mutated_children, children_results)
            #self.check_convergence(ot)
            ot.objective.values.append(population_results[0])
        print(ot.objective.values)


    def generate_initial_population(self, ot: OptimizationTask):
        num_pars= len(ot.design_variables)
        #individuals = np.random.rand(num_pars, ot.config.population_size)
        individuals = np.random.rand(ot.config.population_size,num_pars)
        return individuals

    def crossbending(self, population, ot:OptimizationTask):
        children = []
        for i in range(ot.config.population_size):
            parent1 = population[np.random.randint(0,ot.config.population_size)]
            parent2 = population[np.random.randint(0,ot.config.population_size)]
            children.append(np.array([parent1[0], parent2[1]]))
        return np.array(children)

    def mutation(self, ot:OptimizationTask, children):
        mutated_children = []
        for child in children:
            mutation1 = (-1+np.random.rand()*2)*0.1
            mutation2 = (-1+np.random.rand()*2)*0.1
            child = child + np.array([mutation1, mutation2])
            if child[0] < ot.design_variables[0].lower_bound:
                child[0] = ot.design_variables[0].lower_bound
            if child[0] > ot.design_variables[0].upper_bound:
                child[0] = ot.design_variables[0].upper_bound
            if child[1] < ot.design_variables[1].lower_bound:
                child[1] = ot.design_variables[1].lower_bound
            if child[1] > ot.design_variables[1].upper_bound:
                child[1] = ot.design_variables[1].upper_bound
            mutated_children.append(child)
        return np.array(mutated_children)

    def selection(self, ot:OptimizationTask, population, population_results, children, children_results):
        results = np.concatenate((children_results.T,population_results.T),axis = 1).T
        population=np.concatenate((children.T, population.T), axis = 1)
        temp_results = results
        for i in range (len(ot.constraints)):
            temp_results[:,i+1] = temp_results[:,i+1] - ot.constraints[i].upper_bound
        temp_results = np.where(temp_results <= 0, 0, temp_results*10000)
        objective = np.zeros((ot.config.population_size))
        for i in range (len(ot.constraints)):
            objective = objective + temp_results[:,i+1]
        index_array = np.argsort(objective)
        sorted_population = population.T[index_array,:]
        sorted_results = results.T[index_array,:]
        return sorted_population[0:ot.config.population_size], sorted_results[0:ot.config.population_size]

    def check_convergence(self, ot:OptimizationTask):
        pass

    def plot_results(self, ot:OptimizationTask):
        pass

    def calculate_dresps(self,ot: OptimizationTask, population):
        #stress_results = np.array([])
        results = np.zeros((ot.config.population_size,1+len(ot.constraints)))
        i = 0
        for individual in population:
            self.change_input(individual, ot)
            ansys.runAPDL(scriptFilename=ot.solver_script,
                          ansyscall=ot.solver_path, workingdir=ot.work_path)
            with open(ot.results_path, encoding='utf-8') as f:
                lines = f.readlines()
            results[i, 0] = lines[0]
            results[i, 1] = lines[1]
            results[i, 2] = lines[0]
            i+=1
        return results



    def change_input(self, individual, ot: OptimizationTask):
        with open(ot.cae_model) as f:
            lines = f.readlines()
        lines[0] = "a="+ str(individual[0])+"\n"
        lines[1] = "b="+ str(individual[1])+"\n"
        with open(ot.cae_model, "w") as f:
            f.writelines(lines)




