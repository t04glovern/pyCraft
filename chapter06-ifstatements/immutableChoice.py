from mcpi.minecraft import Minecraft
mc = Minecraft.create()

ans = input("Do you want blocks to be immutable? Y/N ")

if ans == "Y":
    mc.setting("world_immutable", True)
    mc.postToChat("World is immutable")
elif ans == "N":
    mc.setting("world_immutable", False)
    mc.postToChat("World is mutable")
