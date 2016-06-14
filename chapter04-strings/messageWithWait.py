from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

message1 = input("What you would like to see?")
time.sleep(1)
message2 = input("What else?")
mc.postToChat(message1 + " and " + message2)