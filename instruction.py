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
    fill(55,float(timer-(10))/30*255)
    textSize(50)
    textAlign(LEFT)
    text("Instructions", displayWidth/6, displayHeight/6)
    textSize(30)
    i = 1
    fill(55,float(timer-(10*i))/30*255)
    text("Control sliders with your mouse\nto control parameters.\n\nUse left and right arrow\nkeys to get finer adjustments.",displayWidth*0.1, displayHeight/3+(0.24*displayHeight/(0.001*(timer-(10*i))*(timer-(10*i))*(timer-(10*i))+2) - 0.12*displayHeight)+0.12*displayHeight)
    textAlign(RIGHT)
    i = 4
    fill(55,float(timer-(10*i))/30*255)
    text("Eliminate impurities by\noverlaying the two functions.\n\nDoing so perfectly will\nunlock new levels.\n\nAfter finishing the main levels\nyou can generate a random one!", displayWidth*0.9, displayHeight/3+(0.24*displayHeight/(0.001*(timer-(10*i))*(timer-(10*i))*(timer-(10*i))+2) - 0.12*displayHeight)+0.12*displayHeight)
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
        fill(255,float(timer-(10))/30*255)
    else:
        fill(200,float(timer-(10))/30*255)
    text("Back",displayWidth/12,displayHeight/12)
    pop()
    
    if locked: #unlock mouse
        if not mousePressed:
            locked = False
            if isMouseOverRect(displayWidth/12,displayHeight/15,displayWidth/16,displayHeight/25): #check if mouse is over back button
                status = "intro"

    return (status,timer,locked)
    
