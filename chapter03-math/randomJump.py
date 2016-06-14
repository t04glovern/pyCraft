from mcpi.minecraft import Minecraft
import random
import time

mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

for a in range(1, 10, 1):
    a += a
    _x = x + random.randint(-10, 10)
    _y = y + random.randint(-10, 10)
    _z = z + random.randint(-10, 10)

    mc.player.setPos(_x, _y, _z)
    mc.postToChat(" x: " + str(int(_x)) +
                  " y: " + str(int(_y)) +
                  " z: " + str(int(_z)))

    time.sleep(1)

# set back to starting point
mc.player.setPos(x, y, z)