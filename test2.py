# Import necessary libraries
import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Street Fighter 1v1")

# Set up the game clock
clock = pygame.time.Clock()

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define some game variables
player1_x = 50
player1_y = 300
player2_x = 700
player2_y = 300

# Set up the game loop
game_over = False
while not game_over:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Update game logic
    # TODO: add game logic here

    # Draw the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [player1_x, player1_y, 50, 50])
    pygame.draw.rect(screen, BLACK, [player2_x, player2_y, 50, 50])

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()