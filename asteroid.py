from typing import override
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import pygame
import random
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        
    @override
    def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)
            
            
    @override
    def update(self, dt):
            self.position += self.velocity * dt
            
    def split(self,):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        #pick a random angle for the asteroid split
        angle = random.uniform(20, 50)
        #create new velocity vectors by rotating the current one
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        #creating two new offspring asteroids at the same position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = self.velocity * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = self.velocity * 1.2      