"""ball class"""
import pygame
import random
from math import sin, cos
class Ball():
    def __init__(self, position: list[float], radius: int, maximum_velocity: int) -> None:
        self.acceleration: pygame.math.Vector2 = pygame.math.Vector2(0, 5)
        self.velocity: pygame.math.Vector2 = pygame.math.Vector2(random.randint(5, 10)*random.choice((-1, 1)), 0)
        self.maximum_velocity: int = maximum_velocity
        self.position: pygame.math.Vector2 = pygame.math.Vector2(*position)
        self.radius: int = radius

    def next(self, screen, dt):
        if self.velocity.length() > self.maximum_velocity:
            self.velocity = self.velocity.normalize() * self.maximum_velocity
        self.velocity += self.acceleration
        self.position += self.velocity / dt
        pygame.draw.circle(screen, pygame.Color("#eba0ac"), tuple(map(lambda x: x+self.radius, self.position)), self.radius * 2)
        return self
