#[ Set up Movement ]

#How to run this file (you can change the path depending on your folder structure):
#Example (absolute path):
# py -3.12 F:\pygame\pygame_learning\movement.py

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space War")
icon = pygame.image.load('icon1.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player1.png')

#Player starting position (X and Y coordinates)
playerX = 370
playerY = 480

def player(x, y):
    """
    Draws the player image on the screen
    at the given (x, y) position
    """
    screen.blit(playerImg, (x, y))
    
running = True
while running:
    
    screen.fill((0, 156, 153)) 
    
    #Automatically move the player
    #X increases -> moves right
    #Y decreases -> moves upward
    playerX += 0.1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        #Draw the player at the updated position
        player(playerX, playerY)
        
        pygame.display.update()
        