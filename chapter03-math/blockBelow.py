from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

# lava block...
blockType = 10

mc.setBlock(x, (y - 1), z, blockType)

