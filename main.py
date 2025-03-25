# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def draw_menu(screen, font, title, options, selected_option):
    # Clear screen
    screen.fill("black")
    
    # Draw title
    title_text = font.render(title, True, "white")
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/3))
    screen.blit(title_text, title_rect)
    
    # Draw options
    for i, option in enumerate(options):
        color = "yellow" if i == selected_option else "white"
        option_text = font.render(option, True, color)
        option_rect = option_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + i * 50))
        screen.blit(option_text, option_rect)

def menu_loop(screen):
    font = pygame.font.Font(None, 64)
    options = ["Start Game", "Quit"]
    selected_option = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return options[selected_option].lower().replace(" ", "_")
        
        draw_menu(screen, font, "ASTEROIDS", options, selected_option)
        pygame.display.flip()

def game_loop(screen):
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
                return "quit"

        screen.fill("black")

        #update player
        updatable.update(dt)

        #collision check
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                return "game_over", score
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

        pygame.display.flip()
        dt = game_clock.tick(60)/1000

def game_over_screen(screen, score):
    font = pygame.font.Font(None, 64)
    options = ["Play Again", "Quit"]
    selected_option = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return options[selected_option].lower().replace(" ", "_")
        
        draw_menu(screen, font, f"Game Over!\nScore: {score}", options, selected_option)
        pygame.display.flip()

def main():
    if pygame.get_init() == False:
        pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        # Show main menu
        action = menu_loop(screen)
        if action == "quit":
            break
        elif action == "start_game":
            # Start the game
            result = game_loop(screen)
            if result == "quit":
                break
            elif isinstance(result, tuple):  # Game over with score
                _, score = result
                action = game_over_screen(screen, score)
                if action == "quit":
                    break
                elif action == "play_again":
                    continue

    pygame.quit()

if __name__ == "__main__":
    main()