################################################################################
################################# HEY TAMEEZY ##################################
################################# YOU A WINNA ##################################
################################# GOOD ON YOU ##################################
#################################  GRATZ BRO  ##################################
################################################################################

from visual import *

winner = "Senpai Tameezy"

scene.forward = (0, -1, -4)
scene.width = 600
scene.height = 700
east = 0
south = pi/2
west = pi
north = -pi/2

################################# Trophy Base ##################################

trophyBase = frame(pos = (0, -10, 0))

floor = box(frame = trophyBase, pos = (0, 10, 0), size = (20, 5, 20),
            color = (0.8, 0.6, 0), material = materials.chrome)
base = box(frame = trophyBase, pos = (0, -5, 0), size = (20, 5, 20),
           color = (0.7, 0.4, 0), material = materials.wood)

name = text(frame = trophyBase, pos = (0, 9.25, 10), align = 'center',
            text = winner, color = (0.7, 0.4, 0), height = 2,
            material = materials.chrome)

plaque = box(frame = trophyBase, pos = (0, -5, 10), size = (18, 4, 0.1),
             color = (1, 0.75, 0), material = materials.chrome)
plaqueText = text(frame = trophyBase, pos = (0, -4.6, 10), align = 'center',
                  text = "Congratulations on defeating\nthe evil mango!",
                  color = color.black)

nePillar = cylinder(frame = trophyBase, pos = (8, -5, -8), radius = 2,
                    axis = (0, 13, 0), color = (0.8, 0.6, 0),
                    material = materials.chrome)
nwPillar = cylinder(frame = trophyBase, pos = (-8, -5, -8), radius = 2,
                    axis = (0, 13, 0), color = (0.8, 0.6, 0),
                    material = materials.chrome)
swPillar = cylinder(frame = trophyBase, pos = (-8, -5, 8), radius = 2,
                    axis = (0, 13, 0), color = (0.8, 0.6, 0),
                    material = materials.chrome)
sePillar = cylinder(frame = trophyBase, pos = (8, -5, 8), radius = 2,
                    axis = (0, 13, 0), color = (0.8, 0.6, 0),
                    material = materials.chrome)

mainMango = sphere(frame = trophyBase, pos = (0, 3, 0), radius = 4,
                   color = (1, 0.4, 0), material = materials.chrome,
                   opacity = 0.9)
mangoStand = cylinder(frame = trophyBase, pos = (0, -3, 0), radius = 2,
                      axis = (0, 5, 0), material = materials.glass)
sphere(frame = trophyBase, pos = (8, -0.5, -2.5), radius = 2,
       color = (1, 0.5, 0), material = materials.chrome, opacity = 0.9)
sphere(frame = trophyBase, pos = (8, -0.5, 2.5), radius = 2,
       color = (1, 0.3, 0), material = materials.chrome, opacity = 0.9)
sphere(frame = trophyBase, pos = (-8, -0.5, -2.5), radius = 2,
         color = (1, 0.7, 0), material = materials.chrome, opacity = 0.9)
sphere(frame = trophyBase, pos = (-8, -0.5, 2.5), radius = 2,
       color = (1, 0.2, 0), material = materials.chrome, opacity = 0.9)
sphere(frame = trophyBase, pos = (-2.5, -0.5, 8), radius = 2,
       color = (1, 0.6, 0), material = materials.chrome, opacity = 0.9)
sphere(frame = trophyBase, pos = (2.5, -0.5, 8), radius = 2,
       color = (1, 0.4, 0), material = materials.chrome, opacity = 0.9)
sphere(frame = trophyBase, pos = (-2.5, -0.5, -8), radius = 2,
       color = (1, 0.2, 0), material = materials.chrome, opacity = 0.9)
sphere(frame = trophyBase, pos = (2.5, -0.5, -8), radius = 2,
       color = (1, 0.5, 0), material = materials.chrome, opacity = 0.9)
                    
############################### Mango Man's Body ###############################

r = 10
p = vector(0, r + floor.height / 2, 0)
o = pi/2
mangoManIsDead = False

mangoMan = frame(pos = p)

# Mango Man's body
body = sphere(frame = mangoMan, radius = r, pos = (0, 0, 0),
              color = color.orange, material = materials.plastic)

# Mango Man's eyes
lEye = sphere(frame = mangoMan, radius = 0.4 * r,
              pos = (0.75 * r * cos(o - pi/6), 0, 0.75 * r * sin(o - pi/6)),
              material = materials.plastic)
rEye = sphere(frame = mangoMan, radius = 0.4 * r,
              pos = (0.75 * r * cos(o + pi/6), 0, 0.75 * r * sin(o + pi/6)),
              material = materials.plastic)
lPupil = sphere(frame = mangoMan, radius = r / 8,
                pos = (1.1 * r * cos(o - pi/6), 0, 1.1 * r * sin(o - pi/6)),
                color = color.black, material = materials.plastic)
rPupil = sphere(frame = mangoMan, radius = r / 8,
                pos = (1.1 * r * cos(o + pi/6), 0, 1.1 * r * sin(o + pi/6)),
                color = color.black, material = materials.plastic)

############################### Dead Evil Mango ################################

deadEvilMango = frame(pos = (0, floor.height / 2, 0))

# Dead Evil Mango's body
body2 = cylinder(frame = deadEvilMango, radius = r, pos = (0, 0, 0),
                 axis = (0, 0.01, 0), color = color.orange)

# Dead Evil Mango's eyes
lEye2 = cylinder(frame = deadEvilMango, radius = 0.35 * r,
                 pos = (r/2 * cos(o - pi/2), 0.01, r/2 * sin(o - pi/2)),
                 axis = (0, 0.01, 0))
rEye2 = cylinder(frame = deadEvilMango, radius = 0.35 * r,
                 pos = (r/2 * cos(o + pi/2), 0.01, r/2 * sin(o + pi/2)),
                 axis = (0, 0.01, 0))
lPupil2 = cylinder(frame = deadEvilMango, radius = r / 9,
                   pos = (r/2 * cos(o - pi/2), 0.02, r/2 * sin(o - pi/2)),
                   axis = (0, 0.01, 0), color = (0.5, 0, 0))
rPupil2 = cylinder(frame = deadEvilMango, radius = r / 9,
                   pos = (r/2 * cos(o + pi/2), 0.02, r/2 * sin(o + pi/2)),
                   axis = (0, 0.01, 0), color = (0.5, 0, 0))

# Dead Evil Mango's eyebrows
lEyebrow = box(frame = deadEvilMango, size = (6, 0.01, 1),
           pos = (6 * cos(o - 3*pi/4), 0.03, 6 * sin(o - 3*pi/4)),
           axis = (cos(o + pi/3), 0, sin(o + pi/4)),
           color = color.black)
rEyebrow = box(frame = deadEvilMango, size = (6, 0.01, 1),
           pos = (6 * cos(o + 3*pi/4), 0.05, 6 * sin(o + 3*pi/4)),
           axis = (cos(o - pi/3), 0, sin(o - pi/4)),
           color = color.black)

spin = True

while True:
    while spin:
        if scene.kb.keys:
            key = scene.kb.getkey()
            if key == ' ':
                spin = False
        rate(50)
        mangoMan.rotate(angle = 0.01, axis = (0, 1, 0))
        deadEvilMango.rotate(angle = 0.01, axis = (0, 1, 0))
        trophyBase.rotate(angle = 0.01, axis = (0, 1, 0))
    if scene.kb.keys:
            key = scene.kb.getkey()
            if key == ' ':
                spin = True
