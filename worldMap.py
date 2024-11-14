from vectors import Vector2

class Map:
    def __init__(self, grid:list, SIZE:int):
        self.grid = grid
        self.SIZE = SIZE
        
    def drawMap(self, playerPosition:Vector2) -> str: # returns map with player rawn on it
        strMap = ""
        for y in range(len(self.grid[0]) * self.SIZE):
            for x in range(len(self.grid)* self.SIZE):
                if Vector2(x, y).xy == Vector2(round(playerPosition.x), round(playerPosition.y)).xy:
                    strMap += "☻☻"
                elif self.grid[x//self.SIZE][y//self.SIZE] == 0:
                    strMap += "  "
                else:
                    strMap += "██"
            strMap += "\n"
        return strMap

    def findFirstEmptySpace(self) -> Vector2: 
        for x in range(len(self.grid[0])):
            for y in range(len(self.grid)):
                if x == y == 0:
                    return Vector2(x, y)
