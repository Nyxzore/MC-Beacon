from manim import *
from manim.utils.rate_functions import double_smooth


class WeightedSumScene(Scene):
    def construct(self):
        title = Title("New Beacon Colour")
        
        eq1 = MathTex(
            r"\vec{C_{\omega}} = 1 \cdot \vec{C_0} + 1 \cdot \vec{C_1} + 2 \cdot \vec{C_2} + 4 \cdot \vec{C_3} + 8 \cdot \vec{C_4}"
        )

        self.play(Write(title), Write(eq1))
        # Animate the camera frame to zoom on the word
        
        self.play(Indicate(eq1[0][2]))
        self.play(Indicate(eq1[0][4], color=BLUE))
        self.play(Indicate(eq1[0][10], color=RED))
        self.play(Indicate(eq1[0][16], color=RED))
        self.play(Indicate(eq1[0][22], color=RED))
        self.play(Indicate(eq1[0][28], color=RED))

        # Brace the repeated terms
        brace_terms = eq1[0][10:32]
        brace = Brace(brace_terms, direction=DOWN, color=RED)
        label = Tex("Geometric series").next_to(brace, DOWN, buff=0.2)

        self.play(Create(brace), Write(label))

        # Summation form
        eq2 = MathTex(r"\sum_{i=1}^{n-1}2^{i-1}C_i").next_to(eq1, DOWN, buff=0.2)
        self.play(ReplacementTransform(VGroup(label, brace), eq2))

        # Left-hand side + first term
        e3 = eq1[0][0:10]  
        self.play(
            Indicate(e3, color=BLUE),
            e3.animate.next_to(eq2, LEFT),
            FadeOut(eq1[0][10:33])
        )

        # Group LHS + summation
        e4 = VGroup(e3, eq2)

        # --- Final clean equation ---
        final_eq = MathTex(
            r"\vec{C_{w}} = \vec{C_0} + \sum_{i=1}^{n-1}2^{i-1}C_i"
        ).move_to(ORIGIN)

        self.play(Transform(e4, final_eq))
        self.play(ApplyWave(final_eq))
        self.wait()

class Example(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[0, 255, 50],
            y_range=[0, 255, 50],
            z_range=[0, 255, 50],
            x_length=5,
            y_length=5,
            z_length=5,
        )

        r_label = MathTex("255").next_to(axes.c2p(255, 0, 0), RIGHT, buff=0.2)
        g_label = MathTex("255").next_to(axes.c2p(0, 255, 0), UP, buff=0.2)
        b_label = MathTex("255").next_to(axes.c2p(0, 0, 255), DOWN, buff=0.2)

        red_vec = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(176, 46, 38),
            color=rgb_to_color([176/255, 46/255, 38/255])
        )
        purple_vec = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(137, 50, 184),
            color=rgb_to_color([137/255, 50/255, 184/255])
        )
        cyan_vec = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(22, 156, 156),
            color=rgb_to_color([22/255, 156/255, 156/255])
        )

        labels = VGroup(
            MathTex(r"\text{R}", r"=(176, 46, 38)").set_color_by_tex("R", red_vec.get_color()),
            MathTex(r"\text{P}", r"=(137, 50, 184)").set_color_by_tex("P", purple_vec.get_color()),
            MathTex(r"\text{C}", r"=(22, 156, 156)").set_color_by_tex("C", cyan_vec.get_color()),
        )
        ans = MathTex(r"\text{N}", r" = \text{R} + \text{P} + 2\text{C} = (357,408,534)")
        ans.set_color_by_tex(r"\text{N}", color=[RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])

        labels.arrange(DOWN, aligned_edge=RIGHT)
        labels.to_corner(UR)
        ans.next_to(labels,DOWN,aligned_edge=RIGHT)

        self.play(Write(labels))
        self.add_fixed_in_frame_mobjects(labels)
        self.play(Write(ans))
        self.add_fixed_in_frame_mobjects(ans)

        self.add_fixed_in_frame_mobjects(r_label, g_label, b_label)
        self.play(Create(axes), Write(r_label), Write(g_label), Write(b_label))

        self.play(Create(red_vec))
        self.play(Create(purple_vec))
        self.play(Create(cyan_vec))

        self.wait(1)
        new_vec = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(357,408,534),
            color=[RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        )

        self.play(Create(new_vec, rate_func=double_smooth))
        self.wait()

class Normalise(Scene):
    def construct(self):
        eq1 = MathTex(r"\vec{C_{\omega}} = 1 \cdot \vec{C_0} + 1 \cdot \vec{C_1} + 2 \cdot \vec{C_2} + 4 \cdot \vec{C_3} + 8 \cdot \vec{C_4}")
        self.play(Write(eq1))
        self.play(Indicate(eq1[0][2]))
        self.play(Indicate(eq1[0][4], color=BLUE))
        self.play(Indicate(eq1[0][10], color=RED))
        self.play(Indicate(eq1[0][16], color=RED))
        self.play(Indicate(eq1[0][22], color=RED))
        self.play(Indicate(eq1[0][28], color=RED))

        eq2 = MathTex(r"\omega = 1+1+2+4+8=16")
        self.play(ReplacementTransform(eq1,eq2))
        self.play(FadeOut(eq2))
        ans = MathTex(r"\text{N}", r" = \text{R} + \text{P} + 2\text{C} = (357,408,534)")
        ans.set_color_by_tex(r"\text{N}", color=[RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        self.play(Write(ans))
        eq3 = MathTex(r"\omega = 1+1+2=4").next_to(ans, DOWN)
        self.play(Write(eq3))
        final = MathTex(r"\vec{C}=\left(\frac{357}{4},\frac{408}{4},\frac{534}{4}\right)").next_to(eq3,DOWN)
        self.play(Write(final))
        final2 = MathTex(r"\vec{C}=(89,102,134)").next_to(eq3,DOWN)
        self.play(ReplacementTransform(final, final2))
        self.play(final.animate.set_color("#596686"))
        self.wait()
        self.play(FadeOut(*self.mobjects))

        general = MathTex(r"\vec{C_{w}} = \vec{C_0} + \sum_{i=1}^{n-1}2^{i-1}\vec{C}_i").to_edge(UP)
        self.play(Write(general))

        weight = MathTex(r"\omega = 1+1+2+4+...+2^{(n-1)-1}").next_to(general,DOWN)
        self.play(Write(weight))

        new_weight = MathTex(r"\omega = 1+\sum_{i=1}^{n-1}2^{i-1}").next_to(general,DOWN)
        self.play(ReplacementTransform(weight, new_weight))
        weight = new_weight

        new_weight = MathTex(r"\omega=1+\frac{2^{n-1}-1}{2-1}").next_to(general,DOWN)
        self.play(ReplacementTransform(weight, new_weight))
        weight = new_weight

        new_weight = MathTex(r"\omega=2^{n-1}").next_to(general,DOWN)
        self.play(ReplacementTransform(weight, new_weight))
        weight = new_weight

        self.wait()
        colour = MathTex(r"\vec{C} = \frac{\vec{C}_{\omega}}{\omega}").next_to(weight,DOWN)
        
        self.play(Write(colour))

        self.play(FadeOut(*self.mobjects))
        F = MathTex(r"\vec{C} = \frac{\vec{C_0} + \sum_{i=1}^{n-1}2^{i-1}\vec{C}_i}{2^{n-1}}")
        self.play(Write(F))
        self.play(ReplacementTransform(F, MathTex(r"\vec{C} = \frac{1}{2^n-1}\left(\vec{C}_0 + \sum_{i=1}^{n-1} 2^{i-1} \vec{C}_i \right)")))
        self.play(Wiggle(F))
        num = Tex("n : number of glass blocks").next_to(F, DOWN)
        self.play(Write(num))
        


        self.wait()