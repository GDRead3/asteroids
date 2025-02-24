# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    if pygame.get_init() == False:
        pygame.init()
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #basic Game loop
    while True:
        #quit option - makes close window button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #fill Screen
        screen.fill("black")


        #refresh screen
        pygame.display.flip()

if __name__ == "__main__":
    main()