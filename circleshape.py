from typing import override

import pygame
from constants import LINE_WIDTH

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

    @override
    def draw(self, screen):
        # must override
        pygame.draw.polygon(screen, "white", self.triangle(), width=LINE_WIDTH)

    def update(self, dt):
        # must override
        pass
    
    #Collision logic(if distance is less than or equal to r1 + r2, then they are colliding)
    def collides_with(self, other):
        # is_hit = False
        # if isinstance(other, CircleShape):
        #    distance = self.position.distance_to(other.position)
        #    if distance <= self.radius + other.radius:
        #        is_hit = True
        # return is_hit
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
        