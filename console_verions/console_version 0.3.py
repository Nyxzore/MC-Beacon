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

class VectorHandling():
    @staticmethod
    def multiply_RGB_Vector(vec, multiplier):
        vec = list(vec)
        for i in range(3):
            vec[i] = vec[i] * multiplier
        return vec
    @staticmethod
    def VectorDistance(desired_Color, current_Color):
        d = (   (desired_Color[0] - current_Color[0])**2 + 
                (desired_Color[1] - current_Color[1])**2 + 
                (desired_Color[2] - current_Color[2])**2)**(1/2)
        return d
    @staticmethod
    def add_RGB_Vectors(vec1, vec2):
        new_RGB_Vector = [0,0,0]
        for i in range(3):
            new_RGB_Vector[i] = vec1[i] + vec2[i]
        return new_RGB_Vector
    @staticmethod
    def round_RGB_Vector(vec):
        for i in range(3):
            vec[i] = round(vec[i])
        return vec

def calculateBeamColor(glassBlocks):
    #1/2^(n+1) (C_o + sum_{i=1}{n}2^(i-1)C_i)
    n = len(glassBlocks)

    summed_Vector = list(glassBlocks[0])
    for i in range(1,n):
        term = VectorHandling.multiply_RGB_Vector(glassBlocks[i], 2**(i-1))
        summed_Vector = VectorHandling.add_RGB_Vectors(summed_Vector, term) 

    new_Color = VectorHandling.multiply_RGB_Vector(summed_Vector, (1/(2**(n-1))))
    return VectorHandling.round_RGB_Vector(new_Color)
#annealing
import random, math
from copy import deepcopy

def anneal(desired_color, current_solution):
    current_solution.append(random.choice(list(colourToRGB.values())))
    temp=100
    threshold = 0.0000000000001

    def f(glass_block_list):
        distance = VectorHandling.VectorDistance(desired_color,  calculateBeamColor(glass_block_list))
        return distance

    while temp > threshold:
        neighbour = deepcopy(current_solution)
        neighbour[-1]= random.choice(list(colourToRGB.values()))
        change = f(neighbour) - f(current_solution)

        if change < 0:
            current_solution = neighbour
        else:
            p_acceptance = math.exp(-change/temp)
            random_test = random.uniform(0,1)
            if random_test < p_acceptance:
                current_solution = neighbour
        #update temp
        temp = temp*0.95
    return current_solution

def anneal_to_(n):
    current_solution = []
    for i in range(n):
        current_solution = anneal( (213, 174, 249), current_solution) #255,255,255
    return current_solution

print(anneal_to_(5))