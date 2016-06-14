from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

blockType = 103

for _y in range(y, y + 20, 1):
    mc.setBlock((x + 2), _y, z, blockType)