import keyboard
from vectors import Vector2
from worldMap import Map

class Player:
    def __init__(self, pos: Vector2):
        # Assign position directly if `pos` is already a `Vector2` instance
        if isinstance(pos, Vector2):
            self.pos = pos
        else:
            raise TypeError("pos must be an instance of Vector2")

        # Optionally, assign `x` and `y` separately for direct access
        self.x = pos.x
        self.y = pos.y

    def __repr__(self) -> str:
        return f"Player(position={self.position})"


    def tryMovement(self, worldMap:Map, incrementOfPos:float):
        if worldMap.grid[int(self.y + incrementOfPos)//worldMap.SIZE] == 1 or \
           worldMap.grid[int(self.x + incrementOfPos)//worldMap.SIZE] == 1 : 
            return -1 * incrementOfPos

    def scanForMovement(self, worldMap:Map) -> None:
        PLAYER_MOVEMET = .5
        if keyboard.is_pressed("Up"): self.pos.y += self.tryMovement(worldMap, -PLAYER_MOVEMET)
        if keyboard.is_pressed("down"): self.pos.y += self.tryMovement(worldMap, PLAYER_MOVEMET)
        if keyboard.is_pressed("right"): self.pos.x += self.tryMovement(worldMap, -PLAYER_MOVEMET)
        if keyboard.is_pressed("left"): self.pos.x += self.tryMovement(worldMap, PLAYER_MOVEMET)