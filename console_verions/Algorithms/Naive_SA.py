import Algorithms.RGB_Vec_Handling as RGB
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
        #find neighbour
        def closest_vertex(current_rgb):
            distances = []
            for rgb in colourToRGB.values():
                distances.append(RGB.VectorDistance(current_rgb, rgb))
            min = sorted(distances)[1]
            return list(colourToRGB.values())[distances.index(min)]

        neighbour = deepcopy(current_solution)
        current_block =  neighbour[random.randrange(0, len(neighbour))]
        print(neighbour)
        neighbour[neighbour.index(current_block)] = closest_vertex(current_block)
        print(neighbour)

        change = f(neighbour) - f(current_solution)

        if change < 0:
            current_solution = neighbour
        else:
            p_acceptance = math.exp(-change/temp)
            random_test = random.uniform(0,1)
            if random_test < p_acceptance:
                current_solution = neighbour

        temp = temp*0.97
    return current_solution

def anneal_to_(n, desired_vec):
    current_solution = []
    for i in range(n):
        current_solution = anneal(desired_vec, current_solution) #255,255,255
        dist = RGB.VectorDistance(desired_vec, RGB.calculateBeamColor(current_solution))
    return current_solution, dist