#https://github.com/gitdevpn01/python_pygame_snake/

import pygame , random , time

# Initialisation de pygame
pygame.init()

# Definition des constantes
WIDTH, HEIGHT = 720, 480
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

# Creation fenetre
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Jeu du serpent")

# Frame Per Second
fps = pygame.time.Clock()

# Taille de segment du serpent
segment_size = 10

# Position,direction du serpent
snake_position = [100,50]
direction = 'RIGHT'
change_to = direction

# Variables globales
snake_body = [ [100,50], [90,50], [80,50], [70,50] ]
fruit_position = [random.randrange(1, (WIDTH // 10)) * 10 ,
                  random.randrange(1, (HEIGHT // 10)) * 10  ]
fruit_apparition = False
score = 0

# Fonction gameover
def game_over():
    game_font = pygame.font.SysFont('arial', 50)
    game_over_surface = game_font.render('Ton score est : ' + str(score) , True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH/2, HEIGHT/4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Function Score
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ',True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, (10,10))


# Boucle du jeu
while True:
    # Boucle evenement clavier avec pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'

    # Mise à jour direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Déplacement du serpent
    if direction == 'UP':
        snake_position[1] -= segment_size
    elif direction == 'DOWN':
        snake_position[1] += segment_size
    elif direction == 'LEFT':
        snake_position[0] -= segment_size
    elif direction == 'RIGHT':
        snake_position[0] += segment_size

    # Ajouter un segment au serpent
    snake_body.insert(0, list(snake_position))

    # Test collision serpent
    if snake_position == fruit_position:
        score += 10
        fruit_apparition = False
    else:
        snake_body.pop()
    
    # Position aleatoire de la pomme
    if not fruit_apparition:
        fruit_position = [random.randrange(1, (WIDTH//10) ) * 10,
                          random.randrange(1, (HEIGHT//10) ) * 10]
        fruit_apparition = True

    # Ecran,dessin des éléments
    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], segment_size, segment_size))
    pygame.draw.rect(screen, WHITE, pygame.Rect(fruit_position[0], fruit_position[1], segment_size, segment_size))

    # Affichage du score
    show_score(WHITE, 'arial', 20)

    # Verification collision
    if snake_position[0] < 0 or snake_position[0] > WIDTH - segment_size:
        game_over()
    elif snake_position[1] < 0 or snake_position[1] > HEIGHT - segment_size:
        game_over()

    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    # Mise à jour affichage
    pygame.display.flip()

    # Vitesse affichage
    fps.tick(15)

# Fermer pygame
pygame.quit()
