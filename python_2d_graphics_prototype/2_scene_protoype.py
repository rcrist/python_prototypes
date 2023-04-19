# Notes
# Use 'quad' for sprite entities with a texture

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

window.title = "Scene Prototype"
app = Ursina()
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True

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

# Add platforms to the scene (parent all entities to the scene entity)
p1 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_02.png", position=Vec2(-4.8,0.6), collider="box")
p2 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_03.png", position=Vec2(-6.8,-3.6), collider="box")
p3 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_05.png", position=Vec2(-6.8,-2.6), collider="box")
p4 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_14.png", position=Vec2(-5.8,-3.6), collider="box")
p5 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_10.png", position=Vec2(-5.8,-2.6), collider="box")
p6 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_05.png", position=Vec2(-4.8,-3.6), collider="box")
p7 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_05.png", position=Vec2(-3.8,-3.6), collider="box")
p8 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_13.png", position=Vec2(-2.8,-3.6), collider="box")
p9 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_03.png", position=Vec2(-2.8,-2.6), collider="box")
p10 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_04.png", position=Vec2(-2.8,-1.6), collider="box")
p11 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_06.png", position=Vec2(-1.8,-1.6), collider="box")
p12 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_03.png", position=Vec2(-1.8,-2.6), collider="box")
p13 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_03.png", position=Vec2(-1.8,-3.6), collider="box")
p14 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_15.png", position=Vec2(-0.8,0.6), collider="box")
p15 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_16.png", position=Vec2(0.2,0.6), collider="box")
p16 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_04.png", position=Vec2(1.2,-3.6), collider="box")
p17 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_05.png", position=Vec2(2.2,-3.6), collider="box")
p18 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_05.png", position=Vec2(3.2,-3.6), collider="box")
p19 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_13.png", position=Vec2(4.2,-3.6), collider="box")
p20 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_03.png", position=Vec2(5.2,-3.6), collider="box")
p21 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_03.png", position=Vec2(6.2,-3.6), collider="box")
p22 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_03.png", position=Vec2(7.2,-3.6), collider="box")
p23 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_11.png", position=Vec2(4.2,-2.6), collider="box")
p24 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_22.png", position=Vec2(5.2,-2.6), collider="box")
p25 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_23.png", position=Vec2(6.2,-2.6), collider="box")
p26 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_22.png", position=Vec2(7.2,-2.6), collider="box")
p27 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_24.png", position=Vec2(3.2,1.6), collider="box")
p28 = Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/tileBlue_25.png", position=Vec2(4.2,1.6), collider="box")

# Add random outline shapes in platforms
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/outlineGem.png", scale=(0.5,0.5), position=Vec2(-4.8,-0.3))
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/outlineCrystal.png", scale=(0.5,0.5), position=Vec2(-0.3,-0.3))
Entity(parent=scene1, model='quad', texture="kenney_assets/Tiles/outlineJewel.png", scale=(0.5,0.5), position=Vec2(3.7,0.7))

# Create the bonus items
Entity(parent=scene1, model='quad', texture="kenney_assets/Bonus/blueCrystal.png", scale=(0.3,0.3), position=Vec2(-1.0,1.3))
Entity(parent=scene1, model='quad', texture="kenney_assets/Bonus/blueCrystal.png", scale=(0.3,0.3), position=Vec2(-0.3,1.3))
Entity(parent=scene1, model='quad', texture="kenney_assets/Bonus/blueCrystal.png", scale=(0.3,0.3), position=Vec2(0.4,1.3))

Entity(parent=scene1, model='quad', texture="kenney_assets/Bonus/blueGem.png", scale=(0.3,0.3), position=Vec2(-5.1,1.3))
Entity(parent=scene1, model='quad', texture="kenney_assets/Bonus/blueGem.png", scale=(0.3,0.3), position=Vec2(-4.5,1.3))

Entity(parent=scene1, model='quad', texture="kenney_assets/Bonus/blueJewel.png", scale=(0.3,0.3), position=Vec2(3.0,2.3))
Entity(parent=scene1, model='quad', texture="kenney_assets/Bonus/blueJewel.png", scale=(0.3,0.3), position=Vec2(3.7,2.3))
Entity(parent=scene1, model='quad', texture="kenney_assets/Bonus/blueJewel.png", scale=(0.3,0.3), position=Vec2(4.4,2.3))

# Add walls to confine the player
Entity(parent=scene1, model='quad', color=color.gray, scale=(0.2,20), position=Vec2(-7.2,-3.6), collider="box")
Entity(parent=scene1, model='quad', color=color.gray, scale=(0.2,20), position=Vec2(7.2,-3.6), collider="box")

# Create keyboard handler
def input(key):
    pass


# Create an update function (automatically called during each frame)
def update():
    pass


app.run()
