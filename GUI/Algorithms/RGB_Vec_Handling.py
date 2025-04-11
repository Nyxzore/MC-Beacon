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

def random_vector_inside_hull(bIn):
    import Algorithms.in_hull as ih
    rand_vec = random_vector() 

    if bIn:
        while not ih.in_hull(rand_vec):
            rand_vec = random_vector() 
    else:
        while ih.in_hull(rand_vec):
            rand_vec = random_vector() 

    return rand_vec

def calculateBeamColor(glass_blocks):
    n = len(glass_blocks)

    summed_Vector = list(glass_blocks[0])
    for i in range(1,n):
        term = multiply_RGB_Vector(glass_blocks[i], 2**(i-1))
        summed_Vector = add_RGB_Vectors(summed_Vector, term) 

    new_Color = multiply_RGB_Vector(summed_Vector, (1/(2**(n-1))))
    return round_RGB_Vector(new_Color)