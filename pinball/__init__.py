"""here we make the program"""
import time
import pygame
import neat
from pinball.ball import Ball
from pinball.walls import Walls
from pinball.obstacle import Obstacle

FPS = 120

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 300

BORDER_THICKNESS = 3

OBSTACLE_THICKNESS = 10

BALL_RADIUS = 5
MAXIMUM_VELOCITY = 200

BACKGROUND_COLOR = (30, 30, 46)

def main():
    """the main function
    this is imported in the __main__ file
    the __main__ file is the one that is run when we run it using python -m"""

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Pinball Wizard')
    font = pygame.font.Font(pygame.font.get_default_font(), 10)
    clock = pygame.time.Clock()
    ball = Ball([WINDOW_WIDTH/2, 0], BALL_RADIUS, MAXIMUM_VELOCITY)
    walls = Walls(WINDOW_HEIGHT, WINDOW_WIDTH, BORDER_THICKNESS)
    obstacle = Obstacle((50, 450), (250, 450), OBSTACLE_THICKNESS, True)
    frame_time = 1
    while True:
        screen.fill(BACKGROUND_COLOR)
        ball.next(screen, frame_time)
        walls.collide(ball).next(screen)
        obstacle.collide(ball).next(screen)
        pygame.display.update()
        frame_time = clock.tick(FPS)
