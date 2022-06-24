from com.jogamp.opengl import GLContext, GL3
from intro import intro
from options import options
from instruction import instruction
from levelSelect import levelSelect
from detection import isMouseOverRect
from randomlevel import randomlevel
from randomgame import randomgame

for i in range(8):
    exec("from level%s import level%s" % (str(i+1),str(i+1)))

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
    mainFont = createFont("Consolas",displayWidth/15)
    textAlign(CENTER)
    rectMode(CENTER)
    textFont(mainFont)
    
    #Iinitializing global variables
    global status, timer
    global volMaster, volMusic, volFX, masterLocked, musicLocked,FXLocked
    global locked, locked2
    global level
    global yInt,slope, quadratic
    global yIntLocked,slopeLocked, quadraticLocked
    global yIntValue,slopeValue,quadraticValue
    
    status, timer = "intro", 0
    volMaster,volMusic,volFX, masterLocked,musicLocked,FXLocked = 100,100,100,False,False,False
    locked,locked2 = False,False
    level = 9
    yInt,slope,quadratic = 0,0,0
    yIntLocked,slopeLocked,quadraticLocked = False,False,False
    yIntValue,slopeValue,quadraticValue = 0,0,0
    
def draw():
    '''
    Main draw function. Refreshes the screen __ times a second (defined by frameRate in setup)
    '''
    global status, introStarted, timer
    global volMaster, volMusic, volFX, masterLocked,musicLocked,FXLocked
    global locked,locked2
    global level
    global yInt,slope,quadratic
    global yIntLocked,slopeLocked,quadraticLocked
    global yIntValue,slopeValue,quadraticValue
    timer+=1
    background(255)
    
    if status == "levelselect": #Level select screen
        status, timer,locked, level,yInt,slope,quadratic = levelSelect(ENABLE_P2D,status, timer,locked,level,yInt,slope,quadratic)
    if status == "intro": #Title screen
        status, timer = intro(ENABLE_P2D, status, timer)
    if status == "options": #Options screen
        status, timer, volMaster,volMusic,volFX,masterLocked,musicLocked,FXLocked,locked = options(ENABLE_P2D,status, timer, volMaster,volMusic,volFX,masterLocked,musicLocked,FXLocked,locked)
    if status == "instruction": #Credit screen
        status, timer,locked = instruction(ENABLE_P2D,status, timer,locked)
    if status == "random": #Random level generator screen
        status, timer,locked,yIntValue,slopeValue,quadraticValue = randomlevel(ENABLE_P2D,status, timer,locked,yIntValue,slopeValue,quadraticValue)
    
    #Levels
    if status in ["level1","level2","level3","level4"]:
        status, timer,locked,locked2,yInt,slope,yIntLocked,slopeLocked,level = globals()[status](ENABLE_P2D,status, timer,locked,locked2,yInt,slope,yIntLocked,slopeLocked,level)
    if status in ["level5","level6","level7","level8"]:
        status, timer,locked,locked2,yInt,slope,quadratic,yIntLocked,slopeLocked,quadraticLocked,level = globals()[status](ENABLE_P2D,status, timer,locked,locked2,yInt,slope,quadratic,yIntLocked,slopeLocked,quadraticLocked,level)
    if status == "randomgame": #random level
        status, timer,locked,locked2,yInt,slope,quadratic,yIntLocked,slopeLocked,quadraticLocked,level = randomgame(ENABLE_P2D,status, timer,locked,locked2,yInt,slope,quadratic,yIntLocked,slopeLocked,quadraticLocked,level,yIntValue,slopeValue,quadraticValue)

    #text(timer,200,200)
def keyPressed():
    '''
    Global function to detect singular keypresses
    
    Return: none
    '''
    
    global status
    global yInt,slope, quadratic
    
    #arrow key controls for fine slider movements
    if status == 'level1':
        if isMouseOverRect(displayWidth*0.75,displayHeight*0.7,displayWidth*0.15,displayHeight*0.03,30):
            if keyCode == LEFT:
                yInt = min(10,max(-10,yInt-0.1))
            if keyCode == RIGHT:
                yInt = min(10,max(-10,yInt+0.1))
    
    if status == "level2":        
        if isMouseOverRect(displayWidth*0.75,displayHeight*0.7,displayWidth*0.15,displayHeight*0.03,30):
            if keyCode == LEFT:
                slope = min(10,max(-10,slope-0.1))
            if keyCode == RIGHT:
                slope = min(10,max(-10,slope+0.1))
                
    if status in ["level3","level4"]:
        if isMouseOverRect(displayWidth*0.75,displayHeight*0.7,displayWidth*0.15,displayHeight*0.03,30):
            if keyCode == LEFT:
                yInt = min(10,max(-10,yInt-0.1))
            if keyCode == RIGHT:
                yInt = min(10,max(-10,yInt+0.1))
     
        if isMouseOverRect(displayWidth*0.75,displayHeight*0.8,displayWidth*0.15,displayHeight*0.03,30):
            if keyCode == LEFT:
                slope = min(10,max(-10,slope-0.1))
            if keyCode == RIGHT:
                slope = min(10,max(-10,slope+0.1))
                
    if status in ["level5","level6","level7","level8","randomgame"]:
        if isMouseOverRect(displayWidth*0.75,displayHeight*0.6,displayWidth*0.15,displayHeight*0.03,30):
            if keyCode == LEFT:
                yInt = min(10,max(-10,yInt-0.1))
            if keyCode == RIGHT:
                yInt = min(10,max(-10,yInt+0.1))
     
        if isMouseOverRect(displayWidth*0.75,displayHeight*0.7,displayWidth*0.15,displayHeight*0.03,30):
            if keyCode == LEFT:
                slope = min(10,max(-10,slope-0.1))
            if keyCode == RIGHT:
                slope = min(10,max(-10,slope+0.1))
                
        if isMouseOverRect(displayWidth*0.75,displayHeight*0.8,displayWidth*0.15,displayHeight*0.03,30):
            if keyCode == LEFT:
                quadratic = min(10,max(-10,quadratic-0.1))
            if keyCode == RIGHT:
                quadratic = min(10,max(-10,quadratic+0.1))
                
    if status == "options":
        if isMouseOverRect(displayWidth*0.5,displayHeight*0.4,displayWidth*0.15,displayHeight*0.03,30): #Master
            if keyCode == LEFT:
                volMaster = min(100,max(0,volMaster-1))
            if keyCode == RIGHT:
                volMaster = min(100,max(0,volMaster+1))
        if isMouseOverRect(displayWidth*0.5,displayHeight*0.5,displayWidth*0.15,displayHeight*0.03,30): #Music
            if keyCode == LEFT:
                volMusic = min(100,max(0,volMusic-1))
            if keyCode == RIGHT:
                volMusic = min(100,max(0,volMusic+1))
        if isMouseOverRect(displayWidth*0.5,displayHeight*0.6,displayWidth*0.15,displayHeight*0.03,30): #Effects
            if keyCode == LEFT:
                volFX = min(100,max(0,volFX-1))
            if keyCode == RIGHT:
                volFX = min(100,max(0,volFX+1))
