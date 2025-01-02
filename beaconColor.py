
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

    summed_Vector = [0,0,0]
    for i in range(1,n):
        term = multiply_RGB_Vector(glassBlocks[i], 2**(i-1))
        summed_Vector = add_RGB_Vectors(summed_Vector, term) 

    colorSum = add_RGB_Vectors(glassBlocks[0] , summed_Vector)
    new_Color = multiply_RGB_Vector(colorSum, (1/(2**(n-1))))
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
    percentage_Match_List = []
    for order in OrderList:
        newColor = calculateBeamColor(order)
        beam_Colors.append(newColor)

        p = percentage_Match(desired_Color, newColor)
        percentage_Match_List.append(p)

    return beam_Colors, percentage_Match_List

#resources
#https://minecraft.fandom.com/wiki/Dye#Dyeing_armor
#https://www.checkyourmath.com/convert/color/decimal_rgb.php

#gui
import customtkinter as ctk
import tkinter as tk
from PIL import Image

root = ctk.CTk()
root.geometry("300x400")
root.title("Beacon Color Picker")

#hexadecimal
lblRed = ctk.CTkLabel(master=root, text="Hex Color")
lblRed.pack(pady = 10)
entPickColor = ctk.CTkEntry(master=root)
entPickColor.pack()

class HexColorToRGB():
    def HextoDecimal(HexCode):
        hex_Dict = {
            "0":0,
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "A":10,
            "B":11,
            "C":12,
            "D":13,
            "E":14,
            "F":15,
        }
        sum = 0
        for i in range(-1, -len(HexCode)-1, -1):
            sum += 16**(abs(i)-1) * hex_Dict[HexCode[i]]
        return sum
    
    def Main(HexColor):
        #RRGGBB
        RGBVect = [0,0,0]
        for i in range(1,4):
            CurrentElement = HexColor[-2*i+1] +HexColor[-2*i]
            RGBValue = HexColorToRGB.HextoDecimal(CurrentElement)
            RGBVect[-i] = RGBValue
        return RGBVect

def FindGlassBlocks():
    desired_color_hex = entPickColor.get()[1:]
    desired_rgb_color = HexColorToRGB.Main(desired_color_hex)
    desired_rgb_color = (29, 56, 32)
    OrderList = ComputeAllColoursOfOrder(6)
    colorList, percentageMatchList = calcBeamColorAndMatch(OrderList, (desired_rgb_color))

    maxMatch = max(percentageMatchList)
    maxIndex = percentageMatchList.index(maxMatch)

    #convert orderlist to names so its readable
    bestOrder = OrderList[maxIndex]
    for i in range(len(bestOrder)):
        bestOrder[i] = rgbToColour[bestOrder[i]]

    print(bestOrder, maxMatch)

btnCalc = ctk.CTkButton(master=root, text="Calculate", command=FindGlassBlocks)
btnCalc.pack(pady=10)

#adding beacon png

beacon_img = ctk.CTkImage(light_image=Image.open("beacon.png"), dark_image=Image.open("beacon.png"), size=((64,64)))
beacon_lbl = ctk.CTkLabel(root, text="", image=beacon_img)
beacon_lbl.pack(side="bottom")
root.mainloop()

#https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/25/Beacon_JE6_BE2.png/revision/latest?cb=20241106154445
#https://www.youtube.com/watch?v=GMHtpH68Glo