from detection import isMouseOverRect
from com.jogamp.opengl import GLContext, GL3

def instruction(ENABLE_P2D,status,timer,locked):
    '''
    Displays the instruction screen.
    
    ENABLE_P2D (bool): Uses OpenGL rendering if True.
    status (str): Status of the sketch.
    timer (int): How many frames have passed since the sketch started.
    locked (bool): Checks if back button's mouse press is locked.
    
    Return: status, timer, locked
    '''
    
    #Text
    push()
    noStroke()
    background(200)
    fill(55)
    textSize(50)
    textAlign(LEFT)
    text("Credits", displayWidth/6, displayHeight/6)
    textSize(30)
    text("Game and Music: Vu Cao\nHelp with animation: Feng-Xiang Ming",displayWidth/8, displayHeight/3)
    text("Made with Processing.py", displayWidth/1.6, displayHeight/3)
    pop()
    
    #Invert effect
    push()
    noStroke()
    fill(255)
    blendMode(DIFFERENCE)
    if ENABLE_P2D:
        GLContext.getCurrentGL().getGL3().glBlendFunc(GL3.GL_ONE_MINUS_DST_COLOR, GL3.GL_ZERO)
    rect(displayWidth/4,displayHeight/2,displayWidth/2,displayHeight)
    pop()
    
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
                status = "intro"

    return (status,timer,locked)
    
