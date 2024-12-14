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

        title3 = Tex(r"3. Sistemas de Lindenmayer").to_edge(UP + LEFT)

        # text1 = Tex(r"Inspirado en la división celular.", font_size=28).next_to(title, DOWN*2, aligned_edge=LEFT)
        text1 = Tex(r"Comenzamos con un segmento...", font_size=36).shift(UP)

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

        b2 = Brace(kc2[1])
        b2text = b2.get_tex(r"1/3 u")


        self.play(FadeOut(Group(text)), Transform(title, title3))
        self.play(Write(text1))
        self.play(Write(kc), Write(b1), Write(b1text))

        self.next_slide()
        self.play(Transform(kc, kc2))
        self.play(Transform(b1, b2), Transform(b1text, b2text))

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

        self.play(FadeOut(Group(text1)), kc.scale(0.2).to_corner(DOWN + RIGHT))

        
        

        