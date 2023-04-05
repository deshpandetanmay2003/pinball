"""obstacle class"""
import pygame
class Obstacle():
    def __init__(self, point1: tuple[float, float], point2: tuple[float, float], thickness: int, trampoline: bool) -> None:
        self.points: list[pygame.math.Vector2] = [pygame.math.Vector2(point1), pygame.math.Vector2(point2)]
        self.thickness: int = thickness
        self.trampoline = trampoline
    def next(self, screen):
        pygame.draw.line(screen, pygame.Color("#eba0ac"), self.points[0], self.points[1], self.thickness)
        return self
    def collide(self, ball):
        ab = self.points[1] - self.points[0]
        ac = pygame.math.Vector2(tuple(map(lambda i: self.points[0][i] - ball.position[i], [0, 1])))
        bc = pygame.math.Vector2(tuple(map(lambda i: self.points[1][i] - ball.position[i], [0, 1])))
        distance = ab.cross(ac)/ab.length()

        # reflect
        if abs(distance) < ball.radius + self.thickness and (ab.dot(ac) < 0) == (ab.dot(bc) > 0):
            v = pygame.math.Vector2(*ball.velocity)
            n = ab.rotate(90).normalize()
            vdn = v.dot(n)
            ball.velocity = v - 2 * vdn * n

            # clip
            perp_dir = (ball.velocity - v).normalize()
            ball.position -= perp_dir*distance - perp_dir*self.thickness
            if self.trampoline == True:
                ball.velocity = ball.velocity.normalize() * ball.maximum_velocity

        return self
