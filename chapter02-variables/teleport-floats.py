from mcpi.minecraft import Minecraft

# connect to Minecraft
mc = Minecraft.create()

# set x, y, and z variables to represent coordinates
x = 53.594
y = 72
z = -0.872

# change the player's position
mc.player.setPos(x, y, z)