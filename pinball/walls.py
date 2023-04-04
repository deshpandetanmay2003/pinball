"""walls class"""
import pygame
import random
class Walls():
    def __init__(self, height: float, width: float, thickness: int) -> None:
        self.height: float = height
        self.width: float = width
        self.thickness: int = thickness
    def next(self, screen):
        pygame.draw.rect(screen, pygame.Color("#eba0ac"), pygame.Rect(0, 0, self.width, self.height), self.thickness)
        return self
    def collide(self, ball):
        if ball.position[0] < ball.radius*2 + self.thickness or ball.position[0] > self.width - ball.radius*2 + self.thickness:
            ball.velocity[0] *= -1
        if ball.position[1] < ball.radius*2 + self.thickness:
            ball.velocity[1] *= -1
        if ball.position[1] > self.height - ball.radius*2 + self.thickness:
            ball.position[1] = self.height - ball.radius*2 + self.thickness
            ball.velocity[1] *= -1
        return self
