from typing import Tuple
import pygame
from pygame.surface import Surface

def pong_game() -> None:
    print("Start Pong Game")
    pygame.init()
    # Display Values
    width: int = 1000
    height: int = 600
    display_size: Tuple[int, int] = (width, height)
    new_display: Surface = pygame.display.set_mode(display_size)
    pygame.display.set_caption("Pong Game")
    run: bool = True
    # Colors
    blue : Tuple[int, int, int] = (0, 0, 255)
    red: Tuple[int, int, int] = (255, 0, 0)
    black: Tuple[int, int, int]= (0, 0, 0)
    white: Tuple[int, int, int] = (255, 255, 255)
    # Ball
    radius: int = 15
    ball_x: float = width / 2 - radius
    ball_y: float = height / 2 - radius
    ball_coord: Tuple[float, float] = (ball_x, ball_y)
    vel_x: float = 0.5
    vel_y: float = 0.5
    # Paddles
    paddle_width: int = 20
    paddle_height: int = 120
    paddle_y = height / 2 - paddle_height / 2
    paddle_y1 = paddle_y
    paddle_x = 100 - paddle_width / 2
    paddle_x1 = width - (100 - paddle_width / 2)
    paddle_vel = 0
    paddle_vel1 = paddle_vel
    #Test Print
    print(paddle_x, paddle_x1)
    print(paddle_y, paddle_y1)
    # Game
    while run:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
                continue
        pygame.draw.circle(new_display, blue, ball_coord, radius)
        pygame.draw.rect(new_display, red, pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height))
        pygame.draw.rect(new_display, red, pygame.Rect(paddle_x1, paddle_y1, paddle_width, paddle_height))
        pygame.display.update()
    
        
