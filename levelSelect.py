from detection import isMouseOverRect
from com.jogamp.opengl import GLContext, GL3
shakeValue,shakeNumber,shakeTimer = 0,0,0
transitionValue,transitionTimer, transitionBool = 0,0,False
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
    quadratic (int|float): Quadratic coefficient of graphs.
    
    Return: status, timer, locked, level, yInt, slope,quadratic
    '''
    global shakeValue,shakeNumber,shakeTimer
    global transitionValue,transitionTimer,transitionBool
    
    push()
    noStroke()
    background(200)
    pushMatrix()
    
    #Down button - transition screen to random level generator
    if level>8:
        if isMouseOverRect(displayWidth*0.5, displayHeight*0.845, displayWidth*0.06,displayHeight*0.05):
            if mousePressed and not transitionBool: #check if transition can be done
                transitionBool = True
                transitionTimer = timer
            if transitionBool:
                transitionValue = transition(timer)
            fill(150,float(timer-(80))/30*255)
        else:
            fill(55,float(timer-(80))/30*255)
        translate(0,transitionValue)
        noStroke()
        beginShape(TRIANGLES) #drawing the triangle
        vertex(displayWidth*0.47, displayHeight*0.82)
        vertex(displayWidth*0.53, displayHeight*0.82)
        vertex(displayWidth*0.50, displayHeight*0.87)
        endShape()
        if timer-transitionTimer >= 30 and transitionBool:
            transitionValue,transitionTimer, transitionBool = 0,0,False
            timer = 0
            status = "random"
        
    #Text
    push()
    fill(55,float(timer-(10))/30*255)
    textSize(50)
    textAlign(LEFT)
    text("Level Select", displayWidth/6, displayHeight/6)
    pop()
    
    #Level square buttons
    push()
    noStroke()
    
    for i in range(4):
        shakeValue = (shake(i+1,timer))
        if isMouseOverRect(displayWidth*0.2+i*displayWidth*0.2,displayHeight*0.35,displayHeight*0.15,displayHeight*0.15,30): #If mouse is over button
            if(timer-(10*i)) > 0:
                fill(100)
                if(mousePressed):
                    if (i+1) > level: #check if level is available
                        if shakeNumber != i+1: #shake mechanism
                            shakeTimer = timer
                            shakeNumber = i+1
                    else:
                        status = "level%d" % (i+1)
        else:
            if (i+1) > level: #check if level is available
                fill(150,float(timer-(10*i))/30*255)
            else:
                fill(55,float(timer-(10*i))/30*255)
    
        #Each square here has their translation changed instead of their position. This is because rotation is always around the origin, and translation changes the origin.
        push()
        pushMatrix()
        translate(displayWidth*0.2+i*displayWidth*0.2,displayHeight*0.47+(0.24*displayHeight/(0.001*(timer-(10*i))*(timer-(10*i))*(timer-(10*i))+2) - 0.12*displayHeight))
        if shakeNumber == i+1:
            rotate(shakeValue)
        rect(0,0,displayHeight*0.15,displayHeight*0.15,30)
        fill(200,float(timer-(10*i))/30*255)
        text(i+1,0,0+displayHeight*0.04)
        pop()
        popMatrix()
        
    for i in range(4):
        shakeValue = (shake(i+1,timer))
        if isMouseOverRect(displayWidth*0.2+i*displayWidth*0.2,displayHeight*0.65,displayHeight*0.15,displayHeight*0.15,30): #If mouse is over button
            if (timer-(10*(i+4))) > 0:
                fill(100)
                if(mousePressed):
                    if (i+5) > level: #check if level is available
                        if shakeNumber != i+5: #shake mechanism
                            shakeTimer = timer
                            shakeNumber = i+5
                    else:
                        status = "level%d" % (i+5)
        else:
            if (i+5) > level: #check if level is available
                fill(150,float(timer-(10*(i+4)))/30*255)
            else:
                fill(55,float(timer-(10*(i+4)))/30*255)
                
        push()
        pushMatrix()
        translate(displayWidth*0.2+i*displayWidth*0.2,displayHeight*0.77+(0.24*displayHeight/(0.001*(timer-(10*(i+4)))*(timer-(10*(i+4)))*(timer-(10*(i+4)))+2) - 0.12*displayHeight))
        if shakeNumber == i+5:
            rotate(shakeValue)
        rect(0,0,displayHeight*0.15,displayHeight*0.15,30)
        fill(200,float(timer-(10*(i+4)))/30*255)
        text(i+5,0,0+displayHeight*0.04)
        pop()
        popMatrix()

    pop()
    
    #Invert effect
    push()
    noStroke()
    fill(255)
    blendMode(DIFFERENCE)
    if ENABLE_P2D:
        GLContext.getCurrentGL().getGL3().glBlendFunc(GL3.GL_ONE_MINUS_DST_COLOR, GL3.GL_ZERO)
    rect(displayWidth/4,displayHeight/2,displayWidth/2,displayHeight*4)
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
                timer = 0
    yInt, slope,quadratic = 0, 0, 0
    pop()
    popMatrix()
    rect(displayWidth/2,displayHeight*2,displayWidth,displayHeight)
    return (status,timer,locked,level,yInt,slope,quadratic)


def shake(level,timer):
    '''
    Controls shaking animation for locked levels.
    
    level (int): The level number to shake
    timer (int): frametime of the sketch
    
    Return: rotation amount
    '''
    global shakeTimer, shakeNumber
    internalTime = timer-shakeTimer
    if internalTime >= 30:
        shakeTimer = 0
        shakeNumber = 0
        return 0
    else:
        #y = -x sin x for shake animation
        x = internalTime - 30
        return (0.3*radians(-x * sin(x)))
    
def transition(timer):
    '''
    Controls translation animation into random level generator.
    
    timer (int): frametime of the sketch
    
    Return: translation amount
    '''
    global transitionTimer, transitionBool
    internalTime = timer-transitionTimer
    if internalTime >= 30:
        return 0
    else:
        t = float(internalTime)/65
        return -displayHeight*2.5*(3*(1-t)*(1-t)*t) + (3*(1-t)*t*t) + (t*t*t) #bezier cuve
