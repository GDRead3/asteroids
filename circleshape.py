import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other):
        """
        Check if this CircleShape collides with another CircleShape.
    
        Args:
        other: Another CircleShape object
        
        Returns:
        True if the shapes are colliding, False otherwise
        """
        # Calculate distance between the two centers
        distance = self.position.distance_to(other.position)
    
        # Sum of the radii
        radii_sum = self.radius + other.radius
    
        # If distance is less than or equal to sum of radii, they're colliding
        return distance <= radii_sum