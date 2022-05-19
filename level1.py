from detection import isMouseOverRect
from graph import linear
from com.jogamp.opengl import GLContext, GL3
def level1(ENABLE_P2D,status,timer,locked, yInt, slope): 
    '''
    Displays level 1.
    
    ENABLE_P2D (bool): Uses OpenGL rendering if True.
    status (str): Status of the sketch.
    timer (int): How many frames have passed since the sketch started.
    locked (bool): Checks if back button's mouse press is locked.
    yInt (int|float): Y-intercept of graphs.
    slope (int|float): Slope of graphs.
    
    Return: status, timer, locked, yInt, slope
    '''
    
    #Text
    push()
    background(200)
    fill(55)
    textSize(50)
    textAlign(LEFT)
    text("Level 1", displayWidth/6, displayHeight/6)
    pop()
    
    #Sliderbars
    push()
    noStroke()
    fill(55)
    rect(displayWidth*0.75,displayHeight*0.7,displayWidth*0.15,displayHeight*0.015,30) #slope
    rect(displayWidth*0.75,displayHeight*0.8,displayWidth*0.15,displayHeight*0.015,30) #y-int
    pop()
    
    #Sliderballs
    
    #Invert effect
    push()
    fill(255)
    blendMode(DIFFERENCE)
    if ENABLE_P2D:
        GLContext.getCurrentGL().getGL3().glBlendFunc(GL3.GL_ONE_MINUS_DST_COLOR, GL3.GL_ZERO)
    rect(displayWidth/4,displayHeight/2,displayWidth/2,displayHeight)
    pop()
    
    #Graph
    linear(5,5)
    
    #Back button
    push()
    textSize(50)
    #rect(displayWidth/12,displayHeight/15,displayWidth/16,displayHeight/25) #hitbox for back button
    if isMouseOverRect(displayWidth/12,displayHeight/15,displayWidth/16,displayHeight/25): #check if mouse is over back button
        if mousePressed: #lock mouse
            locked = True
        fill(255)
    else:
        fill(200)
    text("Back",displayWidth/12,displayHeight/12)
    pop()
    
    if locked: #unlock mouse
        if not mousePressed:
            locked = False
            if isMouseOverRect(displayWidth/12,displayHeight/15,displayWidth/16,displayHeight/25): #check if mouse is over back button
                status = "levelselect"
    
    return (status,timer,locked,yInt,slope)
