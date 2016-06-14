from mcpi.minecraft import Minecraft
import time

# connect to Minecraft
mc = Minecraft.create()

# set x, y, and z variables to represent coordinates
x = 54
y = 72
z = 0

# change the player's position
mc.player.setTilePos(x, y, z)

# wait 2 seconds
time.sleep(2)

# set x, y, and z variables to represent coordinates
x = 135
y = 74
z = -15

# change the player's position
mc.player.setTilePos(x, y, z)