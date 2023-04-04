"""here we make the program"""
import pygame
import neat
import time
from pinball.ball import Ball
from pinball.walls import Walls

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

BORDER_THICKNESS = 3

BALL_RADIUS = 3

BACKGROUND_COLOR = (30, 30, 46)

def main():
    """the main function
    this is imported in the __main__ file
    the __main__ file is the one that is run when we run it using python -m"""

    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Enter Coordinates!')
    font = pygame.font.Font(pygame.font.get_default_font(), 10)
    clock = pygame.time.Clock()
    ball = Ball([WINDOW_WIDTH/2, 0], BALL_RADIUS)
    walls = Walls(WINDOW_HEIGHT, WINDOW_WIDTH, BORDER_THICKNESS)
    while True:
        screen.fill(BACKGROUND_COLOR)
        ball.next(screen)
        walls.collide(ball).next(screen)
        clock.tick(30)
        pygame.display.update()
