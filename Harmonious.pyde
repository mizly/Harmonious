from com.jogamp.opengl import GLContext, GL3
from intro import intro
from options import options
from credit import credit
from levelSelect import levelSelect
from level1 import level1
ENABLE_P2D = False

def settings():
    '''
    Sets the screen to fullscreen. Change ENABLE_P2D to True if you want to use OpenGL accelerated graphics.
    '''
    if ENABLE_P2D:
        fullScreen(P2D)
    else:
        fullScreen()
    
def setup():
    '''
    Setups the sketch, and initializes variables for various functions.
    '''
    stroke(255)
    strokeWeight(5)
    frameRate(60)
    smooth(8)

    #loading font
    cartograph = createFont("CartographCF-ExtraLight.ttf",displayWidth/15)
    textAlign(CENTER)
    rectMode(CENTER)
    textFont(cartograph)
    
    #Iinitializing global variables
    global status, spacing, timer
    global yOffset, yOffset2, yOffset3, yOffset4
    global volMaster, volMusic, volFX, masterLocked, musicLocked,FXLocked
    global locked
    global level
    global yInt,slope
    global yIntLocked,slopeLocked
    status, spacing, timer = "level1", 200, 0
    yOffset, yOffset2, yOffset3, yOffset4 = 0,0,0,0
    volMaster,volMusic,volFX, masterLocked,musicLocked,FXLocked = 100,100,100,False,False,False
    locked = False
    level = 1
    yInt,slope = 0,0
    yIntLocked,slopeLocked = False,False
    '''
    add_library('controlP5')
    global cp5
    cp5 = ControlP5(this)
    print(ControlP5.printPublicMethodsFor(Slider))
    cp5.addSlider("Quadratic coefficient")
    cp5.getController("Quadratic coefficient").setPosition(int(displayWidth/1.5),int(displayHeight/9))
    cp5.getController("Quadratic coefficient").setRange(-10,10)'''
    
def draw():
    '''
    Main draw function. Refreshes the screen __ times a second (defined by frameRate in setup)
    '''
    global status, introStarted, spacing, timer
    global yOffset, yOffset2, yOffset3, yOffset4
    global volMaster, volMusic, volFX, masterLocked,musicLocked,FXLocked
    global locked
    global level
    global yInt,slope
    global yIntLocked,slopeLocked
    timer+=1
    background(255)
    if status == "levelselect": #Level select screen
        status, timer,locked, level,yInt,slope = levelSelect(ENABLE_P2D,status, timer,locked,level,yInt,slope)
    if status == "intro": #Title screen
        spacing, status, timer, yOffset, yOffset2, yOffset3, yOffset4 = intro(ENABLE_P2D,spacing, status, timer, yOffset, yOffset2, yOffset3, yOffset4)
    if status == "options": #Options screen
        status, volMaster,volMusic,volFX,masterLocked,musicLocked,FXLocked,locked = options(ENABLE_P2D,status, volMaster,volMusic,volFX,masterLocked,musicLocked,FXLocked,locked)
    if status == "credit": #Credit screen
        status, timer,locked = credit(ENABLE_P2D,status, timer,locked)
    
    #Levels
    if status == "level1": #Level 1
        status, timer,locked,yInt,slope,yIntLocked,slopeLocked = level1(ENABLE_P2D,status, timer,locked,yInt,slope,yIntLocked,slopeLocked)
        
        
        
def graph():
    
    #quadraticValue = cp5.getController("Quadratic coefficient").getValue()
    quadraticValue = 2
    background(200)
    #Drawing the outline of the graph
    line(displayWidth/2,0,displayWidth/2,displayHeight)
    line(0,displayHeight/2,displayWidth,displayHeight/2)
    fill(0,0,0)
    
    for a in range(40):
        text(a-20,displayWidth/40*a,displayHeight/2)
        text((a-20)*-1, displayWidth/2, displayHeight/40*a)

    text("Plotting y = %.1fx^2" % quadraticValue , displayWidth/1.5, displayHeight/10)
    
    startCoordsX = -5
    startCoordsY = 25
    middleCoordsX = 0
    middleCoordsY = 0
    endCoordsX = 5
    endCoordsY = 25
    
    noFill()
    
    beginShape()
    vertex((startCoordsX+20)*displayWidth/40,(startCoordsY*-1+20)*displayHeight/40)
    quadraticVertex((middleCoordsX+20)*displayWidth/40,(middleCoordsY+startCoordsY+20)*displayHeight/40,(endCoordsX+20)*displayWidth/40,(endCoordsY*-1+20)*displayHeight/40)
    endShape()
