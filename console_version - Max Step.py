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
def multiply_RGB_Vector(color, multiplier):
    color = list(color)
    for i in range(3):
        color[i] = color[i] * multiplier
    return color

def add_RGB_Vectors(vec1, vec2):
    new_RGB_Vector = [0,0,0]
    for i in range(3):
        new_RGB_Vector[i] = vec1[i] + vec2[i]
    return new_RGB_Vector

def round_RGB_Vector(vec):
    for i in range(3):
        vec[i] = round(vec[i])
    return vec

def calculateBeamColor(glassBlocks):
    #1/2^(n+1) (C_o + sum_{i=1}{n}2^(i-1)C_i)
    n = len(glassBlocks)

    summed_Vector = list(glassBlocks[0])
    for i in range(1,n):
        term = multiply_RGB_Vector(glassBlocks[i], 2**(i-1))
        summed_Vector = add_RGB_Vectors(summed_Vector, term) 

    new_Color = multiply_RGB_Vector(summed_Vector, (1/(2**(n-1))))
    return round_RGB_Vector(new_Color)

def VectorDistance(desired_Color, current_Color):
    d = (   (desired_Color[0] - current_Color[0])**2 + 
            (desired_Color[1] - current_Color[1])**2 + 
            (desired_Color[2] - current_Color[2])**2)**(1/2)
    return d

class HexColorToRGB():
    def HextoDecimal(HexCode):
        HexCode = HexCode.strip("#")
        hex_Dict = {
            "0":0,"1":1,"2":2,"3":3,"4":4,
            "5":5,"6":6,"7":7,"8":8,"9":9,
            "A":10,"B":11,"C":12,"D":13,"E":14,"F":15,
            "a":10,"b":11,"c":12,"d":13,"e":14,"f":15,
        }
        sum = 0
        for i in range(-1, -len(HexCode)-1, -1):
            sum += 16**(abs(i)-1) * hex_Dict[HexCode[i]]
        return sum
    
    def Main(HexColor):
        #RRGGBB
        RGBVect = [0,0,0]
        for i in range(1,4):
            CurrentElement = HexColor[-2*i] + HexColor[-2*i+1]
            RGBValue = HexColorToRGB.HextoDecimal(CurrentElement)
            RGBVect[-i] = RGBValue
        return RGBVect

def get_children(initial_vector, index_in_sum, n):
    if index_in_sum == 0:
        weighting = 1/(2**n)
    else:
        weighting = 2**(index_in_sum-1) / (2**n) 

    print(weighting)
    children = []
    available_rgb_vectors = list(colourToRGB.values())
    for vectors in available_rgb_vectors:
        children.append(add_RGB_Vectors(multiply_RGB_Vector(vectors, weighting), initial_vector))

    return children

def get_children_distance(desired_Color, current_options):
    distance_list = []
    for colour in current_options:
        distance_list.append(VectorDistance(desired_Color, colour))
    return distance_list


def FindGlassBlocks(n):
    desired_rgb_color = [58,89,54]
    __init__colour = [0,0,0]
    reversed_best_stained_glass_order = []
    for i in range(n,-1,-1):
        currentOptions = get_children(__init__colour, i, n)
        distance_of_current_options = get_children_distance(desired_rgb_color, currentOptions)
        #choose child with min distance from desired colour
        min_Distance = min(distance_of_current_options)
        min_Dist_Index = distance_of_current_options.index(min_Distance)
        bestOption = currentOptions[min_Dist_Index]

        Glass_Block_Names = list(colourToRGB.keys())
        best_stained_glass = Glass_Block_Names[min_Dist_Index]
        reversed_best_stained_glass_order.append(best_stained_glass)

        __init__colour = bestOption
        #reverse list
    return list(reversed(reversed_best_stained_glass_order))

n = 4 #n=number of glass blocks -1
best_stained_glass_order = FindGlassBlocks(n)
print(best_stained_glass_order)