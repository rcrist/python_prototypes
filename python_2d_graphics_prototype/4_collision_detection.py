# Notes
# Use 'quad' for sprite entities with a texture

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

window.title = "Scene Prototype"
app = Ursina()
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True

m = 0
n_frame = 400

# Create scene1 entity
scene1 = Entity()

# Add a player
player = PlatformerController2d(x=-6.8,y=-1.6, scale=(.4,.8,.01/2),color=color.white,
                                texture='kenney_assets/Player/character_robot_idle.png')


# Add kenny background assets to the scene
bg2 = Entity(parent=scene1, model='quad', scale=(20,10), texture='kenney_assets/backgrounds/set2_background.png',z=0.5)
bg2hills = Entity(parent=scene1, model='quad', scale=(20,10), texture='kenney_assets/backgrounds/set2_hills.png',z=0.4)
bg2tiles = Entity(parent=scene1, model='quad', scale=(20,10), texture='kenney_assets/backgrounds/set2_tiles.png',z=0.3)
scene1.enabled = True

# Add fixed platforms
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_03.png", position=Vec2(-6.8,-3.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_05.png", position=Vec2(-6.8,-2.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_14.png", position=Vec2(-5.8,-3.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_10.png", position=Vec2(-5.8,-2.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_05.png", position=Vec2(-4.8,-3.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_05.png", position=Vec2(-3.8,-3.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_13.png", position=Vec2(-2.8,-3.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_03.png", position=Vec2(-2.8,-2.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_04.png", position=Vec2(-2.8,-1.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_06.png", position=Vec2(-1.8,-1.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_03.png", position=Vec2(-1.8,-2.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_03.png", position=Vec2(-1.8,-3.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_04.png", position=Vec2(1.2,-3.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_05.png", position=Vec2(2.2,-3.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_05.png", position=Vec2(3.2,-3.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_13.png", position=Vec2(4.2,-3.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_03.png", position=Vec2(5.2,-3.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_03.png", position=Vec2(6.2,-3.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_03.png", position=Vec2(7.2,-3.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_11.png", position=Vec2(4.2,-2.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_22.png", position=Vec2(5.2,-2.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_23.png", position=Vec2(6.2,-2.6), collider="box")
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_22.png", position=Vec2(7.2,-2.6), collider="box")

# Add moving platforms
xy = [[-4.8,0.6],[-0.8,0.6],[0.2,0.6],[3.2,1.6],[4.2,1.6]]
platforms = []
platform = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_02.png", position=xy[0], collider="box")
platforms.append(platform)
platforms.append(duplicate(platform, texture="kenney_assets/Tiles/tileBlue_15.png", position=xy[1]))
platforms.append(duplicate(platform, texture="kenney_assets/Tiles/tileBlue_16.png", position=xy[2]))
platforms.append(duplicate(platform, texture="kenney_assets/Tiles/tileBlue_24.png", position=xy[3]))
platforms.append(duplicate(platform, texture="kenney_assets/Tiles/tileBlue_25.png", position=xy[4]))

# Add random outline shapes in platforms
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/outlineGem.png", scale=(0.5,0.5), position=Vec2(-4.8,-0.3))
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/outlineCrystal.png", scale=(0.5,0.5), position=Vec2(-0.3,-0.3))
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/outlineJewel.png", scale=(0.5,0.5), position=Vec2(3.7,0.7))

# Create the bonus items
bonuses = []
bonus_images = ['blueGem','blueCrystal','blueJewel']

for i in range(3):
    if i == 0:
        bonus = Entity(parent=scene1, model='quad', texture="kenney_assets/Bonus/" + bonus_images[i], scale=(0.3, 0.3),
                       x=xy[i][0] - 0.5, y=xy[i][1] + 1)
        bonuses.append(bonus)
        bonuses.append(duplicate(bonus, x=xy[i][0] + 0.5))
    elif i == 1:
        bonus = Entity(parent=scene1, model='quad', texture="kenney_assets/Bonus/" + bonus_images[i], scale=(0.3, 0.3),
                       x=xy[i][0] - 0.5, y=xy[i][1] + 1)
        bonuses.append(bonus)
        bonuses.append(duplicate(bonus, x=xy[i][0] + 0.5))
        bonuses.append(duplicate(bonus, x=xy[i+1][0] + 0.6))
    elif i == 2:
        bonus = Entity(parent=scene1, model='quad', texture="kenney_assets/Bonus/" + bonus_images[i], scale=(0.3, 0.3),
                       x=xy[i+1][0] - 0.4, y=xy[i+1][1] + 1)
        bonuses.append(bonus)
        bonuses.append(duplicate(bonus, x=xy[i + 1][0] + 0.5, y=xy[i + 1][1]+1))
        bonuses.append(duplicate(bonus, x=xy[i + 2][0] + 0.4, y=xy[i + 2][1]+1))

# Add walls to confine the player
Entity(parent=scene1, model='quad', color=color.gray, scale=(0.2,20), position=Vec2(-7.2,-3.6), collider="box")
Entity(parent=scene1, model='quad', color=color.gray, scale=(0.2,20), position=Vec2(7.2,-3.6), collider="box")


# Create keyboard handler
def input(key):
    pass


# Create an update function (automatically called during each frame)
def update():
    global m, num, text
    m += 1
    n = m % n_frame
    speed = 0.5 if n < n_frame // 2 else -0.5

    for platform in platforms:
        platform.x += time.dt * speed

    for bonus in bonuses:
        bonus.x += time.dt * speed
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
            if num >= 1000:
                Text(text="Thank You for Your Support!", origin=(0, 0), scale=3, color=color.yellow, background=True)


# Text
num = 0
text = Text(text=f"Score {num}",position=(0,0.4),origin=(0,0),scale=2,color=color.yellow,background=True)

app.run()
