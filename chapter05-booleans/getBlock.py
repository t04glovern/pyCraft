from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while 1:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z

    blockType = mc.getBlock(x, y - 1, z)
    mc.postToChat(blockType)