import os # os module provides a way to interact with the operating system (such as working with files and directories)

import random # allows you to generate random numbers or perform random operations in your code

import math # provides various mathematical functions and constants for mathematical operations

import pygame # library for creating 2D games in Python (functionality for handling graphics, sound, & user input in games)

#  import the listdir function from the os module
from os import listdir # (used to list all the files and directories in a specified directory)

# import the isfile and join functions from the os.path module
from os.path import isfile, join # isfile is used to check if a given path points to a regular file, & join is used to join parts of file paths into a single path

# intitialize pygame module
pygame.init()

# 
pygame.display.set_caption("Platformer")

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def get_background(name): # using tile images create background
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []
    # loop through tiles in width and height direction
    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height) # position of the tile from the top left corner to move
            tiles.append(pos)

    return tiles, image

# draw background
def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)

    pygame.display.update()

def main(window): 
    # event loop for collision, character
    clock = pygame.time.Clock()
    #  refernce background function
    background, bg_image = get_background("Brown.png")

    run = True
    while run:
        clock.tick(FPS) # while loop runs max 60 frames per second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break # break loop if player quirtes the game

        # draw background function
        draw(window, background, bg_image)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
