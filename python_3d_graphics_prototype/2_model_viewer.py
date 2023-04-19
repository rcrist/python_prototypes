# Python 3D Graphics Prototype
# Ursina 3D graphics library
from ursina import *

window.title = "Python 3D Graphics Prototype"
app = Ursina()
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True


Entity(model='Models/kenney_space-kit/Models/OBJ format/alien.obj',
       scale=2,
       double_sided=True,
       collider='box',
       x=0)

Entity(model='Models/kenney_space-kit/Models/OBJ format/astronautA.obj',
       scale=2,
       double_sided=True,
       collider='box',
       x=1)

Entity(model='Models/kenney_space-kit/Models/OBJ format/astronautB.obj',
       scale=2,
       double_sided=True,
       collider='box',
       x=2)

Entity(model='Models/kenney_space-kit/Models/OBJ format/desk_computer.obj',
       scale=2,
       double_sided=True,
       collider='box',
       x=3)

Entity(model='Models/kenney_space-kit/Models/OBJ format/rock.obj',
       scale=2,
       double_sided=True,
       collider='box',
       x=4)

Entity(model='Models/kenney_space-kit/Models/OBJ format/satelliteDisk.obj',
       scale=2,
       double_sided=True,
       collider='box',
       x=5)



EditorCamera()  # add camera controls for orbiting and moving the camera

sky=Sky()

app.run()
