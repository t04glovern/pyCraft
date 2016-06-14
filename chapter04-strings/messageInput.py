from mcpi.minecraft import Minecraft
mc = Minecraft.create()

message = input("What you would like to see?")
mc.postToChat(message)