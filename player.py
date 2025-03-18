from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0  # Initialize the cooldown timer to 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Decrease the cooldown timer by dt
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Only shoot if the cooldown timer is 0 or less
        if self.shoot_cooldown <= 0:
            new_shot = Shot(self.position, self.rotation)
            # Reset the cooldown timer
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

    def collides_with(self, other):
        # For collision with shots (which are circles)
        if isinstance(other, Shot):
            return super().collides_with(other)
        
        # Get the triangle points
        triangle_points = self.triangle()
        
        # For collision with asteroids (which are circles)
        # Check if any point of the triangle is inside the asteroid
        for point in triangle_points:
            if (point - other.position).length() <= other.radius:
                return True
            
        # Check if the asteroid's center is inside the triangle
        def point_in_triangle(p, triangle):
            def sign(p1, p2, p3):
                return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)
            
            d1 = sign(p, triangle[0], triangle[1])
            d2 = sign(p, triangle[1], triangle[2])
            d3 = sign(p, triangle[2], triangle[0])
            
            has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
            has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
            
            return not (has_neg and has_pos)
        
        if point_in_triangle(other.position, triangle_points):
            return True
            
        # Check if any of the triangle's edges intersect with the asteroid's circle
        def line_circle_intersection(p1, p2, circle_pos, circle_radius):
            segment = p2 - p1
            segment_length = segment.length()
            if segment_length == 0:
                return (p1 - circle_pos).length() <= circle_radius
                
            t = max(0, min(1, ((circle_pos - p1).dot(segment)) / (segment_length * segment_length)))
            projection = p1 + segment * t
            return (projection - circle_pos).length() <= circle_radius
            
        for i in range(3):
            if line_circle_intersection(triangle_points[i], triangle_points[(i + 1) % 3], other.position, other.radius):
                return True
                
        return False
