from typing import Tuple
import pygame
from pygame.surface import Surface
from ColorValue import ColorValue

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
    blue: ColorValue = (0, 0, 255)
    red: ColorValue = (255, 0, 0)
    black: ColorValue = (0, 0, 0)
    white: ColorValue = (255, 255, 255)
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
    paddle_left_y: float = height / 2 - paddle_height / 2
    paddle_right_y: float = paddle_left_y
    paddle_left_x: float = 100 - paddle_width / 2
    paddle_right_x: float = width - (100 - paddle_width / 2)
    paddle_left_vel: float = 0
    paddle_right_vel: float = 0
    #Test Print
    print("Left Paddle", paddle_left_x, paddle_left_y)
    print("Right Paddle", paddle_right_x, paddle_right_y)
    # Game
    while run:
        # Black Screen to Show different Tempos Game
        new_display.fill(black)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
                continue
            if i.type == pygame.KEYDOWN:
                # Right Paddle Goes Up with Up Arrow Key
                if i.key == pygame.K_UP:
                    paddle_right_vel = -0.7
                # Right Paddle Goes Down Arrow Key
                if i.key == pygame.K_DOWN:
                    paddle_right_vel = 0.7
                # Left Paddle Goes Up with "W" key
                if i.key == pygame.K_w:
                    paddle_left_vel = -0.7
                # Left Paddle Goes Up with "S" key
                if i.key == pygame.K_s:
                   paddle_left_vel = 0.7
            if i.type == pygame.KEYUP:
                paddle_right_vel = 0
                paddle_left_vel = 0        
        # Bounce Ball Y Axis Out Bounds
        if (ball_y <= 0 + radius) or (ball_y >= height - radius):
            vel_y = vel_y * -1
        # Reset Serve Game X Axis Out Bounds Right
        if ball_x >= (width - radius):
            ball_x = width / 2 - radius
            ball_y = height / 2 - radius
            vel_x = 0.5 
            vel_y = 0.5
            vel_x = vel_x * -1
            vel_y = vel_y * -1
        # Reset Serve Game X Axis Out Bounds Left
        if ball_x <= (0 + radius):
            ball_x = width / 2 - radius
            ball_y= height / 2 - radius
            vel_x = 0.5 
            vel_y = 0.5
        # Paddle Movements Out Bounds Controls
        ## Paddle Left Down Bounds
        if paddle_left_y >= height - paddle_height:
            paddle_left_y = height - paddle_height
        ## Paddle Left Up Bounds
        if paddle_left_y <= 0:
            paddle_left_y = 0
        ## Paddle Right Down Bounds
        if paddle_right_y >= height - paddle_height:
            paddle_right_y = height - paddle_height
        ## Paddle Right Up Bounds
        if paddle_right_y <= 0:
            paddle_right_y = 0
        #Paddle Collisions with Ball
        ## Right Paddle
        if (ball_x >= paddle_right_x) and (ball_x <= paddle_right_x + paddle_width):
            if (ball_y >= paddle_right_y) and (ball_y <= paddle_right_y + paddle_height):
                ball_x = paddle_right_x
                vel_x = vel_x * -1
        # Left Paddle
        if (ball_x >= paddle_left_x) and (ball_x <= paddle_left_x + paddle_width):
            if (ball_y >= paddle_left_y) and (ball_y <= paddle_left_y + paddle_height):
                ball_x = paddle_left_x + paddle_width
                vel_x = vel_x * -1
        # Movements
        ## Movement Paddle
        ### Left Paddle
        paddle_left_y = paddle_left_y + paddle_left_vel
        ### Right Paddle
        paddle_right_y = paddle_right_y + paddle_right_vel
        ## Movement Ball
        ball_x = ball_x + vel_x
        ball_y = ball_y + vel_y
        ball_coord = (ball_x, ball_y)
        # Pong Objects
        ## Ball
        pygame.draw.circle(new_display, blue, ball_coord, radius)
        ## Left Paddle
        pygame.draw.rect(new_display, red, pygame.Rect(paddle_left_x, paddle_left_y, paddle_width, paddle_height))
        ## Right Paddle
        pygame.draw.rect(new_display, red, pygame.Rect(paddle_right_x, paddle_right_y, paddle_width, paddle_height))
        # Pong Update Game
        pygame.display.update()
    
        
