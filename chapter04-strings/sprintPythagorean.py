from mcpi.minecraft import Minecraft
import time
import math
mc = Minecraft.create()

try:
    timer = int(input("How long shall we sprint for?: "))
except:
    mc.postToChat("Please enter a valid int for the timer")

mc.postToChat("Ready")
time.sleep(1)
mc.postToChat("Set")
time.sleep(1)
mc.postToChat("Go!")

pos_start = mc.player.getTilePos()
x_start = pos_start.x
y_start = pos_start.y
z_start = pos_start.z

for t in range(0, timer, 1):
    time.sleep(1)
    mc.postToChat(str(timer - t) + " seconds left;   " +
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

# Pythagorean calculation
distance = math.sqrt(math.pow((x_end - x_start), 2) +
                     math.pow((y_end - y_start), 2) +
                     math.pow((z_end - z_start), 2))

mc.postToChat("You travelled a calculated distance of: " + str(distance))