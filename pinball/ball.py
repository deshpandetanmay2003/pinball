"""ball class"""
import pygame
import random
from math import sin, cos
class Ball():
    def __init__(self, position: list[float], radius: int) -> None:
        self.acceleration: list[float] = [0, 5]
        self.velocity: list[float] = [random.randint(5, 10)*random.choice((-1, 1)), 0]
        self.position: list[float] = position
        self.radius: int = radius

    def next(self, screen):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        pygame.draw.circle(screen, pygame.Color("#eba0ac"), tuple(map(lambda x: x+self.radius, self.position)), self.radius * 2)
        return self
