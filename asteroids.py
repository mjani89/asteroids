from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        rand_angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(rand_angle)
        new_vector2 = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split1 = Asteroid(self.position.x, self.position.y, new_radius)
        split2 = Asteroid(self.position.x, self.position.y, new_radius)

        split1.velocity = new_vector1 * 1.2
        split2.velocity = new_vector2 * 1.2

        self.kill()
