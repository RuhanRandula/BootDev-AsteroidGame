from typing import override

from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        
    @override
    def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)
            
            
    @override
    def update(self, dt):
            self.position += self.velocity * dt