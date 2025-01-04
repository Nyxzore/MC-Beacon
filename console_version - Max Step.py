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

def VectorDistance(desired_Color, current_Color):
    d = (   (desired_Color[0] - current_Color[0])**2 + 
            (desired_Color[1] - current_Color[1])**2 + 
            (desired_Color[2] - current_Color[2])**2)**(1/2)
    return d

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

def calcBeamColorAndMatch(OrderList, desired_Color):
    beam_Colors = []
    vector_distance_list = []
    for order in OrderList:
        newColor = calculateBeamColor(order)
        beam_Colors.append(newColor)

        d = VectorDistance(desired_Color, newColor)
        vector_distance_list.append(d)

    return beam_Colors, vector_distance_list

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

def FindGlassBlocks(n, RGB_vec):
    desired_rgb_color = RGB_vec
    
    OrderList = ComputeAllColoursOfOrder(n)
    colorList, vector_distance_list = calcBeamColorAndMatch(OrderList, desired_rgb_color)

    #determine max
    maxMatch = min(vector_distance_list)
    maxIndex = vector_distance_list.index(maxMatch)
    
    bestOrder = OrderList[maxIndex]
    bestOrder = [rgbToColour[color] for color in bestOrder]
    return bestOrder, maxMatch #returns ["colourName", "colourName", "colourName"], 0.xxxxx

rgb = []

import random
for n in range(1):
    for i in range(16589):
        rgb.append((random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)))

    #average
    dist_sum = 0
    minDistList = []
    for color in rgb:
        bestOrder, minDist = FindGlassBlocks(n+1, color)
        minDistList.append(minDist) # for standard deviation

    import matplotlib.pyplot as plt

    x = []
    for i in range(len(minDistList)):
        x.append(i)
    y = minDistList

    # Create scatter plot
    plt.scatter(x, y)

    # Add labels and title
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Scatter Plot Example')

    # Display the plot
    plt.show()
#https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/25/Beacon_JE6_BE2.png/revision/latest?cb=20241106154445
#https://www.youtube.com/watch?v=GMHtpH68Glo
#https://minecraft.fandom.com/wiki/Dye#Dyeing_armor
#https://www.checkyourmath.com/convert/color/decimal_rgb.php