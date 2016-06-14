from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x_cord = int(input("Enter X: "))
y_cord = int(input("Enter Y: "))
z_cord = int(input("Enter Z: "))
blockType = int(input("Enter Block ID: "))

mc.player.setTilePos(x_cord + 1, y_cord, z_cord)
mc.setBlock(x_cord, y_cord, z_cord, blockType)