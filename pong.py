#Replicando o jogo Pong do ATARI

# Importando as bibliotecas
import turtle
from time import sleep

# Criando a tela de jogo
tela = turtle.Screen()
tela.title("Pong by JeanOmeg")
tela.bgcolor("black")
tela.setup(width=800, height=642)
tela.tracer(0)

# Pontuação
pontuacao_a = 0
pontuacao_b = 0

# Jogador A
jogador_a = turtle.Turtle()
jogador_a.speed(0)
jogador_a.shape("square")
jogador_a.color("white")
jogador_a.shapesize(stretch_wid=5, stretch_len=1)
jogador_a.penup()
jogador_a.goto(-350, 0)

# Jogador B
jogador_b = turtle.Turtle()
jogador_b.speed(0)
jogador_b.shape("square")
jogador_b.color("white")
jogador_b.shapesize(stretch_wid=5, stretch_len=1)
jogador_b.penup()
jogador_b.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dy = 0.5
bola.dx = 0.1

# Marcador de pontos
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 291)
marcador.write(f"PLAYER A: {pontuacao_a}    PLAYER B: {pontuacao_b}   SPEED: {bola.dx}", align="center", font=("Courie", 8, "bold"))

# Funções
def jogador_a_cima():
    y = jogador_a.ycor()
    y += 20
    jogador_a.sety(y)
    
def jogador_a_baixo():
    y = jogador_a.ycor()
    y -= 20
    jogador_a.sety(y)

def jogador_b_cima():
    y = jogador_b.ycor()
    y += 20
    jogador_b.sety(y)
    
def jogador_b_baixo():
    y = jogador_b.ycor()
    y -= 20
    jogador_b.sety(y)


# Leitura do teclado
tela.listen()
tela.onkeypress(jogador_a_cima, "w")
tela.onkeypress(jogador_a_baixo, "s")
tela.onkeypress(jogador_b_cima, "Up")
tela.onkeypress(jogador_b_baixo, "Down")

# Loop principal do jogo
while True:
    tela.update()
    
    # Movimento da bola
    bola.sety(bola.ycor() + bola.dy)
    bola.setx(bola.xcor() + bola.dx)
    
    # Checando as bordas
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
        
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
        
    # Atualizando pontuação, velocidade e direção da bola
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        bola.dx += -0.1
        pontuacao_a += 1
        marcador.clear()
        marcador.write(f"PLAYER A: {pontuacao_a}    PLAYER B: {pontuacao_b}   SPEED: {bola.dx * -1:.1f}", align="center", font=("Courie", 8, "bold"))
        
    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        bola.dx += 0.1
        pontuacao_b += 1
        marcador.clear()
        marcador.write(f"PLAYER A: {pontuacao_a}    PLAYER B: {pontuacao_b}   SPEED: {bola.dx:.1f}", align="center", font=("Courie", 8, "bold"))
        
    # Colisão jogadores e bola
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < jogador_b.ycor() + 60 and bola.ycor() > jogador_b.ycor() -60):
        bola.setx(340)
        bola.dx *= -1
        
    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < jogador_a.ycor() + 60 and bola.ycor() > jogador_a.ycor() -60):
        bola.setx(-340)
        bola.dx *= -1
