import sys
import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from shot import Shot
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init()
    pygame.display.set_caption("Asteroids")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)

    asteroid_field = AsteroidField()
    
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()


        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.is_colliding_with(player):
                print("Game over!")
                sys.exit()

        screen.fill((0, 0, 0))
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()