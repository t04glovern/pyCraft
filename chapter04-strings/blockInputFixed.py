from mcpi.minecraft import Minecraft
mc = Minecraft.create()

try:
    blockType = int(input("Enter block ID: "))
except:
    mc.postToChat("Invalid input, please enter a number")

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlock(x + 1,  # offset position of block
            y,
            z,
            blockType)