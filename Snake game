import pygame
from collections import deque
import random
# import asyncio

def main():
    """Game loop"""
    global direction
    global head

    while True:
        # Pygame logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise StopIteration

            # Check for key press
            if event.type == pygame.KEYDOWN:
                # Check which key was pressed
                if event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                elif event.key == pygame.K_UP:
                    direction = "up"

        # Game logic
        head = control()
        if collision():
            delete_tail(*tail)
        draw_cube(*head)

        # Update screen and frame-rate
        pygame.display.update()
        clock.tick(frame_rate)

def draw_cube(x, y):
    """Draw snake and add coords to hashmap for collision detection"""
    pygame.draw.rect(screen, cube_colour, (x, y, cube_size, cube_size))
    snake[(x, y)] = (x, y)


def delete_tail(x, y):
    """Oldest part of snake body becomes new tail, old tail erased."""
    global tail
    tail = body.popleft()
    pygame.draw.rect(screen, background_colour, (x, y, cube_size, cube_size))

    # For collision detection
    if (x, y) in snake:
        del snake[(x, y)]

def collision():
    """Detects border, food and snake body collision. TODO: Move food collision to its own func"""
    global food_location
    # If head eats food, returning False prevents tail deletion
    if head == food_location:
        food_location = place_food()
        return False

    # Border control
    if board+cube_size in head or -cube_size in head:
        pygame.quit()
        raise StopIteration

    # Snake collision
    if head in snake:
        pygame.quit()
        raise StopIteration

    return True

def place_food():
    """Randrange will eventually slow down game horrifically. TODO: asyncio it"""
    while True:
        x, y = random.randrange(0, board, cube_size), random.randrange(0, board, cube_size)
        # Prevent food from being placed inside snake
        if (x, y) not in snake:
            break
    pygame.draw.rect(screen, food_colour, (x, y, cube_size, cube_size))
    return x, y

def control():
    """Depending on direction, add/sub to either x or y. Change direction"""
    # Old head becomes part of body
    body.append(head)

    x, y = head
    if direction == "left":
        x -= cube_size
    elif direction == "right":
        x += cube_size
    elif direction == "down":
        y += cube_size
    elif direction == "up":
        y -= cube_size
    return x, y

# Setting up pygame board/screen
pygame.init()
board = 500  # x and y value
screen = pygame.display.set_mode((board, board))
background_colour = "black"
clock = pygame.time.Clock()  # Control frame-rate
frame_rate = 10

# Snake logic
cube_size = 25  # x itself
cube_colour = "red"
head = (board//2, board//2)  # Middle of board
tail = ((board//2)-(cube_size*2), board//2)  # 2 cubes behind head
body = deque([ ((board // 2) - cube_size, board // 2) ])  # 1 cube behind head
snake = {}
direction = "right"
# Draw the starting 3 length snake
for e in (tail, body[0], head):
    draw_cube(*e)

# Snake food
food_colour = "green"
food_location = place_food()

if __name__ == "__main__":
    main()
