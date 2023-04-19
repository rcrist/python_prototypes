from ursina import *

app = Ursina()

# Kenny tan backgrounds
bgs1 = Entity()
bg1 = Entity(model='quad', scale=(20,10), texture='kenney_assets/backgrounds/set1_background.png',z=0.5)
bg1hills = Entity(model='quad', scale=(20,10), texture='kenney_assets/backgrounds/set1_hills.png',z=0.4)
bg1tiles = Entity(model='quad', scale=(20,10), texture='kenney_assets/backgrounds/set1_tiles.png',z=0.3)
bg1.parent = bgs1
bg1hills.parent = bgs1
bg1tiles.parent = bgs1
bgs1.enabled = False

# Kenney purple backgrounds
bgs2 = Entity()
bg2 = Entity(model='quad', scale=(20,10), texture='kenney_assets/backgrounds/set2_background.png',z=0.5)
bg2hills = Entity(model='quad', scale=(20,10), texture='kenney_assets/backgrounds/set2_hills.png',z=0.4)
bg2tiles = Entity(model='quad', scale=(20,10), texture='kenney_assets/backgrounds/set2_tiles.png',z=0.3)
bg2.parent = bgs2
bg2hills.parent = bgs2
bg2tiles.parent = bgs2
bgs2.enabled = True

# Kenney light tan backgrounds
bgs3 = Entity()
bg3 = Entity(model='quad', scale=(20,10), texture='kenney_assets/backgrounds/set3_background.png',z=0.5)
bg3hills = Entity(model='quad', scale=(20,10), texture='kenney_assets/backgrounds/set3_hills.png',z=0.4)
bg3tiles = Entity(model='quad', scale=(20,10), texture='kenney_assets/backgrounds/set3_tiles.png',z=0.3)
bg3.parent = bgs3
bg3hills.parent = bgs3
bg3tiles.parent = bgs3
bgs3.enabled = False

# Kenney brown backgrounds
bgs4 = Entity()
bg4= Entity(model='quad', scale=(20,10), texture='kenney_assets/backgrounds/set4_background.png',z=0.5)
bg4hills = Entity(model='quad', scale=(20,10), texture='kenney_assets/backgrounds/set4_hills.png',z=0.4)
bg4tiles = Entity(model='quad', scale=(20,10), texture='kenney_assets/backgrounds/set4_tiles.png',z=0.3)
bg4.parent = bgs4
bg4hills.parent = bgs4
bg4tiles.parent = bgs4
bgs4.enabled = False


bgs = [bgs1, bgs2, bgs3, bgs4]
index = 1


# Rotate though background is "space" key is pressed
def input(key):
    global index
    if key == "space":
        bgs[index].enabled = False
        index += 1
        if index > 3:
            index = 0
        bgs[index].enabled = True


app.run()
