#not my code at all
#https://stackoverflow.com/questions/16750618/whats-an-efficient-way-to-find-if-a-point-lies-in-the-convex-hull-of-a-point-cl
from scipy.spatial import ConvexHull, Delaunay
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

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

#ChatGPT model 4o
def min_distance_to_hull(test_point):
    """
    Find the shortest distance from a point to the convex hull.
    """
    # Loop through all faces (simplices) of the convex hull
    hull = ConvexHull(points)
    distances = []
    for simplex in hull.simplices:
        # Get the three points that define the face
        A, B, C = points[simplex]
        
        # Compute the normal to the plane defined by the simplex
        normal = np.cross(B - A, C - A)
        normal = normal / np.linalg.norm(normal)  # Normalize the normal
        
        # Compute perpendicular distance from the point to the plane
        distance = abs(np.dot(normal, test_point - A))  # Point to plane distance
        distances.append(distance)
    
    return min(distances)  

def plot(hull, test_point):
    # 3D plot setup
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Plot convex hull points in red
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color="r", label="Hull Points")

    # Plot convex hull edges
    for simplex in hull.simplices:
        simplex = np.append(simplex, simplex[0])  # Close the loop
        ax.plot(points[simplex, 0], points[simplex, 1], points[simplex, 2], "k-")

    # Plot test point in blue
    ax.scatter(test_point[:, 0], test_point[:, 1], test_point[:, 2], color="blue", s=20, label="Test Point")

    # Labels and legend
    ax.set_xlabel("R")
    ax.set_ylabel("B")
    ax.set_zlabel("G")
    ax.legend()

    # Show the plot
    plt.show()