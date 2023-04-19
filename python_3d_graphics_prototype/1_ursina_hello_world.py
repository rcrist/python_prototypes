# Python 3D Graphics Prototype
# Ursina 3D graphics library
from ursina import *

window.title = "Python 3D Graphics Prototype"
app = Ursina()
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True


cube = Entity(model='cube', scale=2, collider='box', texture='brick')


def spin():
    cube.animate('rotation_y', cube.rotation_y+360, duration=2, curve=curve.in_out_expo)


cube.on_click = spin
EditorCamera()  # add camera controls for orbiting and moving the camera

app.run()
