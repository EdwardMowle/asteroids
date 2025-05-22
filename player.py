import pygame
from circleshape import CircleShape 
from shot import Shot
from constants import SCREEN_WIDTH, PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.integrity = 100
        self.rotation = 0
        
        self.weapon_overheated = False
        self.weapon_heat = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def __weapon_cooling(self, dt):
        cool_rate = 0.3 if self.weapon_overheated else 1
        
        self.weapon_heat = min(max(0, self.weapon_heat - dt * cool_rate), 1)

        if (self.weapon_heat >= 1): self.weapon_overheated = True
        elif (self.weapon_heat == 0): self.weapon_overheated = False

    def __weapon_overheat(self):
        # TODO: Burn/damage energy shield.

        self.weapon_overheated = True
        self.weapon_heat = 1

        print("overheat")

    def __weapon_fire(self):
        self.weapon_heat += 0.33

        if self.weapon_heat >= 1:
            self.__weapon_overheat()

        Shot(
            x= self.position.x, 
            y= self.position.y, 
            rotation = self.rotation,
            primed = self.weapon_heat == 0
        )

    def __weapon_misfire(self):
        # TODO: Animate to indicate failed shot.

        print("misfire")

    def shoot(self):
        if self.weapon_overheated:
            self.__weapon_misfire()
        else:
            self.__weapon_fire()


    def draw(self, screen):
        pygame.draw.polygon(
            surface = screen,
            color = (255, 255, 255),
            points = self.triangle(),
            width = 2
        )

        # UI Extract
        width = SCREEN_WIDTH - 500
        shade = 255
        # shade = 255 /100 + 155 * (1-self.weapon_)

        pygame.draw.rect(
            surface = screen,
            color = (shade, shade, shade, 255),
            rect = (250, 250, width, 30)
        )

        heat_width = (width - 4) * (1 if self.weapon_overheated else self.weapon_heat)
        heat_x = (SCREEN_WIDTH - heat_width) / 2

        pygame.draw.rect(screen, "red", (heat_x, 252, heat_width, 26))

    def update(self, dt):
        self.__weapon_cooling(dt)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
