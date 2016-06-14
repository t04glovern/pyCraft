# Import the Minecraft python library
from mcpi.minecraft import Minecraft

# create the minecraft connection instance
mc = Minecraft.create()

# this opens an connection when run and will provide the following
# feedback in the server status window
"""
[14:06:27 INFO]: [RaspberryJuice] Opened connection to/127.0.0.1:57543.
[14:06:27 INFO]: [RaspberryJuice] Starting output thread!
[14:06:27 INFO]: [RaspberryJuice] Closed connection to/127.0.0.1:57543.
"""

# sets players x, y and z values in game (teleport)
mc.player.setTilePos(0, 120, 0)