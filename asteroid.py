import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_asteroid = random.uniform(20, 50)
        asteroid_velocity_one = self.velocity.rotate(random_asteroid)
        asteroid_velocity_two = self.velocity.rotate(-random_asteroid)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_velocity_one *= 1.2
        asteroid_velocity_two *= 1.2

        # Use self.position.x and self.position.y instead
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        # Assign the velocities
        first_asteroid.velocity = asteroid_velocity_one
        second_asteroid.velocity = asteroid_velocity_two
        
