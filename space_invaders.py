import pygame
import random
import math
# Iniciando o pygame
pygame.init()

# Iniciando a tela  
screen = pygame.display.set_mode((800, 600))


# Título e ícone 
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('inimigo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('jogo-de-arcade (1).png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 8

for i in range(num_of_enemies):
     enemyImg.append(pygame.image.load('inimigo.png')) 
     enemyX.append(random.randint(0, 735))
     enemyY.append(random.randint(50, 150))
     enemyX_change.append(0.30)
     enemyY_change.append(40)

# bala 
balaImg = pygame.image.load('bala.png')
balaX = 0
balaY = 480
balaX_change = 0
balaY_change = 10
bala_state = "ready"

# score 
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
     score = font.render("Score:" + str(score_value), True, (255, 255, 255))
     screen.blit(score, (x, y))

def game_over_text():
     over_text = over_font.render("GAME OVER", True, (255, 255, 255))
     screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))    

def fire_bala(x, y):
     global bala_state
     bala_state = "fire"
     screen.blit(balaImg, (x + 16, y +10))

def isCollision(enemyX, enemyY, balaX, balaY):
     distance = math.sqrt((math.pow(enemyX - balaX, 2)) + (math.pow(enemyY - balaY, 2)))
     if distance < 27:
          return True
     else:
          return False

#Game loop 
running = True
while running:

    # RGB 
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keystroke 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                 if bala_state is "ready":
                    balaY_change = 0.8
                    balaX = playerX
                    fire_bala(balaX, balaY)          
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT  or event.key == pygame.K_RIGHT:
                      playerX_change = 0
    

    
    playerX += playerX_change
    if playerX <=0:
         playerX = 0
    elif playerX >=736:
         playerX = 736        

    for i in range(num_of_enemies):

        if enemyY[i] > 440:
             for j in range(num_of_enemies):
                  enemyY[j] = 2000
             game_over_text()
             break     

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >=736:
            enemyX_change[i] = -0.3 
            enemyY[i] += enemyY_change[i]
    
        collision = isCollision(enemyX[i], enemyY[i], balaX, balaY)
        if collision:
            balaY = 480
            bala_state = "ready"
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)


    if balaY <=30:
         balaY = 480
         bala_state = "ready"

    if bala_state is "fire":          
         fire_bala(balaX, balaY)
         balaY -= balaY_change     


    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()