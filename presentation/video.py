from manim import *
from manim_slides import ThreeDSlide
import numpy as np
from scipy.integrate import solve_ivp

class MovingCameraSlide(ThreeDSlide, MovingCameraScene):
    pass

def KochCurve(
            n, length=5, stroke_width=8, color=("#ffffff", "#ffffff", "#ffffff") 
        ):

            l = length / (3 ** n)

            LineGroup = Line().set_length(l)

            def NextLevel(LineGroup):
                return VGroup(
                    *[LineGroup.copy().rotate(i) for i in [0, PI / 3, -PI / 3, 0]]
                ).arrange(RIGHT, buff=0, aligned_edge=DOWN)

            for _ in range(n):
                LineGroup = NextLevel(LineGroup)

            KC = (
                VMobject(stroke_width=stroke_width)
                .set_points(LineGroup.get_all_points())
                .set_color(color)
            )
            return KC
        

class KochVideo(ThreeDScene):
    def construct(self):
        title = Tex(r"3. Sistemas Lindenmayer: Consecuencias").to_edge(UP + LEFT)

        subtitle = Tex(r"\textbf{Instrucciones}", font_size=36)
        text1 = Tex(r"F $\rightarrow$ Mover 1 paso", font_size=36).next_to(subtitle, DOWN, aligned_edge=LEFT)
        text2 = Tex(r"+ $\rightarrow$ Girar $\frac{\pi}{3}$", font_size=36).next_to(text1, DOWN, aligned_edge=LEFT)
        text3 = Tex(r"- $\rightarrow$ Girar $-\frac{\pi}{3}$", font_size=36).next_to(text2, DOWN, aligned_edge=LEFT)

        instructions = VGroup(subtitle, text1, text2, text3)
        inst_box = SurroundingRectangle(instructions, color=BLUE, buff=MED_LARGE_BUFF, corner_radius=0.2)
        instructions.add(inst_box)
        instructions.next_to(title, DOWN*2, aligned_edge=LEFT)

        subtitle2 = Tex(r"\textbf{Normas de sustitución}", font_size=36)
        text4 = Tex(r"F $\rightarrow$ F+F--F+F", font_size=36).next_to(subtitle2, DOWN, aligned_edge=LEFT)

        rules = VGroup(subtitle2, text4)
        rules_box = SurroundingRectangle(rules, color=RED, buff=MED_LARGE_BUFF, corner_radius=0.2)
        rules.add(rules_box)
        rules.next_to(instructions, DOWN*2, aligned_edge=LEFT)

        island   = KochCurve(0, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT)
        island1  = KochCurve(0, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(240*DEGREES, about_point=island.get_start()).shift(RIGHT * 5)
        island2  = KochCurve(0, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(-240*DEGREES, about_point=island.get_end()).shift(LEFT * 5)

        island3  = KochCurve(1, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT)
        island4  = KochCurve(1, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(240*DEGREES, about_point=island3.get_start()).shift(RIGHT * 5)
        island5  = KochCurve(1, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(-240*DEGREES, about_point=island3.get_end()).shift(LEFT * 5)


        self.play(FadeIn(instructions), FadeIn(rules))
        self.play(Write(island), Write(island1), Write(island2))
        self.wait()
        self.play(Transform(island, island3), Transform(island1, island4), Transform(island2, island5))

        
        island3  = KochCurve(2, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT)
        island4  = KochCurve(2, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(240*DEGREES, about_point=island3.get_start()).shift(RIGHT * 5)
        island5  = KochCurve(2, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(-240*DEGREES, about_point=island3.get_end()).shift(LEFT * 5)

        self.play(Transform(island, island3), Transform(island1, island4), Transform(island2, island5))

        island3  = KochCurve(3, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT)
        island4  = KochCurve(3, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(240*DEGREES, about_point=island3.get_start()).shift(RIGHT * 5)
        island5  = KochCurve(3, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(-240*DEGREES, about_point=island3.get_end()).shift(LEFT * 5)

        self.play(Transform(island, island3), Transform(island1, island4), Transform(island2, island5))

        island3  = KochCurve(4, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT)
        island4  = KochCurve(4, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(240*DEGREES, about_point=island3.get_start()).shift(RIGHT * 5)
        island5  = KochCurve(4, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(-240*DEGREES, about_point=island3.get_end()).shift(LEFT * 5)

        self.play(Transform(island, island3), Transform(island1, island4), Transform(island2, island5))

        island3  = KochCurve(7, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT)
        island4  = KochCurve(7, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(240*DEGREES, about_point=island3.get_start()).shift(RIGHT * 5)
        island5  = KochCurve(7, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(-240*DEGREES, about_point=island3.get_end()).shift(LEFT * 5)

        self.play(Transform(island, island3), Transform(island1, island4), Transform(island2, island5))

        
class CreditsVideo(ThreeDScene):
     def construct(self):
        
        music = VGroup(
             Text('Música'),
             Text("♪ Fractals - Vincent Rubinetti", font_size=36) 
            ).arrange(DOWN, buff=0.5).to_corner(UP)
        
        line = KochCurve(7, stroke_width=1, length=4).next_to(music, DOWN * 3)

        credits = VGroup(
             Text("Gráficos"),
             Text("Jonny Hyman (https://github.com/jonnyhyman/Chaos)", font_size=30) ,
             Text("Zoom del mapa logístico, mapeo al conjunto de Mandelbrot", font_size=24)
        ).arrange(DOWN, buff=0.5).next_to(line, DOWN * 3)


        self.play(Write(music, run_time=1))
        self.play(Write(line, run_time=1))
        self.play(Write(credits, run_time=2))
        self.wait()

        self.play(FadeOut(*self.mobjects))

        colab = VGroup(
             Text('Supervisión'),
             Text("María Ermitas Pintos Testa", font_size=36),
             Text("Coordinadora del centro", font_size=30),
             KochCurve(7, stroke_width=1, length=4),
             Text("Jerónimo Rodríguez García", font_size=36),
             Text("Tutor de la USC", font_size=30) 
            ).arrange(DOWN, buff=0.5)
        self.play(Write(colab), run_time=3)

        self.wait()
        self.play(FadeOut(*self.mobjects))
        
        text = Group(Text("Código y memoria del proyecto"),
                      ImageMobject("qr-code.png"),
                      Text("https://github.com/AlexTatis/stembach", font_size=36)
            ).arrange(DOWN)

        self.play(FadeIn(text))
        self.wait()

class Testing(ThreeDSlide):
     def construct(self):
        axes = Axes(
            x_range=[0.7, 4, 0.2],
            y_range=[0, 1, 0.2],
            axis_config={"color": BLUE},
        )

        labels = axes.get_axis_labels(x_label="r", y_label="x")

        self.play(Create(axes), Write(labels))

        def logistic_map(r, x):
            return r * x * (1 - x)

        def bifurcation_diagram(r_values, iterations, last):
            x = np.random.rand(len(r_values))
            for i in range(iterations):
                x = logistic_map(r_values, x)
            if i >= (iterations - last):
                yield r_values, x

        r_values = np.linspace(0.7, 4.0, 15000)
        points = VGroup()

        for r, x in bifurcation_diagram(r_values, 1000, 100):
            for i in range(len(r)):
                points.add(Dot(axes.coords_to_point(r[i], x[i]), radius=0.01, color=WHITE))

        self.play(FadeIn(points, lag_ratio=0.01), run_time=2)
        self.wait()

