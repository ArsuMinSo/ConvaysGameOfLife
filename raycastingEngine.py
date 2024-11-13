from vectors import Vector2
import keyboard
import os
import time

charSet = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@█"
lstDarknessOfCharset = [0, 0.0751, 0.0829, 0.0848, 0.1227, 0.1403, 0.1559, 0.185, 0.2183, 0.2417, 0.2571, 
                        0.2852, 0.2902, 0.2919, 0.3099, 0.3192, 0.3232, 0.3294, 0.3384, 0.3609, 0.3619, 
                        0.3667, 0.3737, 0.3747, 0.3838, 0.3921, 0.396, 0.3984, 0.3993, 0.4075, 0.4091, 
                        0.4101, 0.42, 0.423, 0.4247, 0.4274, 0.4293, 0.4328, 0.4382, 0.4385, 0.442, 
                        0.4473, 0.4477, 0.4503, 0.4562, 0.458, 0.461, 0.4638, 0.4667, 0.4686, 0.4693, 
                        0.4703, 0.4833, 0.4881, 0.4944, 0.4953, 0.4992, 0.5509, 0.5567, 0.5569, 0.5591, 
                        0.5602, 0.5602, 0.565, 0.5776, 0.5777, 0.5818, 0.587, 0.5972, 0.5999, 0.6043, 
                        0.6049, 0.6093, 0.6099, 0.6465, 0.6561, 0.6595, 0.6631, 0.6714, 0.6759, 0.6809, 
                        0.6816, 0.6925, 0.7039, 0.7086, 0.7235, 0.7302, 0.7332, 0.7602, 0.7834, 0.8037, 
                        0.9084, 1.0]

lstGrid = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]

SIZE_OF_BLOCKS = 10
SIZE_OF_PLAYER = 1

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

    def __repr__(self):
        return f"Player(position={self.position})"


    def scanForMovement(self):
        PLAYER_MOVEMET = .5
        if keyboard.is_pressed("Up"): self.pos.y -= PLAYER_MOVEMET
        if keyboard.is_pressed("down"): self.pos.y += PLAYER_MOVEMET
        if keyboard.is_pressed("left"): self.pos.x -= PLAYER_MOVEMET
        if keyboard.is_pressed("right"): self.pos.x += PLAYER_MOVEMET

def drawMap(mapWorld, playerPosition):# playerpos 1.0256, 3.8430
    strMap = ""
    for y in range(len(mapWorld[0]) * SIZE_OF_BLOCKS):
        for x in range(len(mapWorld)* SIZE_OF_BLOCKS):
            if Vector2(x, y).xy == Vector2(round(playerPosition.x), round(playerPosition.y)).xy:
                strMap += "☻☻"
            elif mapWorld[x//SIZE_OF_BLOCKS][y//SIZE_OF_BLOCKS] == 0:
                strMap += "  "
            else:
                strMap += "██"
        strMap += "\n"
    return strMap




player = Player(Vector2(15, 15))

def main():
    player.scanForMovement()
    print(player.pos)
    print(drawMap(mapWorld = lstGrid, playerPosition = player.pos))
    time.sleep(1/20)
    os.system("cls")

while not keyboard.is_pressed("q"):
    main()
exit()    
