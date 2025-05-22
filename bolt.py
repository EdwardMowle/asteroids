import pygame
from circleshape import CircleShape 
from constants import BOLT_RADIUS, BOLT_SPEED

class Bolt(CircleShape):
    def __init__(self, x, y, rotation, primed = False):
        super().__init__(x, y, BOLT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * BOLT_SPEED
        self.primed = primed

    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(
            surface = screen,
            color = 'blue' if self.primed else 'white',
            center = self.position,
            radius = self.radius,
            width = 2
        )
        