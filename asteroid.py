import pygame
import random
from bolt import Bolt
from circleshape import CircleShape 
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        
    def impact(self, bolt: Bolt):
        velocity = bolt.velocity
        x, y = self.position

        bolt.kill()
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS: return

        angle = random.uniform(20, 50)

        asteroid = Asteroid(x, y, self.radius * 0.6)
        fracture = Asteroid(x, y, self.radius * 0.4)

        asteroid.velocity = velocity.rotate(0+angle) * 0.33
        fracture.velocity = velocity.rotate(0-angle) * 0.33
