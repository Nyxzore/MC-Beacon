from manim import *
class ConvexHullExample(ThreeDScene):
    def construct(self):
        # Define points as a list of coordinate tuples
        ax = ThreeDAxes(
            x_range=[0,300,50],
            y_range=[0,300,50],
            z_range=[0,300,50],
            x_length=8,
            y_length=8,
            z_length=8,
        ).add_coordinates().center()
        self.add(ax)
        self.set_camera_orientation(phi=75 * DEGREES, theta= -30 * DEGREES)
        points = [
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
        ]
        cpts = [ax.c2p(*p) for p in points]
        hull = ConvexHull3D(
            *cpts,
            faces_config = {"stroke_opacity": 0.05, "color": WHITE},
            graph_config = {
                "vertex_type": Dot3D,
                "edge_config": {
                    "stroke_color": WHITE,
                    "stroke_width": 2,
                    "stroke_opacity": 0.05,
                }
            }
        )
        dots = VGroup(*[Dot(point) for point in cpts])

        
        self.play(Create(hull))
        self.play(Create(dots))

        self.begin_ambient_camera_rotation(rate=0.4)
        self.wait(2)