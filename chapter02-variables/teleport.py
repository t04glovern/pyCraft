from mcpi.minecraft import Minecraft

# connect to Minecraft
mc = Minecraft.create()

# set x, y, and z variables to represent coordinates
x = 55
y = 72
z = 0

# change the player's position
mc.player.setTilePos(x, y, z)