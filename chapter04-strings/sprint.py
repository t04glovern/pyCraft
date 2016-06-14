from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

pos_start = mc.player.getTilePos()
x_start = pos_start.x
y_start = pos_start.y
z_start = pos_start.z

mc.postToChat("Ready")
time.sleep(1)
mc.postToChat("Set")
time.sleep(1)
mc.postToChat("Go!")

for t in range(0, 15, 1):
    time.sleep(1)
    mc.postToChat(str(15 - t) + " seconds left;   " +
                  " X: " + str(mc.player.getTilePos().x) +
                  " Y: " + str(mc.player.getTilePos().y) +
                  " Z: " + str(mc.player.getTilePos().z))

pos_end = mc.player.getTilePos()
x_end = pos_end.x
y_end = pos_end.y
z_end = pos_end.z

x_travel = x_end - x_start
y_travel = y_end - y_start
z_travel = z_end - z_start

mc.postToChat("You travelled " + str(x_travel) + " from X")
mc.postToChat("You travelled " + str(y_travel) + " from Y")
mc.postToChat("You travelled " + str(z_travel) + " from Z")