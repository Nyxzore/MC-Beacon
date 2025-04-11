#searches half then half
import RGB_Vec_Handling as RGB
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

def calculateBeamColor(glassBlocks, n):
    #1/2^(n+1) (C_o + sum_{i=1}{n}2^(i-1)C_i)

    summed_Vector = list(glassBlocks[0])
    for i in range(1,len(glassBlocks)):
        term = RGB.multiply_RGB_Vector(glassBlocks[i], 2**(i-1))
        summed_Vector = RGB.add_RGB_Vectors(summed_Vector, term) 

    new_Color = RGB.multiply_RGB_Vector(summed_Vector, (1/(2**(n-1))))
    return RGB.round_RGB_Vector(new_Color)

def IndexToRGB(Indx):
    RGBList = list(colourToRGB.values())
    return RGBList[Indx]

def getNextPermutation(currentPerm):
    start = -len(currentPerm)
    c = list(currentPerm)
    c[-1] += 1
    for i in range(-1,start - 1, -1):
        if c[i] > 15:
            c[i]=0
            if i != start:
                c[i-1] += 1
    return (c)

def ComputeAllCombinationsOfOrder(n):
    initColorOrder = [0,]*n
    OrderList = [(initColorOrder)]
    NewOrder = None
    while NewOrder != [15,]*n:
        NewOrder = getNextPermutation(OrderList[-1])
        OrderList.append(NewOrder)
    

    #converts the list from indexes to RGB
    for i in range(len(OrderList)):
        for j in range(len(OrderList[0])):
            currentIndx = OrderList[i][j]
            OrderList[i][j] = IndexToRGB(currentIndx)
    return OrderList
    desired_rgb_color = RGB_vec

    colorList, vector_distance_list = calcBeamColorAndMatch(OrderList, desired_rgb_color)

    #determine max
    min_dist = min(vector_distance_list)
    maxIndex = vector_distance_list.index(min_dist)
    
    bestOrder = OrderList[maxIndex]
    #bestOrder = [rgbToColour[color] for color in bestOrder]
    return bestOrder, min_dist #returns ["colourName", "colourName", "colourName"], 0.xxxxx

def PermuationToColours(perm_list, n):
    colour_list = []
    for perms in perm_list:
        colour = calculateBeamColor(perms,n)
        colour_list.append(colour)
    return colour_list

import math
def Main(n, desired_rgb):
    halfway_index = math.floor(n/2)
    avail_perms_at_halfway = ComputeAllCombinationsOfOrder(halfway_index)
    avail_colours_at_halfway = PermuationToColours(avail_perms_at_halfway, halfway_index)

    distances = []
    for colour in avail_colours_at_halfway:
        dist = RGB.VectorDistance(desired_rgb, colour)
        distances.append(dist)
    min_dist = min(distances)
    min_perm = avail_perms_at_halfway[distances.index(min_dist)]
    # now we have (x),(x),(x),(x) + (),(),()
    extentions = ComputeAllCombinationsOfOrder(n-halfway_index)
    full_list = [min_perm + item for item in extentions]

    total_colours = PermuationToColours(full_list, n)

    distances = []
    for colour in total_colours:
        dist = RGB.VectorDistance(desired_rgb, colour)
        distances.append(dist)
    min_dist = min(distances)
    min_perm = full_list[distances.index(min_dist)]
    return min_perm, min_dist

for j in range(5):
    for i in range(1678):
        distances = []
        desired_rgb = RGB.random_vector()
        perm, dist = Main(2, desired_rgb)
        distances.append(dist)

    print(sum(distances)/len(distances))

#41.7851648315523, 14.89966442575134, 57.62811813689564, 23.366642891095847, 5.385164807134504#2
#27.748873851023216, 29.698484809834994, 71.76350047203663, 48.518037882832814, 79.5298686029343 #3
#10.295630140987, 20.322401432901575, 31.064449134018133, 34.87119154832539, 18.0 #4
#76.66159403508382, 7.54983443527075, 45.574115460423364, 1.0, 7.810249675906654 #5
#19.026297590440446, 63.31666447310692, 25.65151067676132, 36.0416425818802, 7.0710678118654755 #6