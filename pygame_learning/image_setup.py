#[ Adding Images  ]

#How to run this file (you can change the path depending on your folder structure):
#Example (absolute path):
# py -3.12 F:\pygame\pygame_learning\image_setup.py

import pygame

pygame.init()

#Create the game window (width: 800, height: 600)
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space War")
icon = pygame.image.load('icon1.png')
pygame.display.set_icon(icon)

#Load the player image
playerImg = pygame.image.load('player1.png')

# Player starting position (X and Y coordinates)
playerX = 370
playerY = 400

def player():
    screen.blit(playerImg, (playerX, playerY))

clock = pygame.time.Clock()

#Game Loop
running = True
while running:
    
    #RGB = Red, Green, Blue
    screen.fill((0, 156, 153)) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Draw the player on the screen
    player()
    pygame.display.update()
            
    clock.tick(60)
