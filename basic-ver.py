import random

############################################################
# grid #####################################################
# 00 10 20 30
# 01 11 21 31
# 02 12 22 32
# 03 13 23 33

grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

############################################################
# Functions ################################################
        
def new():
    spawn = True
    while spawn == True:
        x = random.randint(0,3)
        y = random.randint(0,3)
        val = random.randint(1,10)
        if val == 10:
            val = 4
        else:
            val = 2
        loc = grid[x][y]
        if loc != 0:
            spawn = True
        else:
            grid[x][y] = val
            spawn = False
    score = grid[0][0] + grid[0][1] + grid[0][2] + grid[0][3] + grid[1][0] + grid[1][1] + grid[1][2] + grid[1][3] + grid[2][0] + grid[2][1] + grid[2][2] + grid[2][3] + grid[3][0] + grid[3][1] + grid[3][2] + grid[3][3]
    print("score: " + str(score))
    
def onedig(num):
    return("|  " + num + " |")#2 left 1 right

def twodig(num):
    return("| " + num + " |")#1 left 1 right

def threedig(num):
    return("| " + num + "|")#1 left 0 right

def fourdig(num):
    return("|" + num + "|")#0 left 0 right
    
def showGrid():
    for y in range(0,4):
        a = [str(grid[0][y]),str(grid[1][y]),str(grid[2][y]),str(grid[3][y])]
        tp = []
        for i in a:
            if len(i) == 1:
                tp.append(onedig(i))
            elif len(i) == 2:
                tp.append(twodig(i))
            elif len(i) == 3:
                tp.append(threedig(i))
            elif len(i) == 4:
                tp.append(fourdig(i))
        print(tp[0] + tp[1] + tp[2] + tp[3])
        print("------------------------")
    print("")
    
def up():
    for i in range(0,5):
        for x in range(0,4):
            y = 3
            while y > 0:
                if grid[x][y-1] == grid[x][y]:
                    grid[x][y-1] = grid[x][y-1] * 2
                    grid[x][y] = 0
                elif grid[x][y-1] == 0:
                    grid[x][y-1] = grid[x][y]
                    grid[x][y] = 0
                y = y - 1
    
                
def down():
    for i in range(0,5):
        for x in range(0,4):
            y = 2
            while y > -1:
                if grid[x][y+1] == grid[x][y]:
                    grid[x][y+1] = grid[x][y+1] * 2
                    grid[x][y] = 0
                elif grid[x][y+1] == 0:
                    grid[x][y+1] = grid[x][y]
                    grid[x][y] = 0
                y = y - 1


                
def left():
    for i in range(0,5):
        for y in range(0,4):
            x = 3
            while x > 0:
                if grid[x-1][y] == grid[x][y]:
                    grid[x-1][y] = grid[x-1][y] * 2
                    grid[x][y] = 0
                elif grid[x-1][y] == 0:
                    grid[x-1][y] = grid[x][y]
                    grid[x][y] = 0
                x = x - 1
                
def right():
    for i in range(0,5):
        for y in range(0,4):
            x = 2
            while x > -1:
                if grid[x+1][y] == grid[x][y]:
                    grid[x+1][y] = grid[x+1][y] * 2
                    grid[x][y] = 0
                elif grid[x+1][y] == 0:
                    grid[x+1][y] = grid[x][y]
                    grid[x][y] = 0
                x = x - 1

def play():
    while True:
        showGrid()
        inp = input("move: ")
        if inp == "w":
            up()
            new()
        elif inp == "s":
            down()
            new()
        elif inp == "a":
            left()
            new()
        elif inp == "d":
            right()
            new()
        else:
            print("invald move, use 'wasd' to control movement.")
        
####################################################
###### playing the game ############################

print("Warning, the game ends when it has no free tiles to spawn a new block, not when no moves can be made!")   
new()
new()

play()
