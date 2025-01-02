import customtkinter as ctk
from tkinter import Canvas, Label
from PIL import Image, ImageTk, ImageDraw
import colorsys

# Initialize the main window
root = ctk.CTk()
root.geometry("400x500")
root.title("Color Wheel Picker")

# Function to create a color wheel image
def create_color_wheel(size):
    wheel = Image.new("RGB", (size, size))
    draw = ImageDraw.Draw(wheel)

    for x in range(size):
        for y in range(size):
            dx, dy = x - size / 2, y - size / 2
            distance = (dx**2 + dy**2) ** 0.5

            if distance <= size / 2:
                angle = (180 + (180 / 3.14159) * -1 * (dy / (dx + 1e-6))) % 360
                r, g, b = colorsys.hsv_to_rgb(angle / 360, distance / (size / 2), 1)
                draw.point((x, y), fill=(int(r * 255), int(g * 255), int(b * 255)))

    return wheel

# Create the color wheel image
wheel_size = 300
color_wheel_image = create_color_wheel(wheel_size)

# Tkinter Canvas to display the color wheel
canvas = Canvas(root, width=wheel_size, height=wheel_size)
canvas.pack(pady=20)
color_wheel_tk = ImageTk.PhotoImage(color_wheel_image)
canvas.create_image(0, 0, anchor="nw", image=color_wheel_tk)

# Label to display the selected color
selected_color_label = Label(root, text="Selected Color: #FFFFFF", bg="#FFFFFF", fg="#000000", font=("Arial", 16))
selected_color_label.pack(pady=10)

# Function to handle mouse clicks on the color wheel
def pick_color(event):
    x, y = event.x, event.y
    if 0 <= x < wheel_size and 0 <= y < wheel_size:
        rgb = color_wheel_image.getpixel((x, y))
        color_hex = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        selected_color_label.configure(text=f"Selected Color: {color_hex}", bg=color_hex)

# Bind the color picker function to mouse clicks
canvas.bind("<Button-1>", pick_color)

root.mainloop()