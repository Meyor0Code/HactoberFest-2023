import random
import pygame
import time
import sys

# I define the game window size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
  MOVE_SNAKE(SNAKE_BODY)
# I define the snake's initial position and size
SNAKE_X = 100
SNAKE_Y = 100
SNAKE_SIZE = 10

# I define the snake's initial direction
SNAKE_DIRECTION = "right"

# I define the food's initial position
FOOD_X = random.randint(0, SCREEN_WIDTH - SNAKE_SIZE)
FOOD_Y = random.randint(0, SCREEN_HEIGHT - SNAKE_SIZE)

# I initialize the game window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Here, we start the game loop
while True:

    # we also check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # here handles key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                SNAKE_DIRECTION = "up"
            elif event.key == pygame.K_DOWN:
                SNAKE_DIRECTION = "down"
            elif event.key == pygame.K_LEFT:
                SNAKE_DIRECTION = "left"
            elif event.key == pygame.K_RIGHT:
                SNAKE_DIRECTION = "right"

    # here is the direction of the snake defined
    if SNAKE_DIRECTION == "up":
        SNAKE_Y -= SNAKE_SIZE
    elif SNAKE_DIRECTION == "down":
        SNAKE_Y += SNAKE_SIZE
    elif SNAKE_DIRECTION == "left":
        SNAKE_X -= SNAKE_SIZE
    elif SNAKE_DIRECTION == "right":
        SNAKE_X += SNAKE_SIZE

    # we also check if the snake has collided with itself or the edges of the screen
    if SNAKE_X < 0 or SNAKE_X >= SCREEN_WIDTH or SNAKE_Y < 0 or SNAKE_Y >= SCREEN_HEIGHT:
        # The snake must not collide with the screen nor itself, else Game over!!!
        print("Game over!")
        pygame.quit()
        sys.exit()

    # check if the snake has collided with the food
    if SNAKE_X == FOOD_X and SNAKE_Y == FOOD_Y:
        # The snake has eaten the food!
        # if the snake eats the food, it size increases by 1 unit
        SNAKE_SIZE += 1

        # now we randomly generate a new position for the food
        FOOD_X = random.randint(0, SCREEN_WIDTH - SNAKE_SIZE)
        FOOD_Y = random.randint(0, SCREEN_HEIGHT - SNAKE_SIZE)

    # Draw the snake
    pygame.draw.rect(screen, (0, 255, 0), (SNAKE_X, SNAKE_Y, SNAKE_SIZE, SNAKE_SIZE))

    # Draw the food
    pygame.draw.rect(screen, (255, 0, 0), (FOOD_X, FOOD_Y, SNAKE_SIZE, SNAKE_SIZE))

    # Update the display
    pygame.display.flip()

