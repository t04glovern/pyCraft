from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# get player position
pos = mc.player.getTilePos()
x = pos.x + 1
y = pos.y
z = pos.z

b_height = 2
blockType = 1  # stone

# Spire sides: should be same as height
sideHeight = b_height
mc.setBlocks(x + 1,  # start pos x
             y,  # start pos y
             z + 1,  # start pos z
             x + 3,  # end pos x
             y + sideHeight - 1,  # end pos y
             z + 3,  # end pos z
             blockType)

# Spire point: should be two times the height
pointHeight = b_height * 2
mc.setBlocks(x + 2,  # start pos x
             y,  # start pos y
             z + 2,  # start pos z
             x + 2,  # end pos x
             y + pointHeight - 1,  # end pos y
             z + 2,  # end pos z
             blockType)

# Spire base: should be half the height
baseHeight = b_height / 2
mc.setBlocks(x,  # start pos x
             y,  # start pos y
             z,  # start pos z
             x + 4,  # end pos x
             y + baseHeight - 1,  # end pos y
             z + 4,  # end pos z
             blockType)

