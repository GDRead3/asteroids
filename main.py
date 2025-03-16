# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    if pygame.get_init() == False:
        pygame.init()
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize score
    score = 0
    font = pygame.font.Font(None, 36)

    #create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #set groups as container for player
    Player.containers = (updatable, drawable)

    #set group as container for asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    
    #set group as container for asteroid field (only updatable, not drawable)
    AsteroidField.containers = (updatable,)
    
    #set group as container for shots
    Shot.containers = (shots, updatable, drawable)
    
    #create player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #create asteroid field
    asteroid_field = AsteroidField()

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

        #update player
        updatable.update(dt)

        #collision check
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print ("Game Over!")
                return #this exits the game
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
                    # Add points based on asteroid size
                    score += int(100 * (asteroid.radius / ASTEROID_MAX_RADIUS))

        #draw player
        #player.draw(screen)
        for thing in drawable:
            thing.draw(screen)

        # Draw score
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        #refresh screen
        pygame.display.flip()

        #tick count
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()