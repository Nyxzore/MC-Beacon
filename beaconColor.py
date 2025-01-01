#reference to all the rgb vectors available in mc
colourToRGB = {
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

    summed_Vector = [0,0,0]
    for i in range(1,n):
        term = multiply_RGB_Vector(glassBlocks[i], 2**(i-1))
        summed_Vector = add_RGB_Vectors(summed_Vector, term) 

    new_Color = multiply_RGB_Vector(add_RGB_Vectors(glassBlocks[0] , summed_Vector), (1/(2**(n+1))))
    return round_RGB_Vector(new_Color)

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

def percentage_Match(desired_Color, current_Color):
    error= []
    for i in range(3):
        error.append(abs(current_Color[i] - desired_Color[i]) / 256) # distance off
    
    ave_error = sum(error)/3
    return (1 - ave_error)

def ComputeAllColoursOfOrder(n, desired_Color):
    initColorOrder = [0,]*n
    OrderList = [(initColorOrder)]
    NewOrder = None
    while NewOrder != [15,]*n:
        NewOrder = getNextPermutation(OrderList[-1])
        OrderList.append(NewOrder)
    
    #converts the list from indexes to RGB
    percentage_Match_List = []
    for i in range(len(OrderList)):
        for j in range(len(OrderList[0])):
            currentIndx = OrderList[i][j]
            OrderList[i][j] = IndexToRGB(currentIndx)
        #calculating percentages in this loop to save on computation
        beamColor = calculateBeamColor(OrderList[i])
        OrderList[i] = beamColor
        percentage_Match_List.append(percentage_Match(desired_Color, beamColor))
    return OrderList, percentage_Match_List

with open('output.txt', 'w') as file:
    OrderList, percentage_Match_List = ComputeAllColoursOfOrder(3, (58, 90, 64))
    for item in OrderList:
        file.write(f"{item}\n")

    print(max(percentage_Match_List))
    maxInx = percentage_Match_List.index(max(percentage_Match_List))
    bestOrderRGB = OrderList[maxInx]

# Convert each tuple to its corresponding color name

print(calculateBeamColor(((94, 124, 22), (22, 156, 156), (137, 50, 184))))

print("List saved to output.txt")
print(max)
#resources
#https://minecraft.fandom.com/wiki/Dye#Dyeing_armor
#https://www.checkyourmath.com/convert/color/decimal_rgb.php