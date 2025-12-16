# BASIC SETUP
import pygame
from sys import exit

#Initialize the pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Page 1, Learning PYGAME")
clock = pygame.time.Clock()

while True: #This is the main game loop. Everything that happens in your game repeatedly goes here
    for event in pygame.event.get(): #gets all the events (keyboard, mouse, quit, etc.)
        if event.type == pygame.QUIT: #checks if the user clicked the close button on the window
            pygame.quit()
            exit()
    # Draw all our elements
    # update anything
    pygame.display.update() #Updates the entire window so any changes you made to the screen actually appear
    clock.tick(60) #limits your game loop to run at most 60 frames per second (FPS)
    