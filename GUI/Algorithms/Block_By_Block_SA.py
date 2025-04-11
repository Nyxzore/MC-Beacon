import Algorithms.RGB_Vec_Handling as RGB
#This version will make use of a "max step alogrithm"
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

#annealing
import random, math
from copy import deepcopy


def anneal(desired_color, current_solution):
    current_solution.append(random.choice(list(colourToRGB.values())))
    temp=100
    threshold = 1

    def f(glass_block_list):

        distance = RGB.VectorDistance(desired_color,  RGB.calculateBeamColor(glass_block_list))
        return distance

    while temp > threshold:
        neighbour = deepcopy(current_solution)
        neighbour[random.randrange(0, len(current_solution)-1)]= random.choice(list(colourToRGB.values()))
        change = f(neighbour) - f(current_solution)

        if change < 0:
            current_solution = neighbour
        else:
            p_acceptance = math.exp(-change/temp)
            random_test = random.uniform(0,1)
            if random_test < p_acceptance:
                current_solution = neighbour
        #update temp1
        temp = temp*0.95
    return current_solution

def anneal_to_(n, desired_vec):
    init_solution = []
    for i in range(n):
        init_solution.append(random.choice(list((colourToRGB.values()))))
    solution = anneal(desired_vec, init_solution) #255,255,255
    dist = RGB.VectorDistance(desired_vec, RGB.calculateBeamColor(solution))
    return solution, dist