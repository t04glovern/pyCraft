from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# get player position
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

b_width = 10
b_height = 5
b_length = 6

block_type = 4  # cobblestone
block_fill = 0  # air

# create base cube
mc.setBlocks(x,  # start pos x
             y,  # start pos z
             z,  # start pos z
             x + b_width,  # end pos x
             y + b_length,  # end pos y
             z + b_length,  # end pos z
             block_type)

# punch out center of cube
mc.setBlocks(x + 1,  # start pos x
             y + 1,  # start pos z
             z + 1,  # start pos z
             x + b_width - 1,  # end pos x
             y + b_length - 1,  # end pos y
             z + b_length - 1,  # end pos z
             block_fill)