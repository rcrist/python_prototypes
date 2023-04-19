# Python 3D Graphics Prototype
# Ursina 3D graphics library
from ursina import *

window.title = "Python 3D Graphics Prototype"
app = Ursina()
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True


Entity(model='Models/kenney_blocky-characters/Models/advancedCharacter.fbx',
       scale=.1,
       double_sided=True,
       collider='box',
       x=0,
       texture='Models/kenney_blocky-characters/Skins/Advanced/skin_adventurer.png')

Entity(model='Models/kenney_blocky-characters/Models/advancedCharacter.fbx',
       scale=.1,
       double_sided=True,
       collider='box',
       x=1,
       texture='Models/kenney_blocky-characters/Skins/Advanced/skin_man.png')

Entity(model='Models/kenney_blocky-characters/Models/advancedCharacter.fbx',
       scale=.1,
       double_sided=True,
       collider='box',
       x=2,
       texture='Models/kenney_blocky-characters/Skins/Advanced/skin_manAlternative.png')

Entity(model='Models/kenney_blocky-characters/Models/advancedCharacter.fbx',
       scale=.1,
       double_sided=True,
       collider='box',
       x=3,
       texture='Models/kenney_blocky-characters/Skins/Advanced/skin_orc.png')

Entity(model='Models/kenney_blocky-characters/Models/advancedCharacter.fbx',
       scale=.1,
       double_sided=True,
       collider='box',
       x=4,
       texture='Models/kenney_blocky-characters/Skins/Advanced/skin_robot.png')

Entity(model='Models/kenney_blocky-characters/Models/advancedCharacter.fbx',
       scale=.1,
       double_sided=True,
       collider='box',
       x=6,
       texture='Models/kenney_blocky-characters/Skins/Advanced/skin_soldier.png')

Entity(model='Models/kenney_blocky-characters/Models/advancedCharacter.fbx',
       scale=.1,
       double_sided=True,
       collider='box',
       x=7,
       texture='Models/kenney_blocky-characters/Skins/Advanced/skin_woman.png')

Entity(model='Models/kenney_blocky-characters/Models/advancedCharacter.fbx',
       scale=.1,
       double_sided=True,
       collider='box',
       x=8,
       texture='Models/kenney_blocky-characters/Skins/Advanced/skin_womanAlternative.png')


EditorCamera()  # add camera controls for orbiting and moving the camera

sky=Sky()

app.run()
