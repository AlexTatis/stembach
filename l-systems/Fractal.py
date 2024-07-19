import turtle

def generate_fractal_sequence(sequence, iterations):
    for _ in range(iterations):
        new_sequence = ''
        for char in sequence:
            if char == '+':
                new_sequence += '-+-+-+-+-+-+-+-+-+-+-+-++'
            else:
                new_sequence += char
        sequence = new_sequence

    return sequence

def draw_fractal(sequence, radius):
    turtle.penup()
    #turtle.goto(-radius, -radius)
    turtle.pendown()
    turtle.speed(0)
    for char in sequence:
        if char == '+':
            turtle.circle(radius)
            radius *= -6
        elif char == '-':
            turtle.circle(radius, 360 / 12)
            radius /= -6

def main():
    iterations = int(input("Enter the number of iterations: "))
    sequence = generate_fractal_sequence("+", iterations)
    radius = 50 * iterations

    draw_fractal(sequence, radius)
    turtle.done()

if __name__ == "__main__":
    main()