import os, time, random, numpy

WIDTH, HEIGHT = os.get_terminal_size()
WIDTH //= 2

HEIGHT -= 1





def setRandomGrid(grid):
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            grid[x][y] = random.randint(0, 1)
    return grid

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

def getNumberOfNeignours(grid, x, y):
    intCount = 0
    for i in range(3):
        for j in range(3):
            intCount += grid[(x + i - 1) % WIDTH][(y + j - 1) % HEIGHT] if not(i == 1 and j == 1) else 0
    return intCount

def main():
    lstOldGrid = numpy.zeros([WIDTH, HEIGHT], dtype=int)

    for i in range(WIDTH//2 - 1, WIDTH//2+2):
        for j in range(HEIGHT//2, HEIGHT//2+1):
            lstOldGrid[i][j] = 1

    for _ in range(10):
        os.system('cls')
        print(printGrid(lstOldGrid))
        lstOldGrid = getNewGrid(lstOldGrid)
        time.sleep(1/10)



main()



