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
angle = 90
#the size of each block
space = 30
cur_shape = []
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

class shape:
    startX
    startY
    shape = []
    shape_name = ""
    rot_num = 0
    def __init__(self, startX, startY, shape, shape_name):
        self.startX = startX
        self.startY = startY
        self.shape = shape
        self.shape_name = shape_name

#function for the main game loop
pressed = False
def main_game():
    global space
    global pressed
    global cur_shape
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if not pressed and cur_shape != [] and cur_shape.startX - space >= 0:
                cur_shape.shape = [(x - space, y) for x, y in cur_shape.shape]
                cur_shape.startX -= space
                pressed = True
                active_shapes.append(cur_shape)
        elif event.key == pygame.K_RIGHT:
            if not pressed and cur_shape != [] and cur_shape.startX + space < 700:
                cur_shape.shape = [(x + space, y) for x, y in cur_shape.shape]
                cur_shape.startX += space
                pressed = True
                active_shapes.append(cur_shape)
        elif event.key == pygame.K_DOWN:
            if not pressed and cur_shape != [] and cur_shape.startY + space < 550:
                cur_shape.shape = [(x, y + space) for x, y in cur_shape.shape]
                cur_shape.startY += space
                pressed = True
                active_shapes.append(cur_shape)
        elif event.key == pygame.K_UP:
            if not pressed and cur_shape != [] and cur_shape.startY - space >= 0:
                cur_shape.startY -= space
                cur_shape.shape = [(x, y - space) for x, y in cur_shape.shape]
                pressed = True
                active_shapes.append(cur_shape)
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            pressed = False
    
    for sh in active_shapes:
        draw_shape(sh)


def not_pressed():
        global cur_shape
        global active_shapes
        shape_select = random.randint(0, 6)
        cur_shape = shape(0, 0, shapes[shape_select], get_name(shape_select))
        active_shapes.append(cur_shape)
    
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
        pygame.draw.polygon(screen, (102, 255, 255), sh.shape)
    elif sh.shape_name == "T":
        pygame.draw.polygon(screen, (255, 51, 255), sh.shape)
    elif sh.shape_name == "O":
        pygame.draw.polygon(screen, (255, 255, 0), sh.shape)
    elif sh.shape_name == "J":
        pygame.draw.polygon(screen, (0, 0, 255), sh.shape)
    elif sh.shape_name == "L":
        pygame.draw.polygon(screen, (255, 153, 51), sh.shape)
    elif sh.shape_name == "S":
        pygame.draw.polygon(screen, (51, 255, 51), sh.shape)
    elif sh.shape_name == "Z":
        pygame.draw.polygon(screen, (255, 0, 0), sh.shape)


def rotate_shape(sh):
    global I, T, O, J, L, S, Z
    incrX = [sh.startX, sh.startX + space, sh.startX + (space * 2), sh.startX + (space * 3), sh.startX + (space * 4)]
    incrY = [sh.startY, sh.startY + space, sh.startY + (space * 2), sh.startY + (space * 3), sh.startY + (space * 4)]
    if sh.shape_name == "I":
        #init spot
        if sh.rot_num == 0:
            sh.shape = [(incrX[0], incrY[0]), (incrX[0], incrY[1]), (incrX[4], incrY[1]), (incrX[4], incrY[0]), (incrX[0], incrY[0])]
            sh.rot_num += 1
        elif sh.rot_num == 1:
            sh.shape = [(incrX[0], incrY[0]), (incrX[0], incrY[4]), (incrX[1], incrY[4]), (incrX[1], incrY[0]), (incrX[0], incrY[0])]
            sh.rot_num = 0
    elif sh.shape_name == "T":
        if sh.rot_num == 0:
            sh.shape = [(incrX[0], incrY[1]), (incrX[0], incrY[2]), (incrX[1], incrY[2]), (incrX[1], incrY[3]), (incrX[2], incrY[3]), (incrX[2], incrY[0]), (incrX[1], incrY[0]), (incrX[1], incrY[1]), (incrX[0], incrY[1])]
            sh.rot_num += 1
        elif sh.rot_num == 1:
            sh.shape = [(incrX[0], incrY[2]), (incrX[3], incrY[2]), (incrX[3], incrY[1]), (incrX[2], incrY[1]), (incrX[2], incrY[0]), (incrX[1], incrY[0]), (incrX[1], incrY[1]), (incrX[0], incrY[1]), (incrX[0], incrY[2])]
            sh.rot_num += 1
        elif sh.rot_num == 2:
            sh.shape = [(incrX[1], incrY[0]), (incrX[1], incrY[3]), (incrX[2], incrY[3]), (incrX[2], incrY[2]), (incrX[3], incrY[2]), (incrX[3], incrY[1]), (incrX[2], incrY[1]), (incrX[2], incrY[0]), (incrX[1], incrY[0])]            
            sh.rot_num += 1
        elif sh.rot_num == 3:
            sh.shape = [(incrX[0], incrY[0]), (incrX[0], incrY[1]), (incrX[1], incrY[1]), (incrX[1], incrY[2]), (incrX[2], incrY[2]), (incrX[2], incrY[1]), (incrX[3], incrY[1]), (incrX[3], incrY[0]), (incrX[0], incrY[0])]
            sh.rot_num = 0
    #theres only one shape that the O can be in
    elif sh.shape_name == "O":
        sh.shape = [(incrX[0], incrY[0]), (incrX[0], incrY[2]), (incrX[2], incrY[2]), (incrX[2], incrY[0]), (incrX[0], incrY[0])]
    elif sh.shape_name == "J":
        if sh.rot_num == 0:
            sh.shape = [(incrX[0], incrY[0]), (incrX[0], incrY[2]), (incrX[1], incrY[2]), (incrX[1], incrY[1]), (incrX[3], incrX[1]), (incrX[3], incrX[0]), (incrX[0], incrY[0])]
            sh.rot_num += 1
        elif sh.rot_num == 1:
            sh.shape = [(incrX[0], incrY[0]), (incrX[0], incrY[3]), (incrX[2], incrY[3]), (incrX[2], incrY[2]), (incrX[1], incrX[2]), (incrX[1], incrX[0]), (incrX[0], incrY[0])]
            sh.rot_num += 1
        elif sh.rot_num == 2:
            sh.shape = [(incrX[0], incrY[1]), (incrX[0], incrY[2]), (incrX[3], incrY[2]), (incrX[3], incrY[0]), (incrX[2], incrX[0]), (incrX[2], incrX[1]), (incrX[0], incrY[1])]
            sh.rot_num += 1
        elif sh.rot_num == 3:
            sh.shape = [(incrX[0], incrY[0]), (incrX[0], incrY[1]), (incrX[1], incrY[1]), (incrX[1], incrY[3]), (incrX[2], incrX[3]), (incrX[2], incrX[0]), (incrX[0], incrY[0])]
            sh.rot_num = 0
    elif sh.shape_name == "L":
        if sh.rot_num == 0:
            print("here")
            sh.shape = [(incrX[0], incrY[0]), (incrX[0], incrY[2]), (incrX[3], incrY[2]), (incrX[3], incrY[1]), (incrX[1], incrX[1]), (incrX[1], incrX[0]), (incrX[0], incrY[0])]
            sh.rot_num += 1
        elif sh.rot_num == 1:
            print("here 2")
            sh.shape = [(incrX[0], incrY[2]), (incrX[0], incrY[3]), (incrX[2], incrY[3]), (incrX[2], incrY[0]), (incrX[1], incrX[0]), (incrX[1], incrX[2]), (incrX[0], incrY[2])]
            sh.rot_num += 1
        elif sh.rot_num == 2:
            print("here 3")
            sh.shape = [(incrX[0], incrY[0]), (incrX[0], incrY[1]), (incrX[2], incrY[1]), (incrX[2], incrY[2]), (incrX[3], incrX[2]), (incrX[3], incrX[0]), (incrX[0], incrY[0])]
            sh.rot_num += 1
        elif sh.rot_num == 3:
            sh.shape = [(incrX[0], incrY[0]), (incrX[0], incrY[3]), (incrX[1], incrY[3]), (incrX[1], incrY[1]), (incrX[2], incrX[1]), (incrX[2], incrX[0]), (incrX[0], incrY[0])]
            sh.rot_num = 0
    elif sh.shape_name == "S":
        if sh.rot_num == 0:
            sh.shape = [(incrX[0],incrY[1]),(incrX[0],incrY[3]),(incrX[1],incrY[3]),(incrX[1], incrY[2]),(incrX[2], incrY[2]),(incrX[2], incrY[0]), (incrX[1], incrY[0]), (incrX[1], incrY[1]), (incrX[0], incrY[1])]
            sh.rot_num += 1
        elif sh.rot_num == 1:
            sh.shape = [(incrX[0],incrY[1]),(incrX[0],incrY[3]),(incrX[1],incrY[3]),(incrX[1], incrY[2]),(incrX[2], incrY[2]),(incrX[2], incrY[0]), (incrX[1], incrY[0]), (incrX[1], incrY[1]), (incrX[0], incrY[1])]
            sh.rot_num = 0
    elif sh.shape_name == "Z":
        if sh.rot_num == 0:
            sh.shape = [(incrX[0],incrY[0]),(incrX[0],incrY[2]),(incrX[1],incrY[2]),(incrX[1], incrY[3]),(incrX[2], incrY[3]),(incrX[2], incrY[1]), (incrX[1], incrY[1]), (incrX[1], incrY[0]), (incrX[0], incrY[0])]
            sh.rot_num += 1
        elif sh.rot_num == 1:
            sh.shape = [(incrX[0],incrY[1]),(incrX[0],incrY[2]),(incrX[2],incrY[2]),(incrX[2], incrY[1]),(incrX[3], incrY[1]),(incrX[3], incrY[0]), (incrX[1], incrY[0]), (incrX[1], incrY[1]), (incrX[0], incrY[1])]
            sh.rot_num = 0


#
# LEAVE THIS AT THE BOTTOM!!!!
#
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if rot:
                    if cur_shape != []:
                        active_shapes.remove(cur_shape)
                        rotate_shape(cur_shape)
                        rot = False
                        active_shapes.append(cur_shape)
            elif event.key == pygame.K_d:
                if not pressed:
                    not_pressed()
                    pressed = True
    else:
        rot = True
    screen.fill((255, 255, 255))  # Fill the screen with white
    # Game logic and updates go here
    main_game()
    # Rendering
    
    
    pygame.display.flip()    # Update the display


pygame.quit()