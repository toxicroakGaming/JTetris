#init
import pygame
import math
import random
import copy
import threading
import time
from Shape import shape

pygame.init()
#CONTROLS
#arrows to move
#A and F to rotate
#D to create a new shape


#initial values of shapes
I = [1, 2, 3, 4]
T = [1, 5, 6, 9]
J = [5, 9, 10, 11]
L = [5, 6, 7, 9]
S = [1, 5, 6, 10]
Z = [6, 9, 10, 13]
O = [5, 9, 6, 10]


#there will be a "grid" of squares. 1 will represent occupied and 0 will represent free
columns = 10
rows = 20
grid = [[0 for j in range(columns)]
for i in range(rows)]

shapes = [I, T, O, J, L, S, Z]
names = {"I": I, "T": T, "O": O, "J": J, "L": L, "S": S, "Z": Z}


# Set up the window dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
#was our previous rotation a left or a right?
#important for resetting a value
left = False
#we cant assume which way the user will flip first
firstPress = False
# Set a title for the window
pygame.display.set_caption("Tetris")
startX = 0
startY = 0
#the size of each block
space = 30

active_shapes = []

cur_shape = shape(0, 0, "")
nextShape = shape(0, 0, "")

def get_rect(a):
    cur_shape.sh = []
    for s in a:
        x = s / 4
        y = s % 4
        if s == 4:
            x = 0
            y = 4
        #left, top, width, height
        x = int(x)
        y = int(y)
        cur_shape.sh.append(pygame.Rect(cur_shape.startX + ((x-1) * space), cur_shape.startY + ((y-1) * space), space, space))


def check_collision():
    for s in active_shapes:
        for a in s.sh:
            for o in cur_shape.sh:
                if a.colliderect(o):
                    return True
    return False

# dir == true means move y units
# dir == false means move x units
def trans_rects(dir, num):
    for s in cur_shape.sh:
        if dir:
            s.move_ip(0, num)
        else:
            s.move_ip(num, 0)

#function for the main game loop
pressed = False
first = True
def main_game():
    global space
    global pressed
    global cur_shape
    global first
    if first:
        first = False
        #next_shape()
        #move_cur_shape()
    old_shape = copy.deepcopy(cur_shape)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if not pressed and cur_shape.sh != [] and cur_shape.startX - space >= 0:
                    active_shapes.remove(cur_shape)
                    cur_shape.startX -= space
                    trans_rects(False, space * -1)
                    if check_collision():
                        cur_shape.startX += space
                        trans_rects(False, space)
                    active_shapes.append(cur_shape)
                    pressed = True
        elif event.key == pygame.K_RIGHT:
            if not pressed and cur_shape.sh != [] and cur_shape.startX + space < 700:
                active_shapes.remove(cur_shape)
                cur_shape.startX += space
                trans_rects(False, space)
                if check_collision():
                    cur_shape.startX -= space
                    trans_rects(False, space * -1)
                active_shapes.append(cur_shape)
                pressed = True
        elif event.key == pygame.K_DOWN:
            if not pressed and cur_shape.sh != [] and cur_shape.startY + space < 550:
                active_shapes.remove(cur_shape)
                cur_shape.startY += space
                trans_rects(True, space)
                if check_collision():
                    cur_shape.startY -= space
                    trans_rects(True, -space)
                active_shapes.append(cur_shape)
                pressed = True
        #t1 = threading.Thread(move_down, none)
        #leaving this here as playground code
        #if you want to free move the blocks around the screen, this is for
        #moving the blocks up
        #elif event.key == pygame.K_UP:
            #if not pressed and cur_shape.sh != [] and cur_shape.startY - space >= 0:
                #active_shapes.remove(cur_shape)
                #cur_shape.startY -= space
                #trans_rects(True, -space)
                #if check_collision():
                    #cur_shape.startY += space
                    #trans_rects(True, space)
                #active_shapes.append(cur_shape)
                #pressed = True
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            pressed = False
    
    for sh in active_shapes:
        draw_shape(sh)


def move_down():
    ch = True
    while ch and cur_shape.startY > 700:
        time.sleep(1)
        active_shapes.remove(cur_shape)
        cur_shape.startY -= space
        trans_rects(True, space)
        if check_collision():
            cur_shape.startY -= space
            trans_rects(True, -space)
            time.sleep(5)
            if check_collision():
                #freezes the current shape in place
                move_cur_shape()
        active_shapes.append(cur_shape)
    if cur_shape.startY >= 700:
        time.sleep(5)
        move_cur_shape()
    

def next_shape():
        global nextShape
        global active_shapes
        shape_select = random.randint(0, 6)
        #put it in the "ready" spot
        nextShape = shape(500, 150, get_name(shape_select))
        #active_shapes.append(cur_shape)
        get_rect(shapes[shape_select])

def move_cur_shape():
        global nextShape
        global active_shapes
        global cur_shape
        #put it in the "ready" spot
        cur_shape = copy.deepcopy(nextShape)
        next_shape()
        print(cur_shape.sh)
        active_shapes.append(cur_shape)

def get_next_shape():
    global active_shapes
    global cur_shape
    shape_select = random.randint(0, 6)
    #put it in the "ready" spot
    cur_shape = shape(500, 150, get_name(shape_select))
    active_shapes.append(cur_shape)
    get_rect(shapes[shape_select])


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
        for s in sh.sh:
            pygame.draw.rect(screen, (102, 255, 255), s)
    elif sh.shape_name == "T":
        for s in sh.sh:
            pygame.draw.rect(screen, (255, 51, 255), s)
    elif sh.shape_name == "O":
        for s in sh.sh:    
            pygame.draw.rect(screen, (255, 255, 0), s)
    elif sh.shape_name == "J":
        for s in sh.sh:
            pygame.draw.rect(screen, (0, 0, 255), s)
    elif sh.shape_name == "L":
        for s in sh.sh:
            pygame.draw.rect(screen, (255, 153, 51), s)
    elif sh.shape_name == "S":
        for s in sh.sh:    
            pygame.draw.rect(screen, (51, 255, 51), s)
    elif sh.shape_name == "Z":
        for s in sh.sh:
            pygame.draw.rect(screen, (255, 0, 0), s)


def rotate_shape_left(sh):
    global I, T, O, J, L, S, Z, left, firstPress
    #fix some rotation issues
    if not left and not firstPress:
        left = True
        if sh.shape_name == "I" or sh.shape_name == "S" or sh.shape_name == "Z":
            #do nothing
            pass
        else:
            if sh.rot_num == 2:
                sh.rot_num = 0
            elif sh.rot_num == 3:
                sh.rot_num = 1
            else:
                sh.rot_num += 2
    if sh.shape_name == "I":
        #init spot
        if sh.rot_num == 0:
            get_rect([3, 7, 11, 15])
            sh.rot_num += 1
        elif sh.rot_num == 1:
            get_rect(I)
            sh.rot_num = 0
    elif sh.shape_name == "T":
        if sh.rot_num == 0:
            get_rect([5, 6, 7, 10])
        elif sh.rot_num == 1:
            get_rect([6, 10, 14, 9])
        elif sh.rot_num == 2:
            get_rect([9, 10, 11, 6])
        elif sh.rot_num == 3:
            get_rect(T)
        if sh.rot_num != 3:
            sh.rot_num += 1
        else:
            sh.rot_num = 0
    #theres only one shape that the O can be in
    elif sh.shape_name == "O":
        get_rect(O)
    elif sh.shape_name == "J":
        if sh.rot_num == 0:
            get_rect([1, 2, 5, 9])
            sh.rot_num += 1
        elif sh.rot_num == 1:
            get_rect([5, 6, 7, 11])
            sh.rot_num += 1
        elif sh.rot_num == 2:
            get_rect([6, 10, 14, 13])
            sh.rot_num += 1
        elif sh.rot_num == 3:
            get_rect(J)
            sh.rot_num = 0
    elif sh.shape_name == "L":
        if sh.rot_num == 0:
            get_rect([6, 7, 11, 15])
            sh.rot_num += 1
        elif sh.rot_num == 1:
            get_rect([7, 11, 10, 9])
            sh.rot_num += 1
        elif sh.rot_num == 2:
            get_rect([5, 9, 13, 14])
            sh.rot_num += 1
        elif sh.rot_num == 3:
            get_rect(L)
            sh.rot_num = 0
    elif sh.shape_name == "S":
        if sh.rot_num == 0:
            get_rect([6, 7, 9, 10])
        elif sh.rot_num == 1:
            get_rect(S)
            sh.rot_num = 0
    elif sh.shape_name == "Z":
        if sh.rot_num == 0:
            get_rect([5, 6, 10, 11])
            sh.rot_num = 1
        elif sh.rot_num == 1:
            get_rect(Z)
            sh.rot_num = 0
    #if check_collision():
        #sh = copy.deepcopy(old_sh)


# maybe I will find a better way to implement rotating, but for now, this is 
# basically a copied version of rotate_shape_left
# with the variables going the opposite direction
def rotate_shape_right(sh):
    global I, T, O, J, L, S, Z, left, firstPress
    old_sh = copy.deepcopy(sh)
    #fix some rotation issues
    if left and not firstPress:
        left = True
        if sh.shape_name == "I" or sh.shape_name == "S" or sh.shape_name == "Z":
            #do nothing
            pass
        else:
            if sh.rot_num == 1:
                sh.rot_num = 3
            elif sh.rot_num == 0:
                sh.rot_num = 2
            else:
                sh.rot_num -= 2
    if sh.shape_name == "I":
        #init spot
        if sh.rot_num == 0:
            get_rect([3, 7, 11, 15])
            sh.rot_num += 1
        elif sh.rot_num == 1:
            get_rect(I)
            sh.rot_num = 0
    elif sh.shape_name == "T":
        if sh.rot_num == 0:
            get_rect([5, 6, 7, 10])
        elif sh.rot_num == 1:
            get_rect([6, 10, 14, 9])
        elif sh.rot_num == 2:
            get_rect([9, 10, 11, 6])
        elif sh.rot_num == 3:
            get_rect(T)
        if sh.rot_num != 0:
            sh.rot_num -= 1
        else:
            sh.rot_num = 3
    #theres only one shape that the O can be in
    elif sh.shape_name == "O":
        get_rect(O)
    elif sh.shape_name == "J":
        if sh.rot_num == 0:
            get_rect([1, 2, 5, 9])
            sh.rot_num = 3
        elif sh.rot_num == 1:
            get_rect([5, 6, 7, 11])
            sh.rot_num -= 1
        elif sh.rot_num == 2:
            get_rect([6, 10, 14, 13])
            sh.rot_num -= 1
        elif sh.rot_num == 3:
            get_rect(J)
            sh.rot_num -= 1
    elif sh.shape_name == "L":
        if sh.rot_num == 0:
            get_rect([6, 7, 11, 15])
            sh.rot_num = 3
        elif sh.rot_num == 1:
            get_rect([7, 11, 10, 9])
            sh.rot_num -= 1
        elif sh.rot_num == 2:
            get_rect([5, 9, 13, 14])
            sh.rot_num -= 1
        elif sh.rot_num == 3:
            get_rect(L)
            sh.rot_num -= 1
    elif sh.shape_name == "S":
        if sh.rot_num == 0:
            get_rect([6, 7, 9, 10])
            sh.rot_num = 1
        elif sh.rot_num == 1:
            get_rect(S)
            sh.rot_num = 0
    elif sh.shape_name == "Z":
        if sh.rot_num == 0:
            get_rect([5, 6, 10, 11])
            sh.rot_num = 1
        elif sh.rot_num == 1:
            get_rect(Z)
            sh.rot_num = 0
    if check_collision():
        sh = copy.deepcopy(old_sh)



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
                    if cur_shape.sh != []:
                        active_shapes.remove(cur_shape)
                        rotate_shape_right(cur_shape)
                        rot = False
                        #if not check_collision():
                            #get_rect(names.get(cur_shape.shape_name))
                        active_shapes.append(cur_shape)
                        firstPress = False
            if event.key == pygame.K_f:
                if rot:
                    if cur_shape.sh != []:
                        active_shapes.remove(cur_shape)
                        rotate_shape_left(cur_shape)
                        rot = False
                        #if check_collision():
                            #get_rect(names.get(cur_shape.shape_name))
                        active_shapes.append(cur_shape)
                        firstPress = False
            elif event.key == pygame.K_d:
                if not pressed:
                    firstPress = True
                    get_next_shape()
                    pressed = True
    else:
        rot = True
    screen.fill((255, 255, 255))  # Fill the screen with white
    # Game logic and updates go here
    main_game()
    # Rendering
    
    pygame.display.flip()    # Update the display


pygame.quit()