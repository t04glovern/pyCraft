from mcpi.minecraft import Minecraft
mc = Minecraft.create()

blockType = int(input("Enter block ID: "))

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlock(x + 1,  # offset position of block
            y,
            z,
            blockType)