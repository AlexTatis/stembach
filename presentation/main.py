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
        

class FractalPres(ThreeDSlide):
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

        # self.camera.frame.save_state()
        title2 = Tex(r"1. Objetivos").to_edge(UP + LEFT)

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
        """, font_size=28, tex_environment="flushleft").next_to(title2, DOWN*2, aligned_edge=LEFT)

        self.play(Write(title2))
        self.play(Write(text))

        self.next_slide()

        self.play(FadeOut(Group(title2, text)))

        title = Tex(r"2. ¿Qué es un fractal?").to_edge(UP + LEFT)
        text1 = Tex(r"En la \textbf{naturaleza} observamos estructuras que podríamos denominar \textit{fractales}.", font_size=28, ).next_to(title, DOWN*2, aligned_edge=LEFT)
        text2 = Tex(r"""Constarían de algunas propiedades que los caracterizan, destacando su \textit{autosimilaridad}.""", font_size=28, tex_environment="flushleft").next_to(text1, DOWN, aligned_edge=LEFT)

        image = Group(
            ImageMobject("copo-nieve.png").scale(0.5),
            ImageMobject("rayo.png").scale(0.5),
            ImageMobject("helecho.png").scale(0.5),
            ).arrange(RIGHT).to_corner(DOWN)

        self.play(Write(title), Write(text1))

        self.play(Write(text2))
        
        self.play(FadeIn(image))

        # self.next_slide()
        # self.play(self.camera.frame.animate.scale(0.5).move_to(image[0]))

        ###
        ### SLIDE 2
        ###

        self.next_slide()

        self.play(FadeOut(Group(title, text1, text2, image)))

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

        self.play(Transform(kc, kc3))

        self.play(Transform(kc, kc4))
        self.play(Transform(kc, kc5))
        self.play(Transform(kc, kc6))
        self.play(Transform(kc, kc7))
        self.play(Transform(kc, kc8))

        self.next_slide()

        expression = Tex(r"\[S = \left( \Sigma, P, \omega \right)\]").next_to(kc, UP * 3)
        self.play(Write(expression))

        # PENDIENTE: Conseguir poner los Braces en su sitio

        ###
        ### SLIDE 4: Formalizar Lindenmayer
        ###

        self.next_slide()

        self.play(Unwrite(expression))

        subtitle = Tex(r"\textbf{Instrucciones}", font_size=36)
        text1 = Tex(r"F $\rightarrow$ Mover 1 paso", font_size=36).next_to(subtitle, DOWN, aligned_edge=LEFT)
        text2 = Tex(r"+ $\rightarrow$ Girar $\frac{\pi}{3}$", font_size=36).next_to(text1, DOWN, aligned_edge=LEFT)
        text3 = Tex(r"- $\rightarrow$ Girar $-\frac{\pi}{3}$", font_size=36).next_to(text2, DOWN, aligned_edge=LEFT)

        instructions = VGroup(subtitle, text1, text2, text3)
        inst_box = SurroundingRectangle(instructions, color=BLUE, buff=MED_LARGE_BUFF, corner_radius=0.2)
        instructions.add(inst_box)
        instructions.next_to(title, DOWN*2, aligned_edge=LEFT)

        subtitle2 = Tex(r"\textbf{Normas de sustitución}", font_size=36)
        text4 = Tex(r"F $\rightarrow$ F+F- -F+F", font_size=36).next_to(subtitle2, DOWN, aligned_edge=LEFT)

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

        self.play(dot.animate.next_to(kc9, LEFT, buff=0))

        self.next_slide()
        
        tracker = ValueTracker(0)
        dot.add_updater(
             lambda m: m.move_to(kc10.point_from_proportion(tracker.get_value()))
        )

        STOPS = [1.0]

        self.play(Transform(kc, kc10), Transform(iteration, iteration1))
        
        for stop in STOPS:
            # move to next position
            self.play(tracker.animate.set_value(stop),run_time=1.0)
            # pause, do something, pause

        dot.clear_updaters()

        self.play(dot.animate.next_to(kc9, LEFT, buff=0))
        self.play(Transform(kc, kc11), Transform(iteration, iteration2))
        self.play(MoveAlongPath(dot, kc11, run_time=2))

        self.next_slide()

        ##
        ## Slide 5: CONSECUENCIAS SISTEMAS-L
        ##

        title3 = Tex(r"3. Sistemas Lindenmayer: Consecuencias").to_edge(UP + LEFT)

        island   = KochCurve(0, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT)
        island1  = KochCurve(0, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(240*DEGREES, about_point=island.get_start()).shift(RIGHT * 5)
        island2  = KochCurve(0, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(-240*DEGREES, about_point=island.get_end()).shift(LEFT * 5)

        island3  = KochCurve(1, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT)
        island4  = KochCurve(1, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(240*DEGREES, about_point=island3.get_start()).shift(RIGHT * 5)
        island5  = KochCurve(1, stroke_width=1, length=5).to_edge(RIGHT).shift(UP * 2, LEFT).rotate(-240*DEGREES, about_point=island3.get_end()).shift(LEFT * 5)
        

        text = Tex(r"\[A = \lim_{n\rightarrow\infty} \frac{\sqrt{3}}{20} \left(8-3\left(\frac{4}{9}\right)^n\right) = \frac{8\sqrt{3}}{20} = \boxed{\frac{2\sqrt{3}}{5}}\]", font_size=28).next_to(title, DOWN*2, aligned_edge=LEFT)
        text1 = Tex(r"\[P = \lim_{n\rightarrow\infty} 3 \cdot\left( \frac{4}{3} \right)^n = \boxed{\infty}\]", font_size=28).next_to(text, DOWN, aligned_edge=LEFT)
        text2 = Tex(r"\textbf{¡Área finita contenida por una curva \\ de longitud infinita!}", font_size=28).next_to(text1, 5*DOWN, aligned_edge=LEFT)

        self.play(FadeOut(Group(kc, instructions, rules, iteration, dot)), Transform(title, title3))
        self.play(Write(island), Write(island1), Write(island2))

        self.next_slide()

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

        self.next_slide()

        self.play(Write(text))

        self.next_slide()

        self.play(Write(text1))
        self.play(Write(text2))

        ##
        ## Slide 9: Bronquio
        ##

        self.next_slide()

        image1 = ImageMobject("bronquio.png").scale(0.5).to_edge(LEFT)
        image2 = ImageMobject("brain-fractal.jpg").scale(0.2)
        image3 = ImageMobject("antena-pcb-removebg-preview.png").scale(0.5).to_edge(RIGHT)


        self.play(FadeOut(Group(island, island1, island2, text, text1, text2)))
        self.play(FadeIn(image1, image2, image3))

        self.next_slide()

        self.play(FadeOut(image1, image2, image3))

        ##
        ## Slide 6: IFS
        ##

        title4 = Tex(r"2. Sistemas de funciones iteradas").to_edge(UP + LEFT)
        self.play(Transform(title, title4))

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
        

        ##
        ## Slide 8: Sistemas dinámicos
        ##

        self.next_slide()

        title6 = Tex(r"5. Sistemas dinámicos").to_edge(UP + LEFT)
        subtitle = Tex(r"\textbf{Normas recursivas}", font_size=36).to_edge(UP).shift(DOWN * 1.5)
        text = VGroup(
             Tex(r"Expresiones del tipo", font_size=36),
             Tex(r"\[X_n = F(X_{n-1}, t)\]", font_size=36),
             Tex(r"son muy comunes en la ciencia", font_size=36),
        ).arrange(DOWN)
        

        self.play(FadeOut(body), Transform(title, title6))
        self.play(Write(subtitle))
        self.play(Write(text))

        self.next_slide()

        self.play(FadeOut(text))

        subtitle2 = Tex(r"\textbf{Normas recursivas: Economía}", font_size=36).next_to(title, DOWN*2, aligned_edge=LEFT)
        text = VGroup(
             Tex(r"Interés compuesto discreto", font_size=36),
             Tex(r"\[A_n = A_{n-1}(1+r)\]", font_size=36),
        ).arrange(DOWN).next_to(subtitle2, DOWN*2)

        chart = BarChart(
            values=[100, 200, 400, 800, 1600],
            bar_names=["Mes 1", "Mes 2", "Mes 3", "Mes 4", "Mes 5"],
            y_range=[0, 1800, 200],
            y_length=5,
            x_length=5,
            x_axis_config={"font_size": 20},
        ).to_corner(RIGHT)

        self.play(Transform(subtitle, subtitle2))
        self.play(Write(text))
        self.play(DrawBorderThenFill(chart, run_time=2))

        self.next_slide()

        self.play(FadeOut(text), FadeOut(chart))

        subtitle3 = Tex(r"\textbf{Normas recursivas: Meteorología}", font_size=36).next_to(title, DOWN*2, aligned_edge=LEFT)
        
        text = VGroup(
             Tex(r"Corrientes de convección", font_size=36),
             Tex(r"""\[
                    \begin{aligned}
                        \frac{\partial x}{\partial t} &= \sigma (y - x), \\
                        \frac{\partial y}{\partial t} &= x (\rho - z) - y, \\
                        \frac{\partial z}{\partial t} &= x y - \beta z.
                    \end{aligned}
                \]""", font_size=36),
        ).arrange(DOWN).next_to(subtitle2, DOWN*2)

        self.play(Transform(subtitle, subtitle3))
        self.set_camera_orientation(phi=2*PI/5, theta=PI/5)

        def lorenz_equations(t, state):
            x, y, z = state
            sigma, rho, beta = 10, 28, 2.667
            dx = sigma * (y - x)
            dy = x * (rho - z) - y
            dz = x * y - beta * z
            return [dx, dy, dz]   
        
        axes = ThreeDAxes(x_length=6, y_length=6, z_length=6, tips=False).to_corner(LEFT).shift(UP + 0.7 * RIGHT)

        initial_conditions = [[0, 1, 1.05], [0, 1, 1.06]]
        scale_factor = 9
        curves = VGroup(axes)

        self.add_fixed_in_frame_mobjects(title, subtitle, text)

        for condition in initial_conditions:
            solution = solve_ivp(lorenz_equations, [0, 30], condition, t_eval=np.linspace(0, 30, 3000))
            points = [axes.c2p(x / scale_factor, y / scale_factor, z / scale_factor) for x, y, z in zip(solution.y[0], solution.y[1], solution.y[2])]
            curve = VMobject(stroke_width=2, stroke_color=BLUE).set_points_as_corners(points)
            curves.add(curve)

        for mob in curves:
            always_rotate(mob, PI / 5, axis=np.array([0., 0., 1.]))
        
        self.play(Create(curves[0]))
    
        self.play(Write(text), Create(curves[1:], run_time=15, rate_func=linear))

        self.wait(20)
        self.next_slide()

        ##
        ## Slide 7: Consecuencias sistemas dinámicos
        ##

        self.play(FadeOut(text, curves))
        self.set_camera_orientation(phi=0, theta=-1.5707963267948966)
        
        title7 = Tex(r"5. Sistemas dinámicos: Consecuencias").to_edge(UP + LEFT)
        subtitle4 = Tex(r"\textbf{El mapa logístico poblacional}", font_size=36).next_to(title, DOWN*2, aligned_edge=LEFT)
        self.play(Transform(title, title7), Transform(subtitle, subtitle4))

        text = Tex(r"\[X_{n+1} = CX_{n}(1 - X_{n})\]", font_size=36).next_to(subtitle4, DOWN*2, aligned_edge=LEFT)

        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1, 0.1],
            x_length=5,
            y_length=5,
            x_axis_config={"font_size": 20},
            y_axis_config={"font_size": 20},
            tips=False,
        ).to_corner(RIGHT, buff=1.5)

        labels = axes.get_axis_labels(
            Tex("Tiempo").scale(0.6).next_to(axes.x_axis, DOWN), 
            Text("Población").scale(0.45)
        )

        C = 1.0
        on_screen_var = Variable(C, "C", num_decimal_places=1).next_to(text, DOWN*2, aligned_edge=LEFT)
        c_tracker = on_screen_var.tracker

        def logistic_map(x: float) -> float:
            return c_tracker.get_value() * x - c_tracker.get_value() * np.square(x)

        self.play(Write(on_screen_var), Write(text), Create(axes), Write(labels))

        # Function to update the graph
        def update_graph(graph):
            population = [initial_population]
            for _ in range(time_steps):
                population.append(logistic_map(population[-1]))
            new_graph = axes.plot_line_graph(
            x_values=list(range(time_steps + 1)),
            y_values=population,
            line_color=BLUE,
            )
            graph.become(new_graph)

        # Plotting the initial evolution of the population over time
        time_steps = 10
        initial_population = 0.5
        population = [initial_population]

        for _ in range(time_steps):
            population.append(logistic_map(population[-1]))

        time_graph = axes.plot_line_graph(
            x_values=list(range(time_steps + 1)),
            y_values=population,
            line_color=BLUE,
        )

        self.play(Write(time_graph, run_time=2))

        # Add updater to the graph
        time_graph.add_updater(update_graph)

        self.next_slide()

        # Animate the change of the parameter C
        self.play(c_tracker.animate.set_value(3.0), run_time=2)
        self.next_slide()

        # Animate the change of the parameter C
        self.play(c_tracker.animate.set_value(3.8), run_time=2)
        self.wait()

        self.next_slide()


        self.play(FadeOut(text), FadeOut(subtitle), FadeOut(on_screen_var), Unwrite(time_graph), FadeOut(axes), FadeOut(labels))

        body = Group(
            Tex(r"\textbf{¡De un caso natural, emerge una estructura fractal!}", font_size=36),
            Axes(
                x_range=[0.7, 4, 0.2],
                y_range=[0, 1, 0.2],
                axis_config={"color": BLUE},
            ).scale(0.75)
        ).arrange(DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER * 2.5)

        labels = body[1].get_axis_labels(x_label="C", y_label="x")

        def logistic_map(r, x):
            return r * x * (1 - x)

        def bifurcation_diagram(r_values, iterations, last):
            x = np.random.rand(len(r_values))
            for i in range(iterations):
                x = logistic_map(r_values, x)
            if i >= (iterations - last):
                yield r_values, x

        r_values = np.linspace(0.7, 4.0, 50000)
        points = VGroup()

        for r, x in bifurcation_diagram(r_values, 1000, 100):
            for i in range(len(r)):
                points.add(Dot(body[1].coords_to_point(r[i], x[i]), radius=0.01, color=WHITE))

        self.play(FadeIn(body), Write(labels))
        
        self.play(FadeIn(points, lag_ratio=0.01), run_time=2)


        # Slide with GIF
        self.next_slide()

        self.play(FadeOut(body), FadeOut(points), FadeOut(labels))


        axes_top = Axes(
                    x_range=[0, 4, 1],
                    y_range=[0, 1, 0.2],
                    x_length=5,
                    y_length=2.5,
                    axis_config={"color": BLUE}
                )
        # Etiquetas
        labels_top = axes_top.get_axis_labels(x_label="r", y_label="x")
        
        # Colocamos este grupo arriba en la pantalla
        bif_axes_group = VGroup(axes_top, labels_top).to_edge(UP, buff=1.5)

        # 2.2) Función logística
        def logistic_map(r, x):
            return r * x * (1 - x)

        # 2.3) Generador de puntos para el diagrama
        def bifurcation_diagram(r_values, iterations=1000, last=100):
            """
            Devuelve (r, x) tras descartar transitorios.
            r_values: array de valores de 'r'
            iterations: número total de iteraciones
            last: cuántas iteraciones finales graficar
            """
            x = np.random.rand(len(r_values))  # condiciones iniciales aleatorias
            for i in range(iterations):
                x = logistic_map(r_values, x)
                # Sólo generamos puntos en las últimas 'last' iteraciones
                if i >= (iterations - last):
                    yield r_values, x

        # 2.4) Creamos los puntos del diagrama
        r_values = np.linspace(0, 4.0, 1000)
        bif_points = VGroup()
        for r, x in bifurcation_diagram(r_values, iterations=1000, last=100):
            for i in range(len(r)):
                dot = Dot(
                    axes_top.coords_to_point(r[i], x[i]),
                    radius=0.008,
                    color=WHITE
                )
                bif_points.add(dot)

        # ------------------------------------------------
        # 3) Conjunto de Mandelbrot (abajo e invertido)
        # ------------------------------------------------
        # 3.1) Parámetros para el Mandelbrot
        RES = 300       # resolución
        MAX_ITER = 50   # iteraciones máximas
        XMIN, XMAX = -2, 1
        YMIN, YMAX = -1.5, 1.5

        # Para dibujar "abajo", crearemos un VGroup y luego lo moveremos
        mandelbrot_group = VGroup()

        # 3.2) Generamos el fractal píxel a píxel
        # Definimos un ancho y alto en coordenadas Manim
        # (para luego ubicarlo centrado bajo el diagrama).
        fractal_width = 10
        fractal_height = 5

        # Función para mapear (x, y) real a coordenadas de Manim
        # centradas, con el mismo ancho que "fractal_width" y alto "fractal_height".
        def mandelbrot_to_manim(px, py):
            """ 
            px, py están en [XMIN, XMAX], [YMIN, YMAX].
            Devolvemos (X, Y) en la escena, centrados en (0,0) por debajo.
            """
            # Proporciones
            # 1) normalizamos px a [0,1] respecto a [XMIN, XMAX]
            nx = (px - XMIN) / (XMAX - XMIN)
            ny = (py - YMIN) / (YMAX - YMIN)
            # 2) escalamos al tamaño en la escena
            X = fractal_width * (nx - 0.5)   # -0.5 para centrar en 0
            Y = fractal_height * (ny - 0.5)  # -0.5 para centrar en 0
            return np.array([X, Y, 0])

        for i in range(RES):
            for j in range(RES):
                # Convertir (i, j) en coordenadas complejas c = x + i y
                x = XMIN + (XMAX - XMIN) * i / (RES - 1)
                y = YMIN + (YMAX - YMIN) * j / (RES - 1)
                c = complex(x, y)

                # Iteramos z_{n+1} = z_n^2 + c
                z = 0
                iteration = 0
                while abs(z) <= 2 and iteration < MAX_ITER:
                    z = z*z + c
                    iteration += 1

                # Color según número de iteraciones (negro->blanco simple)
                color = interpolate_color(BLACK, WHITE, iteration / MAX_ITER)

                # Representamos cada píxel con un cuadrado
                pixel = Square(
                    side_length=(fractal_width / RES),
                    fill_opacity=1,
                    stroke_width=0
                )
                pixel.set_fill(color)
                # Posicionarlo en la escena
                pixel.move_to(mandelbrot_to_manim(x, y))
                mandelbrot_group.add(pixel)

        # Invertimos verticalmente el mandelbrot
        # (flip en el eje UP equivaldría a "reflejar" sobre el eje horizontal)
        mandelbrot_group.flip(UP)

        # Ahora lo desplazamos debajo del diagrama de bifurcación
        #mandelbrot_group.next_to(bif_axes_group, DOWN, buff=1.0)

        # ------------------------------------------------
        # 4) Añadir líneas que conecten r (arriba) con c (abajo)
        # ------------------------------------------------
        # Supongamos un mapeo lineal: c(r) = -2 + 3r/4
        # => si r=0 -> c=-2, si r=4 -> c=1
        # Dibujamos líneas en r_line_values = [0,1,2,3,4], por ejemplo
        r_line_values = [1, 3, 3.45, 3.85]
        lines_group = VGroup()

        for rv in r_line_values:
            # Coordenada X en el diagrama de bifurcación (arriba)
            top_x = axes_top.coords_to_point(rv, 1.0)  # y=1 (para que baje desde "arriba")
            # Calculamos c
            c_val = -2 + 3*rv/4.0
            # Lo llevamos al mandelbrot "invertido"
            # Tomamos y=0 (eje real) antes de la inversión
            # => (c_val, 0) en el plano del fractal
            # Convertimos a la posición en la escena con la misma función,
            # y luego aplicamos la inversión que ya hicimos con .flip(UP).
            # Para no complicarnos, simplemente localizamos el pixel en y=0:
            bottom_point_before_flip = mandelbrot_to_manim(c_val, 0)
            # Como ya hemos hecho un flip vertical, la posición en la escena
            # es la misma. Solo necesitamos el SHIFT que le dimos a mandelbrot_group.
            # Extraemos la posición final sumando su center:
            bottom_x = bottom_point_before_flip + mandelbrot_group.get_center() - ORIGIN

            # Creamos la línea
            line = DashedLine(
                start=top_x,
                end=bottom_x,
                dash_length=0.05,
                color=YELLOW
            )
            lines_group.add(line)

        # ------------------------------------------------
        # 5) Añadimos todo a la escena
        # ------------------------------------------------
        self.play(FadeIn(title))
        self.wait(0.5)

        # Diagrama de bifurcación
        # self.play(FadeIn(bif_axes_group))
        # self.play(FadeIn(bif_points, lag_ratio=0.01), run_time=2)
        # self.wait(0.5)

        # Mandelbrot (invertido)
        self.play(FadeIn(mandelbrot_group, lag_ratio=0.01), run_time=2)
        self.wait(0.5)

        # Líneas de conexión
        # self.play(Create(lines_group))
        # self.wait(2)
        
        self.next_slide()

        self.play(FadeOut(title), FadeOut(mandelbrot_group))


        body = Group(Tex(r"¡Gracias por su atención!"),
                     ImageMobject("qr-code.png")).arrange(DOWN)
        
        self.play(FadeIn(body))

        self.next_slide()

        self.play(FadeOut(body))

        colab = VGroup(
             Text('Supervisión'),
             Text("María Ermitas Pintos Testa", font_size=36),
             Text("Coordinadora del centro", font_size=30),
             KochCurve(7, stroke_width=1, length=4),
             Text("Jerónimo Rodríguez García", font_size=36),
             Text("Tutor de la USC", font_size=30) 
            ).arrange(DOWN, buff=0.5)
        
        self.play(Write(colab), run_time=3)





