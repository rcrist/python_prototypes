# Python 3D Graphics Prototype
# Ursina 3D graphics library
from ursina import *

window.title = "Python 3D Graphics Prototype"
app = Ursina()
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True

EditorCamera()  # add camera controls for orbiting and moving the camera

skybox_image = load_texture("Textures/duskcontrast.jpg")
sky = Sky(texture=skybox_image, shader=None)

app.run()
