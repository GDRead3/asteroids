# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    if pygame.get_init() == False:
        pygame.init()
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    #set groups as container for player
    Player.containers = (updatable, drawable)
    
    #create player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    game_clock = pygame.time.Clock()
    dt = 0

    #basic Game loop
    while True:
        #quit option - makes close window button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #fill Screen
        screen.fill("black")

        #draw player
        #player.draw(screen)
        for thing in drawable:
            thing.draw(screen)

        #update player
        updatable.update(dt)


        #refresh screen
        pygame.display.flip()

        #tick count
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()