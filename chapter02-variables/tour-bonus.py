from mcpi.minecraft import Minecraft
import time

# connect to Minecraft
mc = Minecraft.create()

# y, and z variables to represent coordinates
x = mc.player.getPos().x
y = mc.player.getPos().y
z = mc.player.getPos().z

for x in range(int(x), int(x + 10), 1):
    # change the player's position
    mc.player.setTilePos(x, y, z)

    # wait 2 seconds
    time.sleep(0.1)
