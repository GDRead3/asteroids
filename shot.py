import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOT_SPEED, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, position, direction):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(direction) * PLAYER_SHOT_SPEED
        self.color = "white"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)