# Asteroids Game

A classic Asteroids arcade game clone built with Python and Pygame.

## Description

This is a recreation of the classic Asteroids arcade game where players control a spaceship and destroy asteroids while avoiding collisions. The game features:

- Player-controlled spaceship with rotation and thrust
- Shooting mechanics with cooldown
- Asteroids that split into smaller pieces when shot
- Simple physics-based movement

## Controls

- **W**: Thrust forward
- **A**: Rotate counter-clockwise
- **D**: Rotate clockwise
- **S**: Thrust backward
- **SPACE**: Shoot

## Installation

1. Ensure you have Python installed (Python 3.6 or higher recommended)
2. Install Pygame:
   ```
   pip install pygame
   ```
3. Clone or download this repository
4. Run the game:
   ```
   python main.py
   ```

## Project Structure

- `main.py`: Game entry point and main loop
- `player.py`: Player spaceship class
- `asteroid.py`: Asteroid class
- `shot.py`: Player projectile class
- `circleshape.py`: Base class for game objects
- `constants.py`: Game constants and configuration
- `asteroidfield.py`: Manages asteroid spawning and behavior

## ToDo List

- [x] Add game states (menu, playing, game over)
- [ ] Implement score tracking
- [ ] Add lives system for the player
- [ ] Create visual effects (explosions, thruster particles)
- [ ] Add sound effects and background music
- [ ] Implement screen wrapping for all game objects
- [ ] Add different asteroid types or behaviors
- [ ] Create power-ups (shield, rapid fire, etc.)
- [ ] Add high score tracking
- [ ] Implement difficulty progression (increasing asteroid speed/frequency)
- [ ] Add UFO enemies that shoot at the player
- [ ] Create a pause feature
- [ ] Implement a tutorial or help screen
- [ ] Add visual polish (better graphics, animations)

## Contributing

Feel free to fork this project and submit pull requests with improvements or new features from the ToDo list.

## License

This project is open source and available under the MIT License. 