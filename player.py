from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_TURN_SPEED
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    #rotate the player by a certain amount based on the turn speed and delta time
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
        # unit vector pointing straight down from (0, 0) to (0, 1). Rotating in the same direction as the player rotation, so that it always points in the direction the player is facing
        unit_vector  = pygame.Vector2(0, 1).rotate(self.rotation)
        rotated_unit_vector_wspeed = unit_vector* PLAYER_SPEED * dt
        # Added forward vector to the player position, so that it moves in the direction it is facing
        self.position += rotated_unit_vector_wspeed