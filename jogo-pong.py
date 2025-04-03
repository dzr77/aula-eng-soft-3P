# -*- coding: utf-8 -*-
import pygame
import time

# Inicialização do Pygame
pygame.init()

# Definir cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir o tamanho da tela
WIDTH = 800
HEIGHT = 600

# Definir a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Definir o relógio para controlar a taxa de atualização
clock = pygame.time.Clock()

# Definir as raquetes
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
BALL_RADIUS = 10

# Definir posições iniciais
player1_x = 50
player1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
player2_x = WIDTH - 50 - PADDLE_WIDTH
player2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

# Definir a bola
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 7
ball_speed_y = 7

# Definir as pontuações
player1_score = 0
player2_score = 0

# Fonte para exibir a pontuação
font = pygame.font.SysFont("arial", 36)

# Função para desenhar os objetos na tela
def draw_objects():
    screen.fill(BLACK)
    
    # Desenhar as raquetes
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    
    # Desenhar a bola
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)
    
    # Desenhar a linha central
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    
    # Exibir as pontuações
    score_text = font.render(f"{player1_score}  -  {player2_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
    
    pygame.display.flip()

# Função para salvar a pontuação no arquivo de texto
def save_score(player1_score, player2_score):
    with open("scores.txt", "a") as file:
        file.write(f"Player 1: {player1_score} - Player 2: {player2_score}\n")

# Função principal do jogo
def game_loop():
    global player1_y, player2_y, ball_x, ball_y, ball_speed_x, ball_speed_y, player1_score, player2_score
    
    running = True
    while running:
        # Limitar o FPS
        clock.tick(60)
        
        # Verificar eventos (teclas pressionadas, sair do jogo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimentação das raquetes (usando teclas de seta e W/S)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1_y > 0:
            player1_y -= 10
        if keys[pygame.K_s] and player1_y < HEIGHT - PADDLE_HEIGHT:
            player1_y += 10
        if keys[pygame.K_UP] and player2_y > 0:
            player2_y -= 10
        if keys[pygame.K_DOWN] and player2_y < HEIGHT - PADDLE_HEIGHT:
            player2_y += 10

        # Movimentação da bola
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Colisão com o teto ou chão
        if ball_y <= BALL_RADIUS or ball_y >= HEIGHT - BALL_RADIUS:
            ball_speed_y = -ball_speed_y

        # Colisão com as raquetes
        if ball_x <= player1_x + PADDLE_WIDTH and player1_y < ball_y < player1_y + PADDLE_HEIGHT:
            ball_speed_x = -ball_speed_x
        if ball_x >= player2_x - BALL_RADIUS and player2_y < ball_y < player2_y + PADDLE_HEIGHT:
            ball_speed_x = -ball_speed_x

        # Marcar pontos
        if ball_x <= 0:
            player2_score += 1
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_speed_x = -ball_speed_x
            time.sleep(1)  # Pausa para reiniciar a partida
        if ball_x >= WIDTH:
            player1_score += 1
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_speed_x = -ball_speed_x
            time.sleep(1)  # Pausa para reiniciar a partida

        # Desenhar objetos na tela
        draw_objects()

    # Salvar pontuação no arquivo ao final da partida
    save_score(player1_score, player2_score)

# Iniciar o jogo
game_loop()

# Finalizar o Pygame
pygame.quit()
