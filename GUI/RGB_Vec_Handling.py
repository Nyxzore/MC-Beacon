import random

def multiply_RGB_Vector(vec, multiplier):
    vec = list(vec)
    for i in range(3):
        vec[i] = vec[i] * multiplier
    return vec

def VectorDistance(desired_Color, current_Color):
    d = (   (desired_Color[0] - current_Color[0])**2 + 
            (desired_Color[1] - current_Color[1])**2 + 
            (desired_Color[2] - current_Color[2])**2)**(1/2)
    return d

def add_RGB_Vectors(vec1, vec2):
    new_RGB_Vector = [0,0,0]
    for i in range(3):
        new_RGB_Vector[i] = vec1[i] + vec2[i]
    return new_RGB_Vector

def round_RGB_Vector(vec):
    for i in range(3):
        vec[i] = round(vec[i])
    return vec

def random_vector():
    random_vec = [0,0,0]
    for i in range(3):
        parameter = random.randrange(0,256)
        random_vec[i] = parameter
    return tuple(random_vec)
