import Algorithms.Brute_Force as BRUTE_FROCE
import Algorithms.Greedy as GREEDY
import Algorithms.Greedy_Leaderboard as LGREEDY
import Algorithms.GA as GENTETIC
import Algorithms.Naive_SA as SA
import Algorithms.in_hull as ih

from Algorithms.RGB_Vec_Handling import random_vector_inside_hull, random_vector
import math, statistics
import matplotlib.pyplot as plt
import numpy as np


global sample_space, num_tests, num_blocks
sample_space = 1678 #math.ceil(256**3 * 0.0001)
num_tests = 5
num_blocks = 5


def calculate_ave_distance_BRUTEFORCE(inside_hull):
    for block_num in range(1, 4):
        average_disances = []
        for tests in range(num_tests):
            distance_sum = 0
            for i in range(sample_space):
                if inside_hull != None:
                    desired_RGB = random_vector_inside_hull(inside_hull)
                else : desired_RGB = random_vector()
                glass_blocks, min_dist = BRUTE_FROCE.FindGlassBlocks(block_num, desired_RGB, BRUTE_FROCE.ComputeAllColoursOfOrder(block_num))
                distance_sum += min_dist
            average_disance = distance_sum / sample_space
            average_disances.append(average_disance)
                
        ave_ave = round(statistics.mean(average_disances), 2)
        std_deviation = round(statistics.stdev(average_disances),3)
        print(block_num, ave_ave, std_deviation, average_disances)


def calculate_ave_distance_GREEDY(inside_hull):
    for block_num in range(1,6):
        average_disances = []
        for tests in range(num_tests):
            distance_sum = 0
            for i in range(sample_space):
                if inside_hull != None:
                    desired_RGB = random_vector_inside_hull(inside_hull)
                else : desired_RGB = random_vector()
                glass_blocks, min_dist = GREEDY.find_glass_blocks(desired_RGB, block_num)
                distance_sum += min_dist

            average_disance = distance_sum / sample_space
            average_disances.append(average_disance)
            
        ave_ave = round(statistics.mean(average_disances), 2)
        std_deviation = round(statistics.stdev(average_disances),3)
        print(block_num, ave_ave, std_deviation, average_disances)

def calculate_ave_distance_GREEDY_LEADERBOARD(inside_hull):
    for block_num in range(1,6):
        average_disances = []
        for tests in range(num_tests):
            distance_sum = 0
            for i in range(sample_space):
                if inside_hull != None:
                    desired_RGB = random_vector_inside_hull(inside_hull)
                else : desired_RGB = random_vector()
                glass_blocks, min_dist = LGREEDY.find_glass_blocks_top16(desired_RGB, block_num)
                distance_sum += min_dist

            average_disance = distance_sum / sample_space
            average_disances.append(average_disance)
            
        ave_ave = round(statistics.mean(average_disances), 2)
        std_deviation = round(statistics.stdev(average_disances),3)
        print(block_num, ave_ave, std_deviation, average_disances)

def calculate_ave_distance_GA(inside_hull):
    for block_num in range(10,11):
        average_disances = []
        for tests in range(num_tests):
            distance_sum = 0
            for i in range(sample_space):
                if inside_hull != None:
                    desired_RGB = random_vector_inside_hull(inside_hull)
                else : desired_RGB = random_vector()
                glass_blocks, min_dist = GENTETIC.genetic_algorithm(block_num, desired_RGB, epochs=10, population_size=1678)
                distance_sum += min_dist
            average_disance = distance_sum / sample_space
            average_disances.append(average_disance)
                
            
        ave_ave = round(statistics.mean(average_disances), 2)
        std_deviation = round(statistics.stdev(average_disances),3)
        print(block_num, ave_ave, std_deviation, average_disances, ave_ave)

def calculate_ave_distance_NSA(inside_hull):
    for block_num in range(1,6):
        average_disances = []
        for tests in range(num_tests):
            distance_sum = 0
            for i in range(sample_space):
                if inside_hull != None:
                    desired_RGB = random_vector_inside_hull(inside_hull)
                else : desired_RGB = random_vector()
                glass_blocks, min_dist = SA.anneal_to_(block_num, desired_RGB)
                distance_sum += min_dist
            average_disance = distance_sum / sample_space
            average_disances.append(average_disance)
                
            
        ave_ave = round(statistics.mean(average_disances), 2)
        std_deviation = round(statistics.stdev(average_disances),3)
        print(block_num, ave_ave, std_deviation, average_disances, ave_ave)
    
#calculate_ave_distance_BRUTEFORCE(inside_hull=True)
#calculate_ave_distance_BRUTEFORCE(inside_hull=False)
#calculate_ave_distance_BRUTEFORCE(inside_hull=None)

#calculate_ave_distance_GREEDY(inside_hull=True)
#calculate_ave_distance_GREEDY(inside_hull=False)
#calculate_ave_distance_GREEDY(None)

#calculate_ave_distance_GREEDY_LEADERBOARD(inside_hull=True)
#calculate_ave_distance_GREEDY_LEADERBOARD(inside_hull=False)
#calculate_ave_distance_GREEDY_LEADERBOARD(None)

#calculate_ave_distance_GA(inside_hull=True)
#calculate_ave_distance_GA(inside_hull=False)
#calculate_ave_distance_GA(None)

#calculate_ave_distance_NSA(inside_hull=True) 
#calculate_ave_distance_NSA(inside_hull=False)
#calculate_ave_distance_NSA(None)


def percentage_in_hull():
    inhull = 0
    outhull = 0
    sample_size = 0

    points_in = []
    points_out = []

    for R in range(0, 256, 8):
        print(R)
        for G in range(0, 256, 8):
            for B in range(0, 256, 8):
                colour = (R, G, B)
                if ih.in_hull(colour):
                    inhull += 1
                    points_in.append((R, G, B))
                else:
                    outhull += 1
                    points_out.append((R, G, B))
                sample_size += 1

    points_in = np.array(points_in)
    points_out = np.array(points_out)

    def plot():
        # Plotting function
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        fig.patch.set_facecolor(np.array([32,34,37])/255)
        ax.set_facecolor(np.array([32,34,37])/255)

        ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        ax.zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        ax.xaxis._axinfo["grid"]['color'] = (0.5, 0.5, 0.5, 0.2)
        ax.yaxis._axinfo["grid"]['color'] = (0.5, 0.5, 0.5, 0.2)
        ax.zaxis._axinfo["grid"]['color'] = (0.5, 0.5, 0.5, 0.2)
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.zaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.tick_params(axis='z', colors='white')

        if len(points_in) > 0:
            ax.scatter(points_in[:, 0], points_in[:, 1], points_in[:, 2], c='white', s=5, label="In Hull")

        ax.set_xlabel("Red")
        ax.set_ylabel("Green")
        ax.set_zlabel("Blue")
        ax.legend()

        plt.show()
    plot()
    print(inhull, outhull, sample_size) #5043528 11733688 16777216


def rim_of_hull():
    with open("output.txt", "w") as f:
        f.write("R,G,B\n") 

    for R in range(256):
        print(R/256 * 100)
        for G in range(256):
            for B in range(256):
                if ih.in_hull((R,B,G)):
                    neighbours_in_hull = 0
                    for dr in [-1, 0, 1]:
                        for dg in [-1, 0, 1]:
                            for db in [-1, 0, 1]:
                                if dr == 0 and dg == 0 and db == 0:
                                    continue  # Skip the center point (R, G, B) itself
                                if ih.in_hull((R + dr, G + dg, B + db)):
                                    neighbours_in_hull += 1

                        if neighbours_in_hull != 0 and neighbours_in_hull != 26:
                            with open("output.txt", "a") as f:
                                f.write(f"{R},{G},{B}\n")
rim_of_hull()

def avg_dist_outside_hull():
    distances= []
    for R in range(256):
        print(R/256 * 100)
        for G in range(256):
            print(G)
            for B in range(256):
                colour = (R,G,B)
                if ih.in_hull(colour) == False:
                    distance = ih.min_distance_to_hull(colour)
                    distances.append(distance)

    print(sum(distances)/len(distances))