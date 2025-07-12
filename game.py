import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 560, 620
TILE_SIZE = 20
FPS = 10
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Pac-Man")
clock = pygame.time.Clock()

# Maze layout (1 = wall, 0 = dot)
maze = [
    "11111111111111111111",
    "10000000001100000001",
    "10111111101101111101",
    "10100000100001000001",
    "10101110111101110101",
    "10001000000000001001",
    "11101111101111101111",
    "10000000001000000001",
    "10111111111111111101",
    "10000000000000000001",
    "11111111111111111111"
]

# Convert maze to list of lists
maze = [list(row) for row in maze]

# Player starting position
player_x, player_y = 1, 1

def draw_maze():
    for y, row in enumerate(maze):
        for x, tile in enumerate(row):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if tile == "1":
                pygame.draw.rect(screen, BLUE, rect)
            elif tile == "0":
                pygame.draw.circle(screen, WHITE, rect.center, 3)

def draw_player(x, y):
    center = (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2)
    pygame.draw.circle(screen, YELLOW, center, TILE_SIZE // 2 - 2)

def move_player(dx, dy):
    global player_x, player_y
    new_x = player_x + dx
    new_y = player_y + dy
    if maze[new_y][new_x] != "1":
        player_x, player_y = new_x, new_y
        if maze[player_y][player_x] == "0":
            maze[player_y][player_x] = " "

# Game loop
while True:
    screen.fill(BLACK)
    draw_maze()
    draw_player(player_x, player_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        move_player(-1, 0)
    elif keys[pygame.K_RIGHT]:
        move_player(1, 0)
    elif keys[pygame.K_UP]:
        move_player(0, -1)
    elif keys[pygame.K_DOWN]:
        move_player(0, 1)

    pygame.display.flip()
    clock.tick(FPS)



