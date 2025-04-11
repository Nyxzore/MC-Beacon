#not my code at all
#https://stackoverflow.com/questions/16750618/whats-an-efficient-way-to-find-if-a-point-lies-in-the-convex-hull-of-a-point-cl
from scipy.spatial import ConvexHull, Delaunay
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import Algorithms.Brute_Force as BRUTE_FROCE
import Algorithms.Greedy as GREEDY
import Algorithms.GA as GENTETIC
import Algorithms.Naive_SA as SA


# Define points
points = np.array([
    [249, 255, 254],
    [157, 157, 151],
    [71, 79, 82],
    [29, 29, 33],
    [131, 84, 50],
    [176, 46, 38],
    [249, 128, 29],
    [254, 216, 61],
    [128, 199, 31],
    [94, 124, 22],
    [22, 156, 156],
    [58, 179, 218],
    [60, 68, 170],
    [137, 50, 184],
    [199, 78, 189],
    [243, 139, 170]
])

# Compute convex hull


# Function to check if a point is inside the convex hull
def in_hull(p):
    """
    Test if points in `p` are in `hull`.

    `p` should be a `NxK` array of coordinates for `N` points in `K` dimensions.
    `hull` should be a `scipy.spatial.ConvexHull` object.
    """
    p = np.array(p)
    hull = ConvexHull(points)
    hull_delaunay = Delaunay(hull.points)
    return hull_delaunay.find_simplex(p) >= 0


def plot(hull, desired_rgb, fig, ax):

    ax.clear()
    all_points.append(desired_rgb)
    # Set dark background
    fig.patch.set_facecolor(np.array([32,34,37])/255)  # Figure background
    ax.set_facecolor(np.array([32,34,37])/255)         # Axes background

    # Customize axis and label colors
    ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))  # Transparent pane
    ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))  # Transparent pane
    ax.zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))  # Transparent pane
    ax.xaxis._axinfo["grid"]['color'] = (0.5, 0.5, 0.5, 0.2)  # Grid color
    ax.yaxis._axinfo["grid"]['color'] = (0.5, 0.5, 0.5, 0.2)  # Grid color
    ax.zaxis._axinfo["grid"]['color'] = (0.5, 0.5, 0.5, 0.2)  # Grid color
    ax.xaxis.label.set_color('white')  # X-axis label color
    ax.yaxis.label.set_color('white')  # Y-axis label color
    ax.zaxis.label.set_color('white')  # Z-axis label color
    ax.tick_params(axis='x', colors='white')  # X-axis tick color
    ax.tick_params(axis='y', colors='white')  # Y-axis tick color
    ax.tick_params(axis='z', colors='white')  # Z-axis tick color

    # Plot convex hull points with RGB colors
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=points/255, marker='o', s=40)

    # Plot convex hull edges
    for simplex in hull.simplices:
        simplex = np.append(simplex, simplex[0])  # Close the loop
        ax.plot(points[simplex, 0], points[simplex, 1], points[simplex, 2], "w-")  # White edges

    # Plot test point in blue
    ax.scatter(desired_rgb[:, 0], desired_rgb[:, 1], desired_rgb[:, 2], color=desired_rgb/255, s=150, label='Desired Colour')

    # Labels and legend
    ax.set_xlabel("R")
    ax.set_ylabel("B")
    ax.set_zlabel("G")
    ax.legend(facecolor='black', labelcolor='white')  # Customize legend colors
    plt.draw()

import tkinter as tk
from tkinter import *
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Tkinter application
def create_gui():
    global all_points
    all_points = []

    root = tk.Tk()
    root.title("3D RGB Plot in Tkinter")
    root.configure(bg = '#202225')
    main  = Label(root, text = 'Beacon Colour Picker', bg = '#202225', fg= 'white', font=('Times new roman', 30))
    main.grid(row=0, column=0, columnspan=3)

    #input
    def on_enter_desired_colour(event):
        desired_rgb = desired_colour_box.get()
        desired_rgb = [int(x) for x in desired_rgb.split(',')]
        desired_rgb =  np.array(desired_rgb).reshape(1, -1)
        plot(hull, desired_rgb, fig, ax)
        desired_n.focus()

    def on_enter_n_blocks(event):
        n_blocks = int(desired_n.get())
        desired_rgb = desired_colour_box.get()
        desired_rgb = [int(x) for x in desired_rgb.split(',')]

        distances = Text(root, bg='#202225', fg='white', width=20, height=15)
        distances.grid(row=6, column=0, padx=10, pady=10)

        permuations = Text(root, bg='#202225', fg='white', width=100, height=15)
        permuations.grid(row=35, column=0, columnspan=3, padx=10, pady=10)


        def RGB_to_Colour(Order):
            new_order = [BRUTE_FROCE.rgbToColour[rgb] for rgb in Order]
            return new_order

        if n_blocks < 5:
            order, dist = BRUTE_FROCE.FindGlassBlocks(n_blocks, desired_rgb, BRUTE_FROCE.ComputeAllColoursOfOrder(n_blocks))
            distances.insert(tk.END, 'Brute Force: ' + str(round(dist,2))+ '\n')
            permuations.insert(tk.END, 'Brute Force: ' + str(RGB_to_Colour(order)) + '\n'*2)
        else:
            distances.insert(tk.END, 'Brute Force: ' + '?' + '\n')
            permuations.insert(tk.END, 'Brute Force: ' + 'Too time complex' + '\n'*2)

        order, dist = GREEDY.find_glass_blocks(n_blocks, desired_rgb)
        distances.insert(tk.END, 'Greedy: ' + str(round(dist,2))+ '\n')
        permuations.insert(tk.END, 'Greedy: ' + str(RGB_to_Colour(order)) + '\n'*2)

        order, dist = SA.anneal_to_(n_blocks, desired_rgb)
        distances.insert(tk.END, 'Naive SA: ' + str(round(dist,2)) + '\n')
        permuations.insert(tk.END, 'Naive SA: '+ str(RGB_to_Colour(order)) + '\n'*2)

        order, dist = GENTETIC.genetic_algorithm(n_blocks, desired_rgb, 20, 1678)
        distances.insert(tk.END, 'Gentetic: ' + str(round(dist,2)) + '\n')
        permuations.insert(tk.END, 'Gentetic: ' + str(RGB_to_Colour(order)) + '\n'*2)


    desired_colour_box_Label = Label(root, bg='#202225', fg='white', text = 'Desired RGB Colour')
    desired_colour_box_Label.grid(row=2, column=0, padx=20)
    desired_colour_box = Entry(root, bg='#17181a', fg='white')
    desired_colour_box.grid(row=3, column=0, padx=20)
    desired_colour_box.bind('<Return>', on_enter_desired_colour)

    desired_n_label = Label(root, bg='#202225', fg='white', text='Number of blocks: ')
    desired_n_label.grid(row=4, column=0, padx=20)
    desired_n = Entry(root, bg='#17181a', fg='white')
    desired_n.grid(row=5, column=0, padx=20)
    desired_n.bind('<Return>', on_enter_n_blocks)

    # Beacon 
    #Beaconframe = ttk.Frame(root)
    #Beaconframe.grid(row=1, column=1, rowspan=20,  padx=10, pady=10)

    #MPL PLOT
    # Create a frame for the plot

    Hullframe = ttk.Frame(root)
    Hullframe.grid(row=1, column=2, rowspan=20,  padx=10, pady=10)

    # Create a Matplotlib figure and axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Embed the Matplotlib figure in the Tkinter frame
    canvas = FigureCanvasTkAgg(fig, master=Hullframe)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Example data
    test_point = np.array([128, 128, 128]).reshape(1, -1)

    # Compute convex hull/home/nysxzore/Desktop/mc_beacon_optimisation/helper_functions/in_hull.py
    hull = ConvexHull(points)

    # Plot the data
    plot(hull, test_point, fig, ax)
    # Run the Tkinter main loop
    root.mainloop()

create_gui()