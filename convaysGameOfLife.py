import os, time, random, numpy, keyboard
from matMul import rotate_matrix
#from numba import jit, cuda


WIDTH, HEIGHT = os.get_terminal_size()
WIDTH //= 2

HEIGHT -= 2

shapes = {
    "blinker":[
        [1, 1, 1]
    ],
    "toad":[
        [0, 1, 1, 1],
        [1, 1, 1, 0]
    ],
    "beacon":[
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ],
    "glider":[
        [0, 0, 1],
        [1, 0, 1],
        [0, 1, 1]
    ],
    "idlerLarge":[
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        ]
}

def rotate(lst):
    return rotate_matrix(lst)

def printOnGrid(grid, x, y, obj):
    for _x, i in zip(range(len(obj)), obj):
        for _y, j in zip(range(len(obj[_x])), obj[_x]):
            grid[x + _x][y + _y] = j

def printGrid(grid): 
    strWhite = "██"
    strBlank = "  "
    strScreen = ""    
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            if grid[x][y] == 1:
                strScreen += strWhite
            else:
                strScreen += strBlank
        strScreen += "\n"
    return strScreen

def getNewGrid(grid):
    lstNewGrid = numpy.zeros([WIDTH, HEIGHT], dtype = int)
    for x in range(len(lstNewGrid)):
        for y in range(len(lstNewGrid[x])):
            intNumberOfNeighbours = getNumberOfNeignours(grid, x, y)
            
            # underpopulation
            if intNumberOfNeighbours < 2:
                lstNewGrid[x][y] = 0
            
            # live
            elif grid[x][y] == 1 and 2 <= intNumberOfNeighbours <= 3:
                lstNewGrid[x][y] = 1
            
            # overpopulation
            elif grid[x][y] == 1 and 4 <= intNumberOfNeighbours:
                lstNewGrid[x][y] = 0
            
            # reproduction
            elif grid[x][y] == 0 and intNumberOfNeighbours == 3:
                lstNewGrid[x][y] = 1

    return lstNewGrid

#@jit(parallel = True)
def getNumberOfNeignours(grid, x, y):
    intCount = 0
    for i in range(3):
        for j in range(3):
            intCount += grid[(x + i - 1) % WIDTH][(y + j - 1) % HEIGHT] if not(i == 1 and j == 1) else 0
    return intCount


def main():

    shapes = {
    "blinker":[
        [1, 1, 1]
    ],
    "toad":[
        [0, 1, 1, 1],
        [1, 1, 1, 0]
    ],
    "beacon":[
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ],
    "glider":[
        [0, 0, 1],
        [1, 0, 1],
        [0, 1, 1]
    ],
    "idlerLarge":[
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        ]
    }


    lstOldGrid = numpy.zeros([WIDTH, HEIGHT], dtype=int)

    """
    for i in range(WIDTH//2 - 1, WIDTH//2+2):
        for j in range(HEIGHT//2, HEIGHT//2+1):
            lstOldGrid[i][j] = 1
    """

    shape = shapes["idlerLarge"]

    #printOnGrid(lstOldGrid, WIDTH//2 - len(shape), HEIGHT//2 - len(shape[0])//2, shape)
    #printOnGrid(lstOldGrid, WIDTH//2 + len(shape), HEIGHT//2 - len(shape[0])//2, rotate_matrix(shape))
 
    for i in range(WIDTH):
        for j in range(HEIGHT):
            lstOldGrid[i][j] = random.randint(0, 1)

    speed = 5
    
    while True:
        start = time.time()
        if keyboard.is_pressed("q"):
            break
        elif keyboard.is_pressed("UP"):
            speed *= 1.1
        elif keyboard.is_pressed("DOWN"):
            speed *= 0.9
            
        
        strSpeed = str(speed)
        
        lstOldGrid = getNewGrid(lstOldGrid)
        #time.sleep(1/speed)
        os.system('cls')
        print(printGrid(lstOldGrid) + strSpeed + "\t\t" + str(1 / (time.time() - start)))

main()