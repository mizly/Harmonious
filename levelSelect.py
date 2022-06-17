from detection import isMouseOverRect
from com.jogamp.opengl import GLContext, GL3
shakeValue,shakeNumber,shakeTimer = 0,0,0
def levelSelect(ENABLE_P2D,status,timer,locked,level,yInt,slope,quadratic):
    '''
    Displays level selection screen.
    
    ENABLE_P2D (bool): Uses OpenGL rendering if True.
    status (str): Status of the sketch.
    timer (int): How many frames have passed since the sketch started.
    locked (bool): Checks if back button's mouse press is locked.
    level (int): The highest level that is available.
    yInt (int|float): Y-intercept of graphs.
    slope (int|float): Slope of graphs.
    
    Return: status, timer, locked, level, yInt, slope,quadratic
    '''
    global shakeValue,shakeNumber,shakeTimer
    #Text
    push()
    background(200)
    fill(55)
    textSize(50)
    textAlign(LEFT)
    text("Level Select", displayWidth/6, displayHeight/6)
    pop()
    
    #Level square buttons
    push()
    noStroke()
    
    for i in range(4):
        if isMouseOverRect(displayWidth*0.2+i*displayWidth*0.2,displayHeight*0.35,displayHeight*0.15,displayHeight*0.15,30): #If mouse is over button
            if(timer-(10*i)) > 0:
                fill(100)
                if(mousePressed):
                    if (i+1) > level: #check if level is available
                        print("level locked")
                        if shakeNumber != i+1:
                            shake(i+1)
                    else:
                        status = "level%d" % (i+1)
        else:
            if (i+1) > level: #check if level is available
                fill(150,float(timer-(10*i))/30*255)
            else:
                fill(55,float(timer-(10*i))/30*255)
        rect(displayWidth*0.2+i*displayWidth*0.2,displayHeight*0.47+(0.24*displayHeight/(0.001*(timer-(10*i))*(timer-(10*i))*(timer-(10*i))+2) - 0.12*displayHeight),displayHeight*0.15,displayHeight*0.15,30)
        fill(200)
        text(i+1,displayWidth*0.2+i*displayWidth*0.2,displayHeight*0.51+(0.24*displayHeight/(0.001*(timer-(10*i))*(timer-(10*i))*(timer-(10*i))+2) - 0.12*displayHeight))

        if isMouseOverRect(displayWidth*0.2+i*displayWidth*0.2,displayHeight*0.65,displayHeight*0.15,displayHeight*0.15,30): #If mouse is over button
            if (timer-(10*(i+4))) > 0:
                fill(100)
                if(mousePressed):
                    if (i+5) > level: #check if level is available
                        print("level locked")
                    else:
                        status = "level%d" % (i+5)
        else:
            if (i+5) > level: #check if level is available
                fill(150,float(timer-(10*(i+4)))/30*255)
            else:
                fill(55,float(timer-(10*(i+4)))/30*255)
        rect(displayWidth*0.2+i*displayWidth*0.2,displayHeight*0.77+(0.24*displayHeight/(0.001*(timer-(10*(i+4)))*(timer-(10*(i+4)))*(timer-(10*(i+4)))+2) - 0.12*displayHeight),displayHeight*0.15,displayHeight*0.15,30)
        fill(200)
        text(i+5,displayWidth*0.2+i*displayWidth*0.2,displayHeight*0.81+(0.24*displayHeight/(0.001*(timer-(10*(i+4)))*(timer-(10*(i+4)))*(timer-(10*(i+4)))+2) - 0.12*displayHeight))

    pop()
    
    #Invert effect
    push()
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
    yInt, slope,quadratic = 0, 0, 0
    return (status,timer,locked,level,yInt,slope,quadratic)

def shake(level):
    pass
