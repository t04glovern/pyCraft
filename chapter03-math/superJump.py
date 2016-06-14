from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

y_change = False

while True:
    position = mc.player.getTilePos()
    x = position.x
    y = position.y
    z = position.z

    if mc.player.getTilePos().y > y:
        y_change = True

    if y_change:
        for _y in range(mc.player.getTilePos().y, (mc.player.getTilePos().y + 10), 1):
            mc.player.setTilePos(x, _y, z)
            time.sleep(0.015)
        y_change = False
