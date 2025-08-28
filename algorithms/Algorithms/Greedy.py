import random
import Algorithms.RGB_Vec_Handling as RGB
#This version will make use of a "max step alogrithm"
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

#time comp : (1)
def calc_beam_color(colour, current_beam_colour, n, i):
    if i == 0:
        weighted_vec = colour
    else:
        weighted_vec = RGB.multiply_RGB_Vector(colour, 2**(i-1))
    normalised_vec = RGB.multiply_RGB_Vector(weighted_vec, 2**(-n))
    summed_vec = RGB.add_RGB_Vectors(current_beam_colour, normalised_vec)
    return summed_vec


#time comp : (16n)
def find_glass_blocks(desired_color, n_desired_blocks):
    avail_colors = list(colourToRGB.values())
    current_beam_color = [0, 0, 0]
    glass_blocks = []

    for current_index in range(n_desired_blocks - 1, -1, -1):
        distances = []
        for color in avail_colors:
            temp_beam_color = calc_beam_color(color, current_beam_color, n_desired_blocks - 1, current_index)
            distances.append(RGB.VectorDistance(desired_color, temp_beam_color))
        
        min_dist = min(distances)
        best_color = avail_colors[distances.index(min_dist)]
        current_beam_color = calc_beam_color(best_color, current_beam_color, n_desired_blocks - 1, current_index)
        glass_blocks.append(best_color)

    return list(reversed(glass_blocks)), min_dist