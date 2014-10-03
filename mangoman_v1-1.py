################################################################################
################################################################################
############################                           #########################
############################      THE ADVENTURES       #########################
############################       OF MANGO MAN        #########################
############################                           #########################
############################   Created by Paula Yuan   #########################
############################                           #########################
################################################################################
################################################################################

from __future__ import division
from visual import *

scene.title = "Mango Man"
scene.fullscreen = True
scene.forward = (0, -1, -1)
scene.center = (0, 0, 5)

###################### Initialize some crucial components ######################

# Most of the components
components = []

# Define position coordinates.
east = 0
south = pi/2
west = pi
north = -pi/2

#--------------------------------- Game Stage ---------------------------------#

stage = frame()
floor = box(frame = stage, pos = (0, 0, 0), size = (100, 0.5, 100))
wallN = box(frame = stage, pos = (0, 0.75, -50.25), size = (101, 2, 0.5))
wallE = box(frame = stage, pos = (50.25, 0.75, 0), size = (0.5, 2, 101))
wallS = box(frame = stage, pos = (0, 0.75, 50.25), size = (101, 2, 0.5))
wallW = box(frame = stage, pos = (-50.25, 0.75, 0), size = (0.5, 2, 101))
stage.visible = False

#--------------------------------- Mango Man ----------------------------------#

def createMangoMan(radius):
    """Creates Mango Man"""
    
    global mangoMan

    mangoMan = frame(pos = vector(0, radius + floor.height / 2, 0))
    mangoMan.r = radius
    mangoMan.o = south
    mangoMan.s = 2
    mangoMan.dead = False

    # Mango Man's body
    mangoMan.body = sphere(frame = mangoMan, radius = radius, pos = (0, 0, 0),
                           color = color.orange)

    # Mango Man's eyes
    mangoMan.lEye = sphere(frame = mangoMan, radius = 0.4 * radius,
                           pos = (0.75 * radius * cos(mangoMan.o - pi/6), 0,
                                  0.75 * radius * sin(mangoMan.o - pi/6)))
    mangoMan.rEye = sphere(frame = mangoMan, radius = 0.4 * radius,
                    pos = (0.75 * radius * cos(mangoMan.o + pi/6), 0,
                           0.75 * radius * sin(mangoMan.o + pi/6)))
    mangoMan.lPupil = sphere(frame = mangoMan, radius = radius / 8,
                      pos = (1.1 * radius * cos(mangoMan.o - pi/6), 0,
                             1.1 * radius * sin(mangoMan.o - pi/6)),
                      color = color.black)
    mangoMan.rPupil = sphere(frame = mangoMan, radius = radius / 8,
                      pos = (1.1 * radius * cos(mangoMan.o + pi/6), 0,
                             1.1 * radius * sin(mangoMan.o + pi/6)),
                      color = color.black)

    components.append(mangoMan)

#--------------------------------- Evil Mango ---------------------------------#

def createEvilMango(speed):
    """Creates the Evil Mango"""

    global evilMango

    evilMango = frame(pos = vector(-40, 10.25, -40))

    evilMango.r = 10
    evilMango.o = pi / 4
    evilMango.s = speed
    evilMango.dead = False

    # Evil Mango's body
    evilMango.body = sphere(frame = evilMango, radius = 10, pos = (0, 0, 0),
                     color = color.orange)

    # Evil Mango's eyes
    evilMango.lEye = sphere(frame = evilMango, radius = 4,
                            pos = (7.5 * cos(evilMango.o - pi/6), 0,
                                   7.5 * sin(evilMango.o - pi/6)))
    evilMango.rEye = sphere(frame = evilMango, radius = 4,
                            pos = (7.5 * cos(evilMango.o + pi/6), 0,
                                   7.5 * sin(evilMango.o + pi/6)))
    evilMango.lPupil = sphere(frame = evilMango, radius = 1.25,
                              pos = (11 * cos(evilMango.o - pi/6), 0,
                                     11 * sin(evilMango.o - pi/6)),
                              color = (0.5, 0, 0), material = materials.emissive)
    evilMango.rPupil = sphere(frame = evilMango, radius = 1.25,
                              pos = (11 * cos(evilMango.o + pi/6), 0,
                                     11 * sin(evilMango.o + pi/6)),
                              color = (0.5, 0, 0), material = materials.emissive)
    evilMango.lEyebrow = box(frame = evilMango, size = (6, 1, 0.25),
                             pos = (10 * cos(evilMango.o - pi/6), 4,
                                    10 * sin(evilMango.o - pi/6)),
                             axis = (cos(evilMango.o + pi/3), -0.25,
                                     sin(evilMango.o + pi/3)),
                             color = color.black)
    evilMango.rEyebrow = box(frame = evilMango, size = (6, 1, 0.25),
                             pos = (10 * cos(evilMango.o + pi/6), 4,
                                    10 * sin(evilMango.o + pi/6)),
                             axis = (cos(evilMango.o - pi/3), -0.25,
                                     sin(evilMango.o - pi/3)),
                             color = color.black)

    components.append(evilMango)

#------------------------------ Welcome Message -------------------------------#

def displayWelcome():
    """Displays welcome message"""

    global welcome
    
    welcomeMessage = ""
    welcomeMessage += "Welcome to the adventures of Mango Man.\n"
    welcomeMessage += "To play, move Mango Man around with the arrow keys.\n"
    welcomeMessage += "Your objective is to devour mangoes and grow big.\n\n"
    welcomeMessage += "Every now and then, a new mango spawns.\n\n"
    welcomeMessage += "Watch out for mangoes that are bigger than you.\n"
    welcomeMessage += "If they roll over you, you die.\n\n"
    welcomeMessage += "Your ultimate goal is to defeat the evil mango.\n"
    welcomeMessage += "You do this by squishing him once you're big enough.\n\n"
    welcomeMessage += "Best of luck on your endeavors. Press space to continue."

    welcome = label(pos = (0, -5, 0), text = welcomeMessage)

    components.append(welcome)

#------------------------- Difficulty Level Selection -------------------------#

def selectDifficulty():
    """Selects difficulty level"""

    global mangoMan, evilMango

    leFrame = frame()
    leFrame.rotate(axis = (1, 0, 0), angle = -pi/4)
    
    text(pos = (0, 10, 0), align = 'center', height = 7, frame = leFrame,
         text = "Select your\ndifficulty")

    easy = box(pos = (-15, -10, 0), size = (20, 10, 1),  color = color.green,
               frame = leFrame)
    text(pos = (-15, -13, 1), align = 'center', height = 6, text = "Easy",
         frame = leFrame)

    hard = box(pos = (15, -10, 0), size = (20, 10, 1), color = color.red,
               frame = leFrame)
    text(pos = (15, -13, 1), align = 'center', height = 6, text = "Hard",
         frame = leFrame)

    while True:
        if scene.mouse.events:
            m = scene.mouse.getevent()
            if m.click == "left" and m.pick == easy:
                createMangoMan(2)
                createEvilMango(0)
                break
            elif m.click == "left" and m.pick== hard:
                createMangoMan(1)
                createEvilMango(0.1)
                break

    leFrame.visible = False

#----------------------------- Mango Generation -------------------------------#

mangoes = [] # a list of all the mangoes

def generateMango(min, max):
    """Generates a mango whose radius falls between min and max"""

    global mangoes

    r = random.uniform(min, max)              
    color = (1, random.uniform(0.25, 0.75), 0)

    acceptable = False

    # A mango is acceptable if it's not going to squish mangoMan instantaneously
    while not acceptable:

        if random.random() < 0.25:
            x = random.randint(-50 + r, 50 - r)
            z = 50 - r
            v = vector(0, 0, random.uniform(-0.4, -0.1))
        elif random.random() < 0.5:
            x = random.randint(-50 + r, 50 - r)
            z = -50 + r
            v = vector(0, 0, random.uniform(0.1, 0.4))
        elif random.random() < 0.75:
            x = 50 - r
            z = random.randint(-50 + r, 50 - r)
            v = vector(random.uniform(-0.4, 0.1), 0, 0)
        else:
            x = -50 + r
            z = random.randint(-50 + r, 50 - r)
            v = vector(random.uniform(0.1, 0.4), 0, 0)
        p = vector(x, r + floor.height / 2, z) + v

        predictedD = (p + 100 * v) - mangoMan.pos
        if predictedD.mag > 0:
            acceptable = True
    
    mangoes.append(sphere(radius = r, pos = p, color = color))
    mangoes[len(mangoes) - 1].v = v
    mangoes[len(mangoes) - 1].eaten = False       # sets eaten of mango to F

############################# Mango Man's Methods ##############################

def eat(victim):
    """Mango Man eats a smaller mango"""

    global mangoMan

    vSelf = 4/3*pi * mangoMan.r**2      # Mango man's volume
    vVictim = 4/3*pi * victim.radius**2 # Victim's volume

    # Change growth rate depending on size
    if victim.radius < 1:
        vSelf += vVictim
    elif victim.radius < 2:
        vSelf += 0.65 * vVictim
    elif victim.radius < 3:
        vSelf += 0.5 * vVictim
    elif victim.radius < 4:
        vSelf += 0.35 * vVictim
    elif victim.radius < 5:
        vSelf += 0.2 * vVictim
    else:
        vSelf += 0.1 * vVictim

    mangoMan.r = math.sqrt(vSelf / (4/3*pi))

    victim.visible = False

def redrawMangoMan():
    """Redraws Mango Man when he grows, moves, or turns."""

    global mangoMan

    mangoMan.body.radius = mangoMan.r
    
    mangoMan.lEye.radius = mangoMan.rEye.radius = 0.4 * mangoMan.r
    mangoMan.lEye.pos = (0.75 * mangoMan.r * cos(mangoMan.o - pi/6), 0,
                         0.75 * mangoMan.r * sin(mangoMan.o - pi/6))
    mangoMan.rEye.pos = (0.75 * mangoMan.r * cos(mangoMan.o + pi/6), 0,
                         0.75 * mangoMan.r * sin(mangoMan.o + pi/6))
    
    mangoMan.lPupil.radius = mangoMan.rPupil.radius = mangoMan.r / 8
    mangoMan.lPupil.pos = (1.1 * mangoMan.r * cos(mangoMan.o - pi/6), 0,
                           1.1 * mangoMan.r * sin(mangoMan.o - pi/6))
    mangoMan.rPupil.pos = (1.1 * mangoMan.r * cos(mangoMan.o + pi/6), 0,
                           1.1 * mangoMan.r * sin(mangoMan.o + pi/6))
    
    mangoMan.pos.y = mangoMan.r + floor.height / 2

def squishMangoMan():
    """Replaces Mango Man with a squished Mango Man"""

    global mangoMan, deadMangoMan
    
    mangoMan.visible = False

    deadMangoMan = frame(pos = (mangoMan.pos.x, floor.height / 2,
                                mangoMan.pos.z))

    # Dead Mango Man's body
    body = cylinder(frame = deadMangoMan, radius = mangoMan.r, pos = (0, 0, 0),
                     axis = (0, 0.01, 0), color = color.orange)

    # Dead Mango Man's eyes
    lEye = cylinder(frame = deadMangoMan, radius = 0.4 * mangoMan.r,
                     pos = (mangoMan.r/2 * cos(mangoMan.o - pi/2), 0.01,
                            mangoMan.r/2 * sin(mangoMan.o - pi/2)),
                     axis = (0, 0.01, 0))
    rEye = cylinder(frame = deadMangoMan, radius = 0.4 * mangoMan.r,
                     pos = (mangoMan.r/2 * cos(mangoMan.o + pi/2), 0.01,
                            mangoMan.r/2 * sin(mangoMan.o + pi/2)),
                     axis = (0, 0.01, 0))
    lPupil = cylinder(frame = deadMangoMan, radius = mangoMan.r / 8,
                       pos = (mangoMan.r/2 * cos(mangoMan.o - pi/2), 0.02,
                              mangoMan.r/2 * sin(mangoMan.o - pi/2)),
                       axis = (0, 0.01, 0), color = color.black)
    rPupil = cylinder(frame = deadMangoMan, radius = mangoMan.r / 8,
                       pos = (mangoMan.r/2 * cos(mangoMan.o + pi/2), 0.02,
                              mangoMan.r/2 * sin(mangoMan.o + pi/2)),
                       axis = (0, 0.01, 0), color = color.black)

    mangoMan.dead = True

    components.append(deadMangoMan)

############################# Evil Mango's Methods #############################

def trackMangoMan():
    """Evil Mango follows Mango Man around."""

    global evilMango, mangoMan, victorySpeech

    d = mangoMan.pos - evilMango.pos # Distance between Mango Man and Evil Mango
    d.y = 0
    evilMango.o = math.atan2(d.z, d.x)

    if d.mag > 1: # Evil Mango chases Mango Man if he's not close enough
        evilMango.v = evilMango.s * d.norm()
    elif mangoMan.dead: # Evil Mango's victory speech if he wins
        evilMango.v = vector(0, 0, 0)
        speech = "MUAHAHAHA! Your sweet mango flesh is now MINE!"
        victorySpeech = label(pos = (evilMango.pos.x,
                                       evilMango.pos.y + evilMango.r + 1,
                                       evilMango.pos.z),
                                text = speech)
        components.append(victorySpeech)

    evilMango.pos += evilMango.v

def inBetween(arg, a, b):
    """Returns true if arg is in between a and b"""
    return arg > a and arg < b

def runAway():
    """Evil Mango runs away from Mango Man."""

    global evilMango, mangoMan

    # Current angle of Mango Man from the origin
    mangoMan.angle = math.atan2(-mangoMan.pos.z, mangoMan.pos.x)
    
    # Current angle of the Evil Mango from the origin
    evilMango.angle = math.atan2(-evilMango.pos.z, evilMango.pos.x)

    # If the evil mango is in quadrant 1
    if inBetween(evilMango.angle, 0, pi/2):
        if inBetween(mangoMan.angle, -pi/2, pi/4):
            destination = vector(-45, 0, -45)
        elif inBetween(mangoMan.angle, pi/4, pi):
            destination = vector(45, 0, 45)
        else:
            destination = vector(45, 0, -45)
    elif inBetween(evilMango.angle, pi/2, pi):
        if inBetween(mangoMan.angle, 0, 3*pi/4):
            destination = vector(-45, 0, 45)
        elif inBetween(mangoMan.angle, -pi/2, 0):
            destination = vector(-45, 0, 45)
        else:
            destination = vector(45, 0, -45)
    elif inBetween(evilMango.angle, -pi, -pi/2):
        if inBetween(mangoMan.angle, 0, pi/2):
            destination = vector(-45, 0, 45)
        elif inBetween(mangoMan.angle, -3*pi/4, 0):
            destination = vector(-45, 0, -45)
        else:
            destination = vector(45, 0, 45)
    else:
        if inBetween(mangoMan.angle, -pi/4, pi/2):
            destination = vector(-45, 0, 45)
        elif inBetween(mangoMan.angle, -pi, -pi/4):
            destination = vector(45, 0, -45)
        else:
            destination = vector(45, 0, 45)

    d = destination - evilMango.pos
    d.y = 0
    evilMango.o = math.atan2(d.z, d.x)
    evilMango.s = 0.3
    if d.mag > 1:
        evilMango.v = evilMango.s * d.norm()
    else:
        evilMango.v = vector(0, 0, 0)
    evilMango.pos += evilMango.v

def redrawEvilMango():
    """Redraws the Evil Mango as he moves and turns."""

    global evilMango
    
    evilMango.lEye.pos = (7.5 * cos(evilMango.o - pi/6), 0,
                          7.5 * sin(evilMango.o - pi/6))
    evilMango.rEye.pos = (7.5 * cos(evilMango.o + pi/6), 0,
                          7.5 * sin(evilMango.o + pi/6))
    
    evilMango.lPupil.pos = (11 * cos(evilMango.o - pi/6), 0,
                            11 * sin(evilMango.o - pi/6))
    evilMango.rPupil.pos = (11 * cos(evilMango.o + pi/6), 0,
                            11 * sin(evilMango.o + pi/6))

    evilMango.lEyebrow.pos = (10 * cos(evilMango.o - pi/6), 4,
                              10 * sin(evilMango.o - pi/6))
    evilMango.lEyebrow.axis = (cos(evilMango.o + pi/3), -0.25,
                               sin(evilMango.o + pi/3))
    evilMango.rEyebrow.pos = (10 * cos(evilMango.o + pi/6), 4,
                              10 * sin(evilMango.o + pi/6))
    evilMango.rEyebrow.axis = (cos(evilMango.o - pi/3), -0.25,
                               sin(evilMango.o - pi/3))    

    evilMango.lEyebrow.size = (6, 1, 0.25)
    evilMango.rEyebrow.size = (6, 1, 0.25)

def squishEvilMango():
    """Replaces Evil Mango with a squished Evil Mango"""

    global evilMango
    
    evilMango.visible = False
    
    deadEvilMango = frame(pos = (evilMango.pos.x, floor.height / 2,
                                 evilMango.pos.z))
    r = 10
    
    # Dead Evil Mango's body
    body = cylinder(frame = deadEvilMango, radius = r, pos = (0, 0, 0),
                     axis = (0, 0.01, 0), color = color.orange)
    
    # Dead Evil Mango's eyes
    lEye = cylinder(frame = deadEvilMango, radius = 0.35 * r,
                    pos = (r/2 * cos(evilMango.o - pi/2), 0.01,
                           r/2 * sin(evilMango.o - pi/2)),
                    axis = (0, 0.01, 0))
    rEye = cylinder(frame = deadEvilMango, radius = 0.35 * r,
                    pos = (r/2 * cos(evilMango.o + pi/2), 0.01,
                           r/2 * sin(evilMango.o + pi/2)),
                    axis = (0, 0.01, 0))
    lPupil = cylinder(frame = deadEvilMango, radius = r / 9,
                      pos = (r/2 * cos(evilMango.o - pi/2), 0.02,
                             r/2 * sin(evilMango.o - pi/2)),
                      axis = (0, 0.01, 0), color = (0.5, 0, 0))
    rPupil = cylinder(frame = deadEvilMango, radius = r / 9,
                      pos = (r/2 * cos(evilMango.o + pi/2), 0.02,
                             r/2 * sin(evilMango.o + pi/2)),
                      axis = (0, 0.01, 0), color = (0.5, 0, 0))

    # Dead Evil Mango's eyebrows
    lEyebrow = box(frame = deadEvilMango, size = (6, 0.01, 1),
               pos = (6 * cos(evilMango.o - 3*pi/4), 0.03,
                      6 * sin(evilMango.o - 3*pi/4)),
               axis = (cos(evilMango.o + pi/3), 0, sin(evilMango.o + pi/4)),
               color = color.black)
    rEyebrow = box(frame = deadEvilMango, size = (6, 0.01, 1),
               pos = (6 * cos(evilMango.o + 3*pi/4), 0.05,
                      6 * sin(evilMango.o + 3*pi/4)),
               axis = (cos(evilMango.o - pi/3), 0, sin(evilMango.o - pi/4)),
               color = color.black)

    evilMango.dead = True

    components.append(deadEvilMango)

######################## Game Initialization and Over ##########################

def start():
    """Starts the game."""

    global counter, interval, mangoesEaten, gameOver
    global components, mangoes
    global mangoMan, evilMango
    global deadMangoMan, deadEvilMango

    components = [stage]
    mangoes = []
    counter = mangoesEaten = 0
    interval = random.randint(100, 1000)
    gameOver = gameStart = False
    deadMangoMan = deadEvilMango = frame()
    deadMangoMan.visible = deadEvilMango.visible = False

    displayWelcome()

    # Doesn't start the game until you press the spacebar
    while True:
        if scene.kb.keys:
            key = scene.kb.getkey()
            if key == ' ':
                break
    # Once you quit the loop, hide the welcome message
    welcome.visible = False
    
    # Time to select difficulty
    selectDifficulty()

    stage.visible = True
    
    for i in range(5):
        generateMango(0.5, 5)
    for i in range(10):
        generateMango(0.5, 1)

    

def gameIsOver():
    """Game over le sadface"""

    global gameOver, evilMango, mangoMan, mangoesEaten
    global endMessage, victorySpeech

    gameOver = True

    if evilMango.dead:
        message = "Congratulations! You have defeated the evil mango!\n"
        
        victorySpeech = label(pos = mangoMan.pos,
                        text = "Fuck you, Evil Mango! I have defeated you!")
        victorySpeech.pos.y += mangoMan.r + 1
        components.append(victorySpeech)

    elif mangoMan.dead:
        message = "You died. Game over.\n"

    message += "You devoured " + str(mangoesEaten) + " mangoes and grew\n"
    message += str(mangoMan.r) + " times bigger."

    endMessage = label(pos = (0, 10, -50), text = message)
    components.append(endMessage)

def restart():
    """Restarts the game."""

    global components
    global counter, mangoesEaten, gameOver, gameStart

    # Delete all the components
    for component in components:
        component.visible = False

    # Delete all the mangos
    for mango in mangoes:
        mango.visible = False

    # Reset everything
    counter = mangoesEaten = 0
    gameOver = gameStart = False
    
    # Start the game
    start()

################################### LET'S GO ###################################
start()

while True:

    rate(100)
    counter += 1    

    # Randomly generate mangoes    
    if counter % interval == 0 and not gameOver:
        generateMango(0.5, mangoMan.r + 2)
        interval = random.randint(200, 1000)
    
    # Response to key commands
    if scene.kb.keys:

        key = scene.kb.getkey()

        # Control Mango Man's Movement
        if not gameOver:
            canMove = True
            if key == 'up' and mangoMan.pos.z > mangoMan.r - 48:
                mangoMan.o = north
            elif key == 'right' and mangoMan.pos.x < 48 - mangoMan.r:
                mangoMan.o = east
            elif key == 'down' and mangoMan.pos.z < 48 - mangoMan.r:
                mangoMan.o = south
            elif key == 'left' and mangoMan.pos.x > mangoMan.r - 48:
                mangoMan.o = west
            else:
                canMove = False
            if canMove:
                mangoMan.pos.x += mangoMan.s * cos(mangoMan.o)
                mangoMan.pos.z += mangoMan.s * sin(mangoMan.o)
                
        if key == 'q':
            break
        if key == 'r':
            restart()

    # Iterate through all of the mangoes
    for mango in mangoes:

        # Makes the mangoes move around according to their assigned velocity
        if math.fabs(mango.pos.x + mango.v.x) <= 50 - mango.radius and \
           math.fabs(mango.pos.z + mango.v.z) <= 50 - mango.radius:
            mango.pos += mango.v
        else:
            mango.v = -mango.v

        # If Mango Man is near another smaller mango, he eats it
        d = mangoMan.pos - mango.pos
        maxD = mangoMan.r + mango.radius
        if d.mag < maxD and not mango.eaten and not gameOver:
            if mango.radius <= mangoMan.r:
                eat(mango)
                mangoesEaten += 1
                mango.eaten = True
            elif not gameOver and not evilMango.dead:
                squishMangoMan()
                gameIsOver()

        # Slow down the mangoes if game is over
        if gameOver:
            if mango.v > 0:
                if mango.v.x > 0:
                    mango.v.x -= 0.001
                elif mango.v.x < 0:
                    mango.v.x += 0.001
                elif mango.v.z > 0:
                    mango.v.z -= 0.001
                elif mango.v.z < 0:
                    mango.v.z += 0.001

    # The Evil Mango follows you around
    if evilMango.r > mangoMan.r or gameOver:
        trackMangoMan()
    else:
        runAway()

    # If Mango Man gets close enough to the Evil Mango, someone gets squished
    d = mangoMan.pos - evilMango.pos
    maxD = mangoMan.r + evilMango.r
    if d.mag < maxD and not gameOver:
        if evilMango.r < mangoMan.r:
            squishEvilMango()
            gameIsOver()
        else:
            squishMangoMan()
            gameIsOver() 
    
    # When the Evil Mango gets squished, Mango Man gets on top of him
    d.y = 0
    if evilMango.dead:
        if d.mag > 2:
            mangoMan.v = -d
            mangoMan.pos += 0.01 * mangoMan.v
            redrawMangoMan()
        else:
            mangoMan.v = vector(0, 0, 0)      

    # Redraw that shit
    redrawMangoMan()
    redrawEvilMango()
