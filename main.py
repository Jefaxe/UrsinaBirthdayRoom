'''
Disclaimer: This solution is not scalable for creating a big world.
Creating a game like Minecraft requires specialized knowledge and is not as easy
to make as it looks.
You'll have to do some sort of chunking of the world and generate a combined mesh
instead of separate blocks if you want it to run fast. You can use the Mesh class for this.
You can then use blocks with colliders like in this example in a small area
around the player so you can interact with the world.
'''
import logging

MAPSIZE = 10
DEPTH = 2

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.title = "Happy Birthday!"
window.fps_counter.enabled = False
logging.basicConfig(level=logging.DEBUG)
# Define a Voxel class.
# By setting the parent to scene and the model to 'cube' it becomes a 3d button.

table = Entity(position=(0, 2, 0), model='cube', scale=(2, 2, 2), color=color.brown, collider="cube")
plate = Entity(position=(0, 3.01, 0), model='circle', color=color.white, scale=(1.5, 1.5),
               rotation=90)
glass = Entity(position=(0.8, 3, 0.8), model="cube", color=color.orange, scale=(0.25, 0.8, 0.25))
photo = Entity(position=(0.8, 3.1, 0), model="plane", texture="birthday.png")


class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            texture='white_cube',
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )

    def input(self, key):
        if self.hovered:
            if key == "r":
                logging.info(f"The block is at position {self.position}")
            if key == "m":
                logging.info(f"You are at {player.position}")
            if key == 'left mouse down' or key == "'":
                voxel = Voxel(position=self.position + mouse.normal)
            if key == 'right mouse down' or key == ";":
                destroy(self)


player = FirstPersonController(position=(-1.96327, 1.5, 0.223245), rotation_x=15)

for y in range(DEPTH):
    for z in range(-MAPSIZE, MAPSIZE):
        for x in range(-MAPSIZE, MAPSIZE):
            voxel = Voxel(position=(x, y, z))

app.run()
