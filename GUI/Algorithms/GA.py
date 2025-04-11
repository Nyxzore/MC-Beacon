#roullette wheel selection
import Algorithms.RGB_Vec_Handling as RGB
import random
colourToRGB = {
    #reference to all the rgb vectors available in mc
    "white" : (249, 255, 254),
    "light_Gray" : (157, 157, 151),
    "gray" : (71, 79, 82),
    "black": (29, 29, 33),
    "brown": (131, 84, 50),
    "red": (176, 46, 38),
    "orange": (249, 128, 29),
    "yellow": (254, 216, 61),
    "lime": (128, 199, 31),
    "green": (94, 124, 22),
    "cyan": (22, 156, 156),
    "light_Blue": (58, 179, 218),
    "blue": (60, 68, 170),
    "purple": (137, 50, 184),
    "magenta": (199, 78, 189),
    "pink": (243, 139, 170)
}
rgbToColour = {value: key for key, value in colourToRGB.items()}  


def genetic_algorithm(desired_n_blocks, desired_rgb, epochs, population_size):
    #create an initial population
    def Random_Permuation(n_blocks):
        perm = []
        for i in range(n_blocks):
            perm.append(random.choice(list(colourToRGB.values())))
        return perm
    
    def calculate_distances(desired_rgb, population):
        distances = []
        for perm in population:
            dist = RGB.VectorDistance(desired_rgb, RGB.calculateBeamColor(perm))
            distances.append(dist) 
        return distances
    
    __init__population = []
    for i in range(population_size):
        __init__population.append(Random_Permuation(desired_n_blocks))

    def perform_evolution(current_generation):
        fitness_values = calculate_distances(desired_rgb, current_generation)
        total_sum = sum(fitness_values)
        flipped_weightings = [(total_sum-fitness)/total_sum for fitness in fitness_values] 
        total_sum = sum(flipped_weightings)
        propablistic_weightings = [weight/total_sum for weight in flipped_weightings]

        #apply probabilty distribution
        modified_generation = random.choices(current_generation, propablistic_weightings, k=population_size)
        #breeding
        for i in range(0, len(modified_generation)-1,2):
            #assuming population is even
            parent1 = modified_generation[i]
            parent2 = modified_generation[i+1]

            gene_splitting_point = random.randrange(0, desired_n_blocks)
            child1 = parent1[:gene_splitting_point] + parent2[gene_splitting_point:]
            child2 = parent2[:gene_splitting_point] + parent1[gene_splitting_point:]

            
            modified_generation[i] = child1
            modified_generation[i+1]= child2

        #mutation
        mutated_child = random.choice(modified_generation)
        mutated_child[random.randint(0, desired_n_blocks-1)] = random.choice(list(colourToRGB.values()))

        #return fitness individual of modified gen
        fitness_values = calculate_distances(desired_rgb, modified_generation)
        min_fit = min(fitness_values)
        min_indx = fitness_values.index(min_fit)
        return modified_generation[min_indx], modified_generation, min_fit
    
    absolute_best_dist = 9999999999
    absolute_best = ''
    for i in range(epochs):
        if i == 0: current_generation = __init__population
        else: current_generation = next_generation
        best_candidate, next_generation, fitness = perform_evolution(current_generation)
        if fitness < absolute_best_dist: 
            absolute_best = best_candidate
            absolute_best_dist = fitness
    
    return absolute_best, absolute_best_dist