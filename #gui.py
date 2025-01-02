#gui
#notes - use canvases to use transparent images along with Pillow

import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

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
    
    OrderList = ComputeAllColoursOfOrder(1)
    colorList, percentageMatchList = calcBeamColorAndMatch(OrderList, desired_rgb_color)

    maxMatch = max(percentageMatchList)
    maxIndex = percentageMatchList.index(maxMatch)

    #convert orderlist to names so its readable
    bestOrder = OrderList[maxIndex]
    for i in range(len(bestOrder)):
        bestOrder[i] = rgbToColour[bestOrder[i]]

    print(bestOrder, maxMatch)

btnCalc = ctk.CTkButton(master=root, text="Calculate", command=FindGlassBlocks)
btnCalc.pack(pady=10)

def on_enter(event, name):
    hover_label.configure(text=name)
    hover_label.place(x=event.x_root - root.winfo_rootx() + 10, y=event.y_root - root.winfo_rooty() + 10)

def on_leave(event):
    hover_label.place_forget()

#adding beacon png

order = ('red','blue','green','red','blue')
n = len(order)
img_length = 64
beacon_img = Image.open("beacon.png")
beacon_img = beacon_img.resize((img_length,img_length))
beacon_img = ImageTk.PhotoImage(beacon_img)

canvas = ctk.CTkCanvas(root, width=150,height=400, bg=root.cget("bg"), highlightthickness=0)
canvas.pack()
#place beacon img on canvas
beacon_item = canvas.create_image(80,260,image=beacon_img,anchor="s")
#beacon info
canvas.tag_bind(beacon_item, "<Enter>", lambda event: on_enter(event, "Beacon"))
canvas.tag_bind(beacon_item, "<Leave>", on_leave)


#hover event for beacon
hover_label = ctk.CTkLabel(root, text="", bg_color=root.cget("bg"), fg_color="black", corner_radius=5, padx=5, pady=5)
hover_label.place_forget()

#stained glass blocks
y =260-(img_length/1.85)
glass_block_images =[]
for color in order:
    glass_block_img = Image.open(f"glass_stained_blocks\{color}.png")
    glass_block_img = glass_block_img.resize((img_length,img_length))
    glass_block_img = ImageTk.PhotoImage(glass_block_img)
    glass_block_images.append(glass_block_img)
    #place glass img on canvas
    glass_item = canvas.create_image(80,y,image=glass_block_img, anchor="s")
    y -= img_length/1.85

    canvas.tag_bind(glass_item, "<Enter>", lambda event, color=color: on_enter(event, f"{color.capitalize()} Glass Block"))
    canvas.tag_bind(glass_item, "<Leave>", on_leave)

root.mainloop()