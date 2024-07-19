from textual.app import App, ComposeResult
from textual import on
from textual.widgets import Label, Input, Button, Header
from textual.containers import Horizontal, Container, Vertical
import turtle

def generate_fractal_sequence(sequence, iterations, rules):

    result = sequence

    for _ in range(iterations):
        new_sequence = ''
        for char in result:
            new_sequence += rules[char]

        result = new_sequence

    return result

def draw_fractal(sequence, distance, plus_angle, minus_angle, my_turtle: turtle.Turtle, initial_x, initial_y):
    turtle.penup()
    turtle.goto(initial_x, initial_y)
    turtle.pendown()

    turtle.speed(0)
    for char in sequence:
        if char == 'F':
            my_turtle.forward(distance)
        elif char == '+':
            my_turtle.right(plus_angle)
        elif char == '-':
            my_turtle.left(minus_angle)


class LindenmayerApp(App[str]):
    CSS_PATH = "main.tcss"
    def compose(self) -> ComposeResult:
        yield Header("Simple L-System generator")

        yield Container(
            Container(
                Label("Operators settings"),
                Input(placeholder="+ angle", type="number", id="plus-angle"),
                Input(placeholder="- angle", type="number", id="minus-angle"),
                Input(placeholder="F distance", type="number", id="forward-distance"),
                classes="box"
            ),

            Container(
                Vertical(
                    Container(
                        Label("Substitution rules"),
                        Input(placeholder="F substitution rule", type="text", restrict="^[F+\-]*$", tooltip="F substitution rule", value="F", id="f-rule"),
                        Input(placeholder="+ substitution rule", type="text", restrict="^[F+\-]*$", tooltip="+ substitution rule", value="+", id="plus-rule"),
                        Input(placeholder="- substitution rule", type="text", restrict="^[F+\-]*$", tooltip="- substitution rule", value="-", id="minus-rule"),
                    ),
                    Container(
                        Label("Initial settings"),
                        Input(placeholder="Axiom", type="text", restrict="^[F+\-]*$", id="axiom"),
                        Input(placeholder="Iterations", type="integer", id="iterations"),
                        Input(placeholder="Initial x-coord", type="number", id="initial-x", value="0"),
                        Input(placeholder="Initial y-coord", type="number", id="initial-y", value="0"),
                    )      
                ),
                classes="box"
            ),
            classes="container"
        )

        yield Button("Run!", id="run")
    

        
        

    @on(Button.Pressed, "#run")
    def run_turtle(self) -> None:
        with self.suspend():

            

            turtle.Turtle._screen = None  # force recreation of singleton Screen object
            turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition


            my_turtle = turtle.Turtle()

            sequence = generate_fractal_sequence(
                sequence=self.query_one("#axiom").value,
                iterations=int(self.query_one("#iterations").value),
                rules= {
                    "F": self.query_one("#f-rule").value,
                    "+": self.query_one("#plus-rule").value,
                    "-": self.query_one("#minus-rule").value,
                }
            )

            print({
                    "F": self.query_one("#f-rule").value,
                    "+": self.query_one("#plus-rule").value,
                    "-": self.query_one("#minus-rule").value,
                })

            draw_fractal(
                sequence=sequence,
                plus_angle=int(self.query_one("#plus-angle").value),
                minus_angle=int(self.query_one("#minus-angle").value),
                distance=int(self.query_one("#forward-distance").value),
                my_turtle=my_turtle,
                initial_x= int(self.query_one("#initial-x").value),
                initial_y= int(self.query_one("#initial-y").value)
            )

            wn = turtle.Screen()
            wn.exitonclick()

            turtle.Turtle._screen = None  # force recreation of singleton Screen object
            turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition

if __name__ == "__main__":
    app = LindenmayerApp()
    app.run()