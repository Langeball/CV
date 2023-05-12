import pygame
from collections import deque
from random import randrange
from sys import exit

def main():
    global direction, head, food_location

    # Prevent game starting immediately
    pygame.display.set_caption("Press any key to start")
    pygame.display.update()
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over(False)
            # Start game if any button is pressed
            elif event.type == pygame.KEYDOWN:
                pause = False
    # Game loop
    while True:
        # Pygame logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over(False)

            # Check for key press
            if event.type == pygame.KEYDOWN:
                # Check which key was pressed and prevent moving opposite direction
                if event.key == pygame.K_LEFT and direction != "right":
                    direction = "left"
                elif event.key == pygame.K_RIGHT and direction != "left":
                    direction = "right"
                elif event.key == pygame.K_DOWN and direction != "up":
                    direction = "down"
                elif event.key == pygame.K_UP and direction != "down":
                    direction = "up"

        # Game logic
        head = move_head()
        collision()
        draw_cube(*head)
        if not food_location:
            food_location = place_food()
        else:
            delete_tail()

        # Update score
        pygame.display.set_caption(f"Current score: {score}")

        # Update screen and frame-rate
        pygame.display.update()
        clock.tick(frame_rate)

def draw_cube(x, y):
    """Draw snake and add coords to hashmap for collision detection"""
    pygame.draw.rect(screen, cube_colour, (x, y, cube_size, cube_size))
    snake[(x, y)] = (x, y)


def delete_tail():
    """Oldest part of snake body becomes new tail, old tail erased."""
    global tail
    x, y = tail
    pygame.draw.rect(screen, background_colour, (x, y, cube_size, cube_size))
    tail = body.popleft()

    # For collision detection
    if (x, y) in snake:
        del snake[(x, y)]

def collision():
    """Detects border, food and snake body collision."""
    global food_location, score
    # If head eats food
    if head == food_location:
        food_location = None
        score += 1

    # Border control
    x, y = head
    if (x < 0 or x >= board_size) or (y < 0 or y >= board_size):
        game_over()

    # Snake collision
    if head in snake:
        game_over()

    return True

def place_food():
    """Using a count we prevent the possibility of bad RNG on food placement"""
    count = 0
    while count < 100:  # To prevent possible lag, we allow the possibility of no food for a while
        x, y = randrange(0, board_size, cube_size), randrange(0, board_size, cube_size)
        # Prevent food from being placed inside snake
        if (x, y) not in snake:
            pygame.draw.rect(screen, food_colour, (x, y, cube_size, cube_size))
            return x, y
        count += 1

def move_head():
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

def game_over(show_score=True):
    if show_score:
        font = pygame.font.Font(None, 36)
        text = f"Final score: {score}"
        text_surface = font.render(text, True, (255, 255, 255))
        text_x = board_size // 2 - text_surface.get_width() // 2
        text_y = 50
        screen.blit(text_surface, (text_x, text_y))
        pygame.display.set_caption("Close window and try again!")
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over(False)

    pygame.quit()
    exit()

# Setting up pygame board/screen
pygame.init()
board_size = 400  # x and y value
screen = pygame.display.set_mode((board_size, board_size))
background_colour = "black"
clock = pygame.time.Clock()  # Control frame-rate
frame_rate = 10

# Snake logic
cube_size = 25  # x and y value
cube_colour = "red"
head = (board_size // 2, board_size // 2)  # Middle of board
tail = ((board_size // 2) - (cube_size * 2), board_size // 2)  # 2 cubes behind head
body = deque([((board_size // 2) - cube_size, board_size // 2), ])  # 1 cube behind head
snake = {}
direction = "right"
# Draw the starting 3 length snake
for e in (tail, body[0], head):
    draw_cube(*e)

# Snake food
food_colour = "green"
food_location = place_food()

# Score
score = 0

if __name__ == "__main__":
    main()
    
