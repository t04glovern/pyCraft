from mcpi.minecraft import Minecraft
mc = Minecraft.create()

answer = input("Create a crater? Y/N")

if answer == "Y":
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z

    mc.setBlocks(x + 1, y + 1, z + 1, x - 1, y - 1, z - 1, 0)
    mc.postToChat("Boom!")