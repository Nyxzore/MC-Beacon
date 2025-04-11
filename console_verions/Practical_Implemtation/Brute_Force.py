import RGB_Vec_Handling as RGB
#this approach is a brute force computation of all the colours made by n blocks and seeing which one is the least distance away
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

#time comp : O(1)
def IndexToRGB(Indx):
    RGBList = list(colourToRGB.values())
    return RGBList[Indx]

#time comp : O(n)
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

#time comp : O(n*16^n)
def ComputeAllColoursOfOrder(n):
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

#time comp : O(n*16^n)
def calcBeamColorAndMatch(OrderList, desired_Color):
    beam_Colors = []
    vector_distance_list = []
    for order in OrderList:
        newColor = RGB.calculateBeamColor(order)
        beam_Colors.append(newColor)

        d = RGB.perceptual_error(desired_Color, newColor)
        vector_distance_list.append(d)

    return beam_Colors, vector_distance_list

#time comp : O(n*16^n)
def FindGlassBlocks(n, RGB_vec, possible_permutations):
    desired_rgb_color = RGB_vec

    colorList, vector_distance_list = calcBeamColorAndMatch(possible_permutations, desired_rgb_color)

    #determine max
    min_dist = min(vector_distance_list)
    min_index = vector_distance_list.index(min_dist)
    
    bestOrder = possible_permutations[min_index]
    #bestOrder = [rgbToColour[color] for color in bestOrder]
    return bestOrder, min_dist #returns ["colourName", "colourName", "colourName"], 0.xxxxx

print(FindGlassBlocks(4, (33, 54, 35), ComputeAllColoursOfOrder(4)))