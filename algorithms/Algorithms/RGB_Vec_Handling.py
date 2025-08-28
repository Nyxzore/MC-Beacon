import random

#time comp: O(1)
def multiply_RGB_Vector(vec, multiplier):
    vec = list(vec)
    for i in range(3):
        vec[i] = vec[i] * multiplier
    return vec

#time comp: O(1)
def VectorDistance(desired_Color, current_Color):
    d = (   (desired_Color[0] - current_Color[0])**2 + 
            (desired_Color[1] - current_Color[1])**2 + 
            (desired_Color[2] - current_Color[2])**2)**(1/2)
    return d

#time comp: O(1)
def add_RGB_Vectors(vec1, vec2):
    new_RGB_Vector = [0,0,0]
    for i in range(3):
        new_RGB_Vector[i] = vec1[i] + vec2[i]
    return new_RGB_Vector

#time comp: O(1)
def round_RGB_Vector(vec):
    for i in range(3):
        vec[i] = round(vec[i])
    return vec

#time comp: O(1)
def random_vector():
    random_vec = [0,0,0]
    for i in range(3):
        parameter = random.randrange(0,256)
        random_vec[i] = parameter
    return tuple(random_vec)

#time comp: O(?)
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

#time comp: O(n)
def calculateBeamColor(glass_blocks):
    n = len(glass_blocks)

    summed_Vector = list(glass_blocks[0])
    for i in range(1,n):
        term = multiply_RGB_Vector(glass_blocks[i], 2**(i-1))
        summed_Vector = add_RGB_Vectors(summed_Vector, term) 

    new_Color = multiply_RGB_Vector(summed_Vector, (1/(2**(n-1))))
    return round_RGB_Vector(new_Color)

#time comp: O(1)
def perceptual_error(desired_RGB, current_RGB):
    Rsr = (desired_RGB[0] + current_RGB[0])/2

    ErrRed = desired_RGB[0] - current_RGB[0]
    ErrGreen = desired_RGB[1] - current_RGB[1]
    ErrBlue = desired_RGB[2] - current_RGB[2]

    return ((2+Rsr/256)*(ErrRed**2)+4*ErrGreen**2+(2+(255-Rsr)/256)*ErrBlue**2)**(1/2)