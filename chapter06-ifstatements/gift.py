from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = mc.player.getTilePos().x
y = mc.player.getTilePos().y
z = mc.player.getTilePos().z
mc.setBlock(x, y - 1, z, 20)

while 1:
    gift = mc.getBlock(x, y - 1, z)

    if gift == 57:
        mc.postToChat("Thanks for the Diamond!")
    elif gift == 6:
        mc.postToChat("I don't want your damn sapling!")
    else:
        mc.postToChat("Bring a gift to " + str(x) + ", " + str(y) + ", " + str(z))