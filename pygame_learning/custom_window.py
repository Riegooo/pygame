#CHANGING THE TITLE, LOGO, AND BACKGROUND COLOR
import pygame

#Initialize the pygame
pygame.init()

#Create The Screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space War") #Sets the title of the window that appears at the top bar
icon = pygame.image.load('icon1.png') #Load an image file as the window icon
pygame.display.set_icon(icon) #Set the loaded image as the window icon, (icon)

#This is very important for controlling game’s speed
clock = pygame.time.Clock() 

#Game Loop
running = True
while running: #This is the main game loop. Everything that happens in your game repeatedly goes here
    for event in pygame.event.get(): #gets all the events (keyboard, mouse, quit, etc.)
        if event.type == pygame.QUIT: #checks if the user clicked the close button on the window
            running = False #Stops the Game Loop
    
    #Fill the entire window with a solid color
    screen.fill((0, 156, 153)) 
    
    #Updates the entire window so any changes you made to the screen actually appear
    pygame.display.update() 
    
    #limits your game loop to run at most 60 frames per second (FPS)
    clock.tick(60) 
    
    
# py -3.12 F:\pygame\pygame_learning\custom_window.py