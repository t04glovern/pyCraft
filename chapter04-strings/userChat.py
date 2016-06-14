from mcpi.minecraft import Minecraft
mc = Minecraft.create()

username = input("Enter your username: ")
message = input("Enter your message: ")
mc.postToChat(username + ": " + message)