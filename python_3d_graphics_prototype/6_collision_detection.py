# Python 3D Graphics Prototype
# Ursina 3D graphics library
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

window.title = "Python 3D Graphics Prototype"
app = Ursina(vsync=False)
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True

Entity.default_shader = lit_with_shadows_shader

ec = EditorCamera()
ec.enabled = False
m = 0
n_frame = 400

ground = Entity(model='Models/kenney_space-kit/Models/OBJ format/terrain.obj', scale=64, collider='box')
player = FirstPersonController(model='Models/kenney_space-kit/Models/OBJ format/astronautA.obj',
                               origin_y=.5, speed=8, collider="box", enabled=True)

# Add walls to confine the player to the plane
w1 = Entity(model='quad', scale=(64,10), collider='box', color=color.gray, position=(0,5,32))
w2 = Entity(model='quad', scale=(64,10), collider='box', color=color.gray, position=(0,5,-32))
w2.rotation_x = 180
w3 = Entity(model='quad', scale=(64,10), collider='box', color=color.gray, position=(32,5,0))
w3.rotation_y = 90
w4 = Entity(model='quad', scale=(64,10), collider='box', color=color.gray, position=(-32,5,0))
w4.rotation_y = 270

# Add platforms and obstacles
Entity(model='Models/kenney_space-kit/Models/OBJ format/barrels.obj',position=(10,0,10),scale=2,collider='box')
Entity(model='Models/kenney_space-kit/Models/OBJ format/platform_low.obj',position=(-10,0,10),scale=2,collider='box')
Entity(model='Models/kenney_space-kit/Models/OBJ format/platform_high.obj',position=(-10,0,2),scale=2,collider='box')
Entity(model='Models/kenney_space-kit/Models/OBJ format/satelliteDish_detailed.obj',position=(22,0,5),scale=2,collider='box')
Entity(model='Models/kenney_space-kit/Models/OBJ format/stairs_short.obj',position=(-10,0,11.5),scale=2,collider='box')
Entity(model='Models/kenney_space-kit/Models/OBJ format/pipe_rampLarge.obj',position=(-10,0,6),scale=2,collider='box')
Entity(model='Models/kenney_space-kit/Models/OBJ format/platform_high.obj',position=(-10,0,-2),scale=2,collider='box')
p1 = Entity(model='Models/kenney_space-kit/Models/OBJ format/platform_long.obj',position=(-10,2,0),scale=2,collider='box')
p1.rotation_y = 90

# Add bonus items
b1 = Entity(model='quad', texture="kenney_assets/Bonus/yellowCrystal.png", scale=(0.3,0.3), position=Vec3(-10,1.1,10),collider='box')
b2 = Entity(model='quad', texture="kenney_assets/Bonus/yellowCrystal.png", scale=(0.3,0.3), position=Vec3(-10,1.1,9),collider='box')
b3 = Entity(model='quad', texture="kenney_assets/Bonus/yellowCrystal.png", scale=(0.3,0.3), position=Vec3(-10,1.1,11),collider='box')

b4 = Entity(model='quad', texture="kenney_assets/Bonus/yellowGem.png", scale=(0.3,0.3), position=Vec3(-10,2.3,2),collider='box')
b5 = Entity(model='quad', texture="kenney_assets/Bonus/yellowGem.png", scale=(0.3,0.3), position=Vec3(-10,2.3,1),collider='box')

b6 = Entity(model='quad', texture="kenney_assets/Bonus/yellowJewel.png", scale=(0.3,0.3), position=Vec3(-10,2.3,-2),collider='box')
b7 = Entity(model='quad', texture="kenney_assets/Bonus/yellowJewel.png", scale=(0.3,0.3), position=Vec3(-10,2.3,-1),collider='box')
b8 = Entity(model='quad', texture="kenney_assets/Bonus/yellowJewel.png", scale=(0.3,0.3), position=Vec3(-10,2.3,-3),collider='box')
bonuses = [b1, b2, b3, b4, b5, b6, b7, b8]
bonus_images = ['yellowGem','yellowCrystal','yellowJewel']

sun = DirectionalLight()
sun.look_at(Vec3(1,-1,-1))

sky = Sky()


# Create an update function (automatically called during each frame)
def update():
    global m, num, text
    m += 1
    n = m % n_frame
    speed = 0.5

    for bonus in bonuses:
        bonus.rotation_y += time.dt * 400

        # Collision
        if abs(player.x - bonus.x) < 0.5 and abs(player.y - bonus.y) < 0.8:
            Animation('assets/flame', color=color.green, scale=1, position=(bonus.x, bonus.y + 0.4),
                      fps=20, loop=False, autoplay=True)
            Audio('assets/coin_sound.wav')
            num += 100
            text.y = 1
            text = Text(text=f"Score {num}", position=(0, 0.4), origin=(0, 0), scale=2, color=color.yellow,
                        background=True)
            bonuses.remove(bonus)
            destroy(bonus)
            if num >= 100:
                Text(text="Thank You for Your Support!", origin=(0, 0), scale=3, color=color.yellow, background=True)
    check_player_dies()
    check_player_wins()


def check_player_wins():
    global num, text
    # player wins if he gets all bonuses (800 points)
    if num >= 800:
        # Player wins, send message, reset the score, put player at start position
        text.y = 1
        Text(text="YOU WIN!", position=(0, 0.2), origin=(0, 0), scale=3, color=color.yellow, background=True)
        num = 0
        player.x = 0
        player.y = .5


def check_player_dies():
    global num, text
    # player dies if he falls in the hole
    if player.y < -20:
        # Player dies, send message, reset the score, put player at start position
        Text(text="You died!", position=(0, 0.2), origin=(0, 0), scale=3, color=color.yellow, background=True)
        num = 0
        text.y = 1
        text = Text(text=f"Score {num}", position=(0, 0.4), origin=(0, 0), scale=2, color=color.yellow,
                    background=True)
        player.x = 0
        player.y = .5

def input(key):
    if key == 'tab':    # press tab to toggle edit/play mode
        ec.enabled = not ec.enabled
        player.enabled = not player.enabled


# Text
num = 0
text = Text(text=f"Score {num}",position=(0,0.4),origin=(0,0),scale=2,color=color.yellow,background=True)

app.run()
