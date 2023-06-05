import pygame
from sys import exit

"""
A functional/visual representation of the RelativeCamera template found in the functions.py file.
This code will initiate a matrix with coordinates relative to a given position in said matrix.
Allows the 'camera' in a game to follow and stay centered on the player character.

How to use:
"Player character" is represented by a small green line. Control using arrow keys.
Control level of zoom with numerical keys 1 and 2.

Red lines are drawn from each node in matrix to center/character, to better illustrate what is happening.

Here is a list of settings that can be changed and what they do:
  matrix_w: Width of the matrix. Controls the size of the "game world".
  matrix_h: Height of the matrix. Controls the size of the "game world".
  board_width: Width of the game window
  board_height: Height of the game window
  sprite_size: Essentially controls the level of zoom.
  char_pos: Position of the "player character" in the matrix. Default is set to center of the matrix
"""

# Create matrix
matrix_one = []
matrix_w = 20
matrix_h = 20
for _ in range(matrix_h):
    matrix_one.append([None] * matrix_w)

# Board/screen information
board_width = 1280
board_height = 720
sprite_size = 25
matrix_center_pos = matrix_h / 2, matrix_w / 2
char_pos = matrix_center_pos

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((board_width, board_height))
clock = pygame.time.Clock()
frame_rate = 60

def offset_center(position):
    """Offsets coordinates of everything in a matrix relative to a given position"""
    h, w = position
    start_h = (board_height / 2) - (sprite_size*h)
    start_w = (board_width / 2) - (sprite_size*w)
    reset_w = start_w
    for i_row, row in enumerate(matrix_one):
        for i_num, num in enumerate(row):
            matrix_one[i_row][i_num] = [start_w, start_h]
            start_w += sprite_size
        start_h += sprite_size
        start_w = reset_w
    #matrix_one[h][w] = "Character"

# Build matrix
offset_center(char_pos)
#print(matrix_one)

# Game loop
while True:
    # Erase screen each loop
    screen.fill((0, 0, 0))
    
    # Listen for input (keyboard, mouse etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            # Movement
            if event.key == pygame.K_LEFT:
                char_pos = char_pos[0], char_pos[1] - 1
                offset_center(char_pos)
            elif event.key == pygame.K_RIGHT:
                char_pos = char_pos[0], char_pos[1] + 1
                offset_center(char_pos)
            elif event.key == pygame.K_DOWN:
                char_pos = char_pos[0] + 1, char_pos[1]
                offset_center(char_pos)
            elif event.key == pygame.K_UP:
                char_pos = char_pos[0] - 1, char_pos[1]
                offset_center(char_pos)
            # Zoom
            elif event.key == pygame.K_1:
                if sprite_size > 10:
                    sprite_size -= 10
                    offset_center(char_pos)
            elif event.key == pygame.K_2:
                if sprite_size < 50:
                    sprite_size += 10
                    offset_center(char_pos)
            #print(matrix_one)

    # Draw matrix grid
    line_colour = (255, 0, 0)  # Max 255, min 0
    for rows in matrix_one:
        for col in rows:
            xy = (0, 0) if not col else col
            pygame.draw.line(surface=screen,
                             color=line_colour,
                             start_pos=xy,
                             end_pos=(board_width / 2, board_height / 2),
                             width=2)

    # Draw crosshair at center of screen
    line_colour = (0, 255, 0)
    pygame.draw.line(surface=screen,
                     color=line_colour,
                     start_pos=((board_width / 2) - 6, board_height / 2),
                     end_pos=((board_width / 2) + 7, board_height / 2),
                     width=2)
    pygame.draw.line(surface=screen,
                     color=line_colour,
                     start_pos=((board_width / 2), (board_height / 2) - 6),
                     end_pos=((board_width / 2), (board_height / 2) + 7),
                     width=2)
    

    # Pygame updates
    pygame.display.update()
    clock.tick(frame_rate)
