import turtle

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")  # titolo del gioco
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # evita il refresh continuo della pagina rendendo il gioco piu veloce

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # velocità dell'animazione non della barra
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)  # la schermata è come un piano cartesiano con l'origine nel centro

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # velocità dell'animazione non della barra
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # velocità dell'animazione non della barra
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.05
ball.dy = 0.05  # ogni volta che la palla si muove lo fa di 2px

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Giocatore A: 0  Giocatore B:0', align="center", font=("Courier", 24, "bold"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()  # ycor è un metodo di turtle
    y += 20  # aggiunge 20 pixel verso l'alto
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # ycor è un metodo di turtle
    y -= 20  # aggiunge 20 pixel verso l'alto
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # ycor è un metodo di turtle
    y += 20  # aggiunge 20 pixel verso l'alto
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # ycor è un metodo di turtle
    y -= 20  # aggiunge 20 pixel verso l'alto
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")  # quando l'utente preme "w" chiama la funzione paddle_a_up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reverse the direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # reverse the direction

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dx = 0.05
        score_a += 1
        pen.clear()
        pen.write('Giocatore A: {}  Giocatore B: {}'.format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dx = 0.05
        score_b += 1
        pen.clear()
        pen.write('Giocatore A: {}  Giocatore B: {}'.format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    # paddle-ball collision
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        ball.dx -= 0.02

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        ball.dx += 0.02
