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


        title = Tex(r"1. Objetivos").to_edge(UP + LEFT)

        
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
        """     for r, x in bifurcation_diagram(r_values, iterations=1000, last=100):
            for i in range(len(r)):
                dot = Dot(
                    axes_top.coords_to_point(r[i], x[i]),
                    radius=0.008,
                    color=WHITE
                )
                 #bif_points.add(dot)
            
        """
        # ------------------------------------------------
        # 3) Conjunto de Mandelbrot (abajo e invertido)
        # ------------------------------------------------
        # 3.1) Parámetros para el Mandelbrot
        RES = 50       # resolución
        MAX_ITER = 50   # iteraciones máximas
        XMIN, XMAX = -2, 1
        YMIN, YMAX = -1.5, 1.5

        # Para dibujar "abajo", crearemos un VGroup y luego lo moveremos
        mandelbrot_group = VGroup()

        # 3.2) Generamos el fractal píxel a píxel
        # Definimos un ancho y alto en coordenadas Manim
        # (para luego ubicarlo centrado bajo el diagrama).
        fractal_width = 7
        fractal_height = 7

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

        mandelbrot_group.next_to(title, DOWN).set_x(0)

        # Mandelbrot (invertido)
        self.play(FadeIn(mandelbrot_group, lag_ratio=0.01), run_time=2)
        self.wait(0.5)

        # Líneas de conexión
        # self.play(Create(lines_group))
        # self.wait(2)
        

