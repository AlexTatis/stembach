from manim import *
from manim_slides import Slide
import numpy as np

class MovingCameraSlide(Slide, MovingCameraScene):
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
        

class FractalPres(MovingCameraSlide):
    def construct(self):
        text = VGroup(
            Tex(r"{\large$\mathbb{E}$}xplorando la geometría fractal:", font_size=40),
            Tex(r"Un análisis de sus métodos de formación, propiedades y utilidades", font_size=40),
            Tex(r"\textit{Por Alejandro Campo Herbés y Álvaro Vázquez Gómez-Reino}", font_size=24)
        ).arrange(DOWN)

        logos = Group(
            ImageMobject("stem-logo.png"),
            ImageMobject("rosalia-logo.png"),
        ).arrange(RIGHT).to_edge(LEFT + DOWN)

        kc = KochCurve(5, stroke_width=1, length=6).to_edge(DOWN, buff=2.5).rotate(angle=PI, about_point=ORIGIN).shift(DOWN*3)
        kc2 = KochCurve(5, stroke_width=1, length=6).to_edge(DOWN, buff=2.5).shift(UP*3)

        self.play(FadeIn(logos), Write(text))
        self.play(Write(kc, run_time=1), Write(kc2))

        self.next_slide()
        self.play(FadeOut(Group(*self.mobjects)))

        self.camera.frame.save_state()

        title = Tex(r"1. ¿Qué es un fractal?").to_edge(UP + LEFT)
        text1 = Tex(r"En la \textbf{naturaleza} observamos estructuras que podríamos denominar \textit{fractales}.", font_size=28, ).next_to(title, DOWN*2, aligned_edge=LEFT)
        text2 = Tex(r"""Constarían de algunas propiedades que los caracterizan, destacando su \textit{autosimilaridad}.""", font_size=28, tex_environment="flushleft").next_to(text1, DOWN, aligned_edge=LEFT)

        image = Group(
                ImageMobject("copo-nieve.png").scale(0.5),
                ImageMobject("rayo.png").scale(0.5),
                ImageMobject("helecho.png").scale(0.5),
            ).arrange(RIGHT).to_corner(DOWN)

        self.play(Write(title), Write(text1))

        self.next_slide()

        self.play(Write(text2))
        
        
        self.next_slide()

        self.play(FadeIn(image))

        self.next_slide()
        self.play(self.camera.frame.animate.scale(0.5).move_to(image[0]))

        ###
        ### SLIDE 2
        ###

        self.next_slide()

        title2 = Tex(r"2. Objetivos").to_edge(UP + LEFT)

        text = Tex(r"""
        \begin{enumerate}
            \item Explorar matemáticamente 3 técnicas de formación fractal:
                \subitem - Sistemas de Lindenmayer
                \subitem - Sistemas de funciones iteradas
                \subitem - Sistemas dinámicos
                
            \item Analizar las consecuencias reales de las propiedades estudiadas:
                \subitem - Biología
                \subitem - Ingeniería
                \subitem - Metereología
                \subitem - Medicina
                \subitem - ...
                
        \end{enumerate}
        """, font_size=28, tex_environment="flushleft").next_to(title, DOWN*2, aligned_edge=LEFT)

        self.play(Restore(self.camera.frame))
        self.play(FadeOut(Group(text1, text2, image)), Transform(title, title2))
        self.play(Write(text))

        ###
        ### Slide 3
        ###

        self.next_slide()

        title3 = Tex(r"3. Sistemas Lindenmayer").to_edge(UP + LEFT)

        # text1 = Tex(r"Inspirado en la división celular.", font_size=28).next_to(title, DOWN*2, aligned_edge=LEFT)
        text1 = Tex(r"Los fractales se pueden entender como la repetición recursiva de una estructura", font_size=36).shift(UP)

        kc  = KochCurve(0, stroke_width=1, length=10).to_edge(DOWN, buff=2.5).next_to(text1, DOWN * 10)
        kc2 = KochCurve(1, stroke_width=1, length=10).to_edge(DOWN, buff=2.5).next_to(text1, DOWN * 10).shift(5 * (1 - np.sqrt(1/3)) * UP)
        kc3 = KochCurve(2, stroke_width=1, length=10).to_edge(DOWN, buff=2.5).next_to(text1, DOWN * 10).shift(5 * (1 - np.sqrt(1/3)) * UP)
        kc4 = KochCurve(3, stroke_width=1, length=10).to_edge(DOWN, buff=2.5).next_to(text1, DOWN * 10).shift(5 * (1 - np.sqrt(1/3)) * UP)
        kc5 = KochCurve(4, stroke_width=1, length=10).to_edge(DOWN, buff=2.5).next_to(text1, DOWN * 10).shift(5 * (1 - np.sqrt(1/3)) * UP)
        kc6 = KochCurve(5, stroke_width=1, length=10).to_edge(DOWN, buff=2.5).next_to(text1, DOWN * 10).shift(5 * (1 - np.sqrt(1/3)) * UP)
        kc7 = KochCurve(6, stroke_width=1, length=10).to_edge(DOWN, buff=2.5).next_to(text1, DOWN * 10).shift(5 * (1 - np.sqrt(1/3)) * UP)
        kc8 = KochCurve(7, stroke_width=1, length=10).to_edge(DOWN, buff=2.5).next_to(text1, DOWN * 10).shift(5 * (1 - np.sqrt(1/3)) * UP)

        b1 = Brace(kc)
        b1text = b1.get_tex(r"1 u")

        """  b2 = Brace(kc2[1])
        b2text = b2.get_tex(r"1/3 u") """

        self.play(FadeOut(Group(text)), Transform(title, title3))
        self.play(Write(text1))
        self.play(Write(kc), Write(b1), Write(b1text))

        self.next_slide()
        self.play(FadeOut(Group(text1, b1, b1text)))
        self.play(Transform(kc, kc2))
        """ self.play(Transform(b1, b2), Transform(b1text, b2text)) """

        self.next_slide()
        self.play(Transform(kc, kc3))

        self.next_slide()
        self.play(Transform(kc, kc4))
        self.play(Transform(kc, kc5))
        self.play(Transform(kc, kc6))
        self.play(Transform(kc, kc7))
        self.play(Transform(kc, kc8))

        # PENDIENTE: Conseguir poner los Braces en su sitio

        ###
        ### SLIDE 4: Formalizar Lindenmayer
        ###

        self.next_slide()

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


        kc9  = KochCurve(0, stroke_width=1, length=10).scale(0.8).to_corner(DOWN + RIGHT)
        kc10  = KochCurve(1, stroke_width=1, length=10).scale(0.8).to_corner(DOWN + RIGHT)
        kc11  = KochCurve(2, stroke_width=1, length=10).scale(0.8).to_corner(DOWN + RIGHT)
        iteration = Tex(r"$C_0 = \{F\}$", font_size=36).next_to(kc9, UP * 20)
        iteration1 = Tex(r"$C_1 = \{F+F--F+F\}$", font_size=36).next_to(kc9, UP * 20)
        iteration2 = Tex(r"$C_2 = \{F+F--F+F+F+F--F+F...\}$", font_size=36).next_to(kc9, UP * 20)

        dot = Dot().next_to(kc9, LEFT, buff=0)

        self.play(kc.animate.scale(0.8).to_corner(DOWN + RIGHT))
        self.play(Transform(kc, kc9))
        self.play(FadeIn(instructions), FadeIn(rules))
        self.play(Write(iteration), Create(dot))

        self.next_slide()
        self.play(MoveAlongPath(dot, kc9, run_time=2))

        self.next_slide()

        self.play(dot.animate.next_to(kc9, LEFT, buff=0))

        self.next_slide()
        
        tracker = ValueTracker(0)
        dot.add_updater(
             lambda m: m.move_to(kc10.point_from_proportion(tracker.get_value()))
        )

        STOPS = [.25, .5, .75, 1.0]

        self.play(Transform(kc, kc10), Transform(iteration, iteration1))
        
        for stop in STOPS:
            # move to next position
            self.play(tracker.animate.set_value(stop),run_time=1.0)
            # pause, do something, pause
            self.next_slide()

        dot.clear_updaters()

        self.play(dot.animate.next_to(kc9, LEFT, buff=0))
        self.play(Transform(kc, kc11), Transform(iteration, iteration2))
        self.play(MoveAlongPath(dot, kc11, run_time=2))

        self.next_slide()

        ##
        ## Slide 5: CONSECUENCIAS SISTEMAS-L
        ##

        title3 = Tex(r"3. Sistemas Lindenmayer: Consecuencias").to_edge(UP + LEFT)

        island   = KochCurve(7, stroke_width=1, length=5).next_to(title, DOWN*2 + RIGHT * 5)
        island1  = KochCurve(7, stroke_width=1, length=5).next_to(title, DOWN*2 + RIGHT * 5).rotate(240*DEGREES, about_point=island.get_start()).shift(RIGHT * 5)
        island2  = KochCurve(7, stroke_width=1, length=5).next_to(title, DOWN*2 + RIGHT * 5).rotate(-240*DEGREES, about_point=island.get_end()).shift(LEFT * 5)

        text = Tex(r"\[A = \lim_{n\rightarrow\infty} \frac{\sqrt{3}}{20} \left(8-3\left(\frac{4}{9}\right)^n\right) = \frac{8\sqrt{3}}{20} = \boxed{\frac{2\sqrt{3}}{5}}\]", font_size=28).next_to(title, DOWN*2, aligned_edge=LEFT)
        text1 = Tex(r"\[P = \lim_{n\rightarrow\infty} 3 \cdot\left( \frac{4}{3} \right)^n = \boxed{\infty}\]", font_size=28).next_to(text, DOWN, aligned_edge=LEFT)
        text2 = Tex(r"\textbf{¡Área finita contenida por una curva \\ de longitud infinita!}", font_size=28).next_to(text1, 5*DOWN, aligned_edge=LEFT)

        self.play(FadeOut(Group(kc, instructions, rules, iteration, dot)), Transform(title, title3))
        self.play(Write(island), Write(island1), Write(island2))

        self.next_slide()

        self.play(Write(text))

        self.next_slide()

        self.play(Write(text1))
        self.play(Write(text2))

        ##
        ## Slide 6: IFS
        ##

        self.next_slide()

        title4 = Tex(r"4. Sistemas de funciones iteradas").to_edge(UP + LEFT)
        self.play(FadeOut(Group(island, island1, island2, text, text1, text2)), Transform(title, title4))

        square_length = 4
        border = VGroup(Square(stroke_color=WHITE, stroke_width = 1, side_length=square_length))
        square_set = VGroup(Square(fill_color=WHITE, fill_opacity=1.0, stroke_color=WHITE, stroke_opacity=0.0, stroke_width=1, side_length=square_length),
                            Square(fill_color=WHITE, fill_opacity=1.0, stroke_color=WHITE, stroke_opacity=0.0, stroke_width=1, side_length=square_length)
                            )
        
        text = VGroup(Tex(r"\textbf{Contracciones}", font_size=36),
                      Tex(r"\[ S_1 = \begin{pmatrix} \frac{1}{2} & 0 & 1 \\ 0 & \frac{1}{2} & -1 \\ 0 & 0 & 1 \end{pmatrix} \]", font_size=30),
                      Tex(r"\[ S_2 =\frac{3}{8} \cdot\begin{pmatrix} \sqrt{2} & -\sqrt{2} & -1 \\ \sqrt{2} & \sqrt{2} & 1 \\ 0 & 0 & 1 \end{pmatrix} \]", font_size=30)
                      ).arrange(DOWN, buff=MED_LARGE_BUFF).next_to(title, DOWN * 2, aligned_edge=LEFT)
        
        initial_sets = VGroup(Tex(r"\textbf{C. iniciales}", font_size=36), Square(side_length=1), Triangle(radius=0.6, color=WHITE)
                              ).arrange(DOWN, buff=MED_LARGE_BUFF).next_to(title, DOWN * 2, aligned_edge=LEFT).to_corner(RIGHT, buff=LARGE_BUFF * 1.5)

        contractions = VGroup(text)
        contractions.next_to(title, DOWN*2, aligned_edge=LEFT)

        matrix = [[0.5, 0], 
                  [0, 0.5]]
        matrix2 = [[0.75 * np.sqrt(2)/2, -0.75 * np.sqrt(2)/2],
                   [0.75 * np.sqrt(2)/2, 0.75 * np.sqrt(2)/2]]

        def barnsley_ifs(set: VGroup) -> VGroup:
            
            result = VGroup()

            for object in set:
                 
                copy = object.copy()
                copy1 = object.copy()
                
                copy.apply_matrix(matrix).shift(square_length / 4 * LEFT, square_length / 4 * UP)
                copy1.apply_matrix(matrix2).shift(square_length / 4 * RIGHT, square_length / 4 * DOWN)

                result.add(copy, copy1)

            return result

        self.play(Write(contractions))
        self.play(Write(initial_sets))

        self.next_slide()

        self.play(initial_sets[1].animate.scale(1.3).set_color(YELLOW), FadeIn(square_set[0]), FadeIn(border))

        self.next_slide()

        self.play(text[1].animate.scale(1.3).set_color(YELLOW), ApplyMatrix(matrix=matrix, mobject=square_set[0]))
        self.play(square_set[0].animate.shift(square_length / 4 * LEFT, square_length / 4 * UP))
        self.play(text[1].animate.scale(1 / 1.3).set_color(WHITE))

        self.next_slide()

        self.play(FadeIn(square_set[1]), text[2].animate.scale(1.2).set_color(YELLOW))

        self.play(ApplyMatrix(matrix=matrix2, mobject=square_set[1]))
        self.play(square_set[1].animate.shift(square_length / 4 * RIGHT, square_length / 4 * DOWN))
        self.play(text[2].animate.scale(1 / 1.2).set_color(WHITE))

        self.next_slide()

        border.add(square_set.copy().set_fill(opacity=0.0).set_stroke(opacity=1.0))

        self.next_slide()

        self.play(ApplyFunction(mobject=square_set, function=barnsley_ifs))

        self.next_slide()

        for _ in range(8):
            self.play(ApplyFunction(mobject=square_set, function=barnsley_ifs))
        
        self.play(FadeOut(border))

        self.next_slide()
        self.play(initial_sets[1].animate.scale(1 / 1.3).set_color(WHITE), FadeOut(square_set))

        square_set = VGroup(Triangle(radius=square_length / 2, color=WHITE, fill_color=WHITE, fill_opacity=1.0))

        self.play(initial_sets[2].animate.scale(1.3).set_color(YELLOW), FadeIn(square_set))

        self.next_slide()

        for _ in range(10):
            self.play(ApplyFunction(mobject=square_set, function=barnsley_ifs))
        


        ##
        ## Slide 7: Consecuencias IFS
        ##

        self.next_slide()
        title5 = Tex(r"4. Sistemas de funciones iteradas: Consecuencias").to_edge(UP + LEFT)
        body = Group(
            Tex(r"\textbf{¡Cualquier forma es posible!}", font_size=36),
            ImageMobject("stem-ifs.png").scale(1.3)
        ).arrange(DOWN, buff=MED_LARGE_BUFF)

        self.play(FadeOut(initial_sets), FadeOut(square_set), FadeOut(contractions))
        self.play(Transform(title, title5))
        self.play(FadeIn(body))

