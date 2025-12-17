#BASIC SETUP 2

#How to run this file (you can change the path depending on your folder structure):
#Example 1 (absolute path):
#py -3.12 F:\pygame\pygame_learning\basicSetup2.py

#Example 2 (if you are already inside the folder):
#py -3.12 basicSetup2.py

import pygame

#Initialize the pygame
pygame.init()

#Create The Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Page 1, BASIC SETUP 2")
clock = pygame.time.Clock()

#Game Loop
isrunning = True
while isrunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isrunning = False
            
    
    clock.tick(60)
