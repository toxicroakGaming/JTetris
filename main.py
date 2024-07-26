#init
import pygame
import math
import random

pygame.init()

# Set up the window dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Set a title for the window
pygame.display.set_caption("Tetris")
startX = 0
startY = 0
#the size of each block
space = 30
#makes it easier on the eyes
incrX = [startX, startX + space, startX + (space * 2), startX + (space * 3)]
incrY = [startY, startY + space, startY + (space * 2), startY + (space * 3)]
I = [(incrX[0], startY), (incrX[0], startY + (space * 4)), (startX + space, startY + (space * 4)), (startX + space, startY), (startX, startY)]
T = [(incrX[0], startY), (incrX[1], startY), (startX + space, startY + space), (startX + (space * 2), startY + space), (startX + (space * 2), startY + (space * 2)), (startX - space, startY + (space * 2)), (startX - space, startY + space), (startX, startY + space), (startX, startY)]
O = [(incrX[0], startY), (incrX[2], startY), (startX + (space * 2), startY + (space * 2)), (startX, startY + (space * 2)), (startX, startY)]
J = [(incrX[0], incrY[0]), (incrX[0], incrY[1]), (incrX[1], incrY[1]), (incrX[1], incrY[3]), (incrX[2], incrX[3]), (incrX[2], incrX[0]), (incrX[0], incrY[0])]
L = [(incrX[0], incrY[0]), (incrX[0], incrY[3]), (incrX[1], incrY[3]), (incrX[1], incrY[1]), (incrX[2], incrY[1]), (incrX[2], incrY[0]), (incrX[0], incrY[0])]
S = [(incrX[0], incrY[0]), (incrX[0], incrY[1]), (incrX[1], incrY[1]), (incrX[1], incrY[2]),(incrX[3], incrY[2]),(incrX[3], incrY[1]),(incrX[2], incrY[1]),(incrX[2], incrY[0]),(incrX[0], incrY[0])]
Z = [(incrX[0], incrY[2]), (incrX[2], incrY[2]), (incrX[2], incrY[1]), (incrX[3], incrY[1]),(incrX[3], incrY[0]),(incrX[1], incrY[0]),(incrX[1], incrY[1]),(incrX[0], incrY[1]),(incrX[0], incrY[2])]
shapes = [I, T, O, J, L, S, Z]
active_shapes = []
dx = space * 2
dy = space
trans = [(x + dx, y + dy) for (x, y) in T]
dx += space * 2
transO = [(x + dx, y + dy) for (x, y) in O]
dx += space * 2
transJ = [(x + dx, y + dy) for (x, y) in J]
dx += space * 2
transL = [(x + dx, y + dy) for (x, y) in L]
dx += space * 2
transS = [(x + dx, y + dy) for (x, y) in S]
dx += space * 3
transZ = [(x + dx, y + dy) for (x, y) in Z]

def rotate_point(point, angle, pivot):
    """Rotate a point around a pivot."""
    s, c = math.sin(angle), math.cos(angle)
    px, py = pivot
    x, y = point
    # Translate point back to origin:
    x -= px
    y -= py
    # Rotate point
    x_new = x * c - y * s
    y_new = x * s + y * c
    # Translate point back
    x = x_new + px
    y = y_new + py
    return (x, y)

# Function to find the center of the polygon
def find_center(points):
    """Find the center (centroid) of a polygon."""
    x_list = [point[0] for point in points]
    y_list = [point[1] for point in points]
    _len = len(points)
    centroid_x = sum(x_list) / _len
    centroid_y = sum(y_list) / _len
    return (centroid_x, centroid_y)


running = True
angle = math.pi / 2
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if rot:
                    center = find_center(trans)
                    trans = [rotate_point(v, angle, center) for v in trans]
                    rot = False
            #pygame.draw.polygon(screen, (255, 51, 255), rotated_vertices)
    else:
        rot = True
    screen.fill((255, 255, 255))  # Fill the screen with white
    # Game logic and updates go here
    pygame.draw.polygon(screen, (102, 255, 255), I)
    pygame.draw.polygon(screen, (255, 51, 255), trans)
    pygame.draw.polygon(screen, (255, 255, 0), transO)
    pygame.draw.polygon(screen, (0, 0, 255), transJ)
    pygame.draw.polygon(screen, (255, 153, 51), transL)
    pygame.draw.polygon(screen, (51, 255, 51), transS)
    pygame.draw.polygon(screen, (255, 0, 0), transZ)
    # Rendering
    
    
    pygame.display.flip()    # Update the display


pygame.quit()

#function for the main game loop
def main_game():
    int shape_select = random.randint(0, 6)
    cur_shape = shape(0, 0, shapes[shape_select], get_name(shape_select))
    active_shapes.append(cur_shape)
    for sh in active_shapes:
        draw_shape(sh)
    

class shape:
    int startX
    int startY
    shape = []
    String shape_name
    def __init__(self, startX, startY, shape, shape_name):
        self.startX = startX
        self.startY = startY
        self.shape = shape
        self.shape_name = shape_name
    
    
def get_name(sel):
    if sel == 0:
        return "I"
    elif sel == 1:
        return "T"
    elif sel == 2:
        return "O"
    elif sel == 3:
        return "J"
    elif sel == 4:
        return "L"
    elif sel == 5:
        return "S"
    elif sel == 6:
        return "Z"
        
        
def draw_shape(sh):
    if sh.shape_name == "I":
        pygame.draw.polygon(screen, (102, 255, 255), sh)
    elif sh.shape_name == "T":
        pygame.draw.polygon(screen, (255, 51, 255), sh)
    elif sh.shape_name == "O":
        pygame.draw.polygon(screen, (255, 255, 0), transO)
    elif sh.shape_name == "J":
        pygame.draw.polygon(screen, (0, 0, 255), transJ)
    elif sh.shape_name == "L":
        pygame.draw.polygon(screen, (255, 153, 51), transL)
    elif sh.shape_name == "S":
        pygame.draw.polygon(screen, (51, 255, 51), transS)
    elif sh.shape_name == "Z":
        pygame.draw.polygon(screen, (255, 0, 0), transZ)