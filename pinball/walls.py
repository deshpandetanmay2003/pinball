"""walls class"""
import pygame
class Walls():
    def __init__(self, height: float, width: float, thickness: int) -> None:
        self.height: float = height
        self.width: float = width
        self.thickness: int = thickness
    def next(self, screen):
        pygame.draw.rect(screen, pygame.Color("#eba0ac"), pygame.Rect(0, 0, self.width, self.height), self.thickness)
        return self
    def collide(self, ball):
        if ball.position.x < ball.radius + self.thickness:
            ball.velocity.x *= -1
            ball.position.x = self.thickness + ball.radius
        if ball.position.x > self.width - ball.radius - self.thickness:
            ball.velocity.x *= -1
            ball.position.x = self.width - ball.radius - self.thickness
        if ball.position.y < ball.radius*4 + self.thickness:
            ball.velocity.y *= -1
        if ball.position.y > self.height - ball.radius*4 + self.thickness:
            ball.position.y = self.height - ball.radius*4 + self.thickness
            ball.velocity.y *= -1
        return self
