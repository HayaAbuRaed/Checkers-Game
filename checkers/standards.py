import pygame

# sizes
WIDTH, HEIGHT = 770, 770
COLS, ROWS = 8, 8

# squares:
# to devide the space evenly
SQ_SIZE = WIDTH // COLS   # square => 100, will represent: width-of-squar = 100 and height-of-square = 100


# colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (64, 51, 10)
OFFWHITE = (234, 215, 155)
GREEN = (15, 156, 13)
BLUE = (51, 92, 232)

# crown
CROWN = pygame.transform.scale(pygame.image.load('../assets/crown2.png'), (44,25))