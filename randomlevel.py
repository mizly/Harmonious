from detection import isMouseOverRect
from com.jogamp.opengl import GLContext, GL3
import random
transitionValue,transitionTimer, transitionBool = 0,0,False
checkboxes = [True,True,True]
def randomlevel(ENABLE_P2D,status,timer,locked,yIntValue,slopeValue,quadraticValue):
    '''
    Displays the credit screen.
    
    ENABLE_P2D (bool): Uses OpenGL rendering if True.
    status (str): Status of the sketch.
    timer (int): How many frames have passed since the sketch started.
    locked (bool): Checks if back button's mouse press is locked.
    yIntValue (float): Y-Int value being passed from random level generator.
    slopeValue (float): Slope value being passed from random level generator.
    quadraticValue (float): Quadratic value being passed from random level generator.
    
    Return: status, timer, locked, yIntValue, slopeValue, quadraticValue
    '''
    global transitionValue,transitionTimer,transitionBool
    push()
    background(200)
    #Down button - transition screen to random level generator
    if isMouseOverRect(displayWidth*0.5, displayHeight*0.155, displayWidth*0.06,displayHeight*0.05):
        if mousePressed and not transitionBool: #check if transition can be done
            transitionBool = True
            transitionTimer = timer
        if transitionBool:
            transitionValue = transition(timer)
        fill(150,float(timer-(-10))/30*255)
    else:
        fill(55,float(timer-(-10))/30*255)
    translate(0,transitionValue)
    noStroke()
    beginShape(TRIANGLES) #drawing the triangle
    i = -1
    vertex(displayWidth*0.47, displayHeight*0.18+(0.24*displayHeight/(0.001*(timer-(10*i))*(timer-(10*i))*(timer-(10*i))+2) - 0.12*displayHeight)+0.12*displayHeight)
    vertex(displayWidth*0.53, displayHeight*0.18+(0.24*displayHeight/(0.001*(timer-(10*i))*(timer-(10*i))*(timer-(10*i))+2) - 0.12*displayHeight)+0.12*displayHeight)
    vertex(displayWidth*0.50, displayHeight*0.13+(0.24*displayHeight/(0.001*(timer-(10*i))*(timer-(10*i))*(timer-(10*i))+2) - 0.12*displayHeight)+0.12*displayHeight)
    endShape()
    if timer-transitionTimer >= 25 and transitionBool:
        transitionValue,transitionTimer, transitionBool = 0,0,False
        timer = 0
        status = "levelselect"
    
    #Text
    push()
    fill(55,float(timer-(0))/30*255)
    textSize(50)
    textAlign(CENTER)
    i = 0
    text("Random Level Generator", displayWidth/2, displayHeight*0.37+(0.24*displayHeight/(0.001*(timer-(10*i))*(timer-(10*i))*(timer-(10*i))+2) - 0.12*displayHeight))
    pop()
    
    #Text and checkboxes
    push()
    for i in range(3):
        textboxes = ["Y Intercept","Slope","Quadratic"]
        if checkboxes[i]:
            fill(100,float(timer-(10*(i+2)))/30*255)
        else:
            noFill()
        if isMouseOverRect(displayWidth*0.55,displayHeight*(0.4+i*0.1)+(0.24*displayHeight/(0.001*(timer-(10*(i+2)))*(timer-(10*(i+2)))*(timer-(10*(i+2)))+2) - 0.12*displayHeight)+0.12*displayHeight,displayHeight*0.07,displayHeight*0.07):
            if mousePressed: #lock mouse
                locked = True
            fill(150,float(timer-(10*(i+2)))/30*255)
        stroke(55,float(timer-(10*(i+2)))/30*255)
        rect(displayWidth*0.55,displayHeight*(0.4+i*0.1)+(0.24*displayHeight/(0.001*(timer-(10*(i+2)))*(timer-(10*(i+2)))*(timer-(10*(i+2)))+2) - 0.12*displayHeight)+0.12*displayHeight,displayHeight*0.07,displayHeight*0.07)
        textSize(50)
        textAlign(RIGHT)
        fill(55,float(timer-(10*(i+2)))/30*255)
        text(textboxes[i], displayWidth*0.45,displayHeight*(0.415+0.1*i)+(0.24*displayHeight/(0.001*(timer-(10*(i+2)))*(timer-(10*(i+2)))*(timer-(10*(i+2)))+2) - 0.12*displayHeight)+0.12*displayHeight)
        
    if locked: #unlock mouse
        if not mousePressed:
            locked = False
            for i in range(3):
                if isMouseOverRect(displayWidth*0.55,displayHeight*(0.4+i*0.1),displayHeight*0.07,displayHeight*0.07): #check if mouse is over checkboxes
                    checkboxes[i] = not (checkboxes[i])
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

    #Generate button
    push()
    i=2
    textSize(40)
    textAlign(CENTER)
    if(not isMouseOverRect(displayWidth/2,displayHeight/2+ 0.285*displayHeight, displayWidth/6, displayHeight/10, 28)):
        fill(255,float(timer-(10*(i+2)))/30*255)
    else:
        if(mousePressed): #generating random values
            if checkboxes[0]:
                yIntValue = float("%.1f" % random.randrange(-100,100))*0.1
            else:
                yIntValue = 0
                
            if checkboxes[1]:
                slopeValue = float("%.1f" % random.randrange(-100,100))*0.1
            else:
                slopeValue = 0
                
            if checkboxes[2]:
                quadraticValue = float("%.1f" % random.randrange(-100,100))*0.1
            else:
                quadraticValue = 0
            
            status = "randomgame"
        fill(180,float(timer-(10*(i+2)))/30*255)
    stroke(0,float(timer-(10*(i+2)))/30*255)
    rect(displayWidth/2,displayHeight/2+0.285*displayHeight+(0.24*displayHeight/(0.001*(timer-(10*(i+2)))*(timer-(10*(i+2)))*(timer-(10*(i+2)))+2) - 0.12*displayHeight)+0.12*displayHeight, displayWidth/6, displayHeight/10, 28);
    fill(55,float(timer-(10*(i+2)))/30*255)
    text("Generate!", displayWidth*0.5,displayHeight*0.8+(0.24*displayHeight/(0.001*(timer-(10*(i+2)))*(timer-(10*(i+2)))*(timer-(10*(i+2)))+2) - 0.12*displayHeight)+0.12*displayHeight)
    pop()
    pop()
    return (status,timer,locked,yIntValue,slopeValue,quadraticValue)
    
def transition(timer):
    '''
    Controls translation animation into level select screen.
    
    timer (int): frametime of the sketch
    
    Return: translation amount
    '''
    global transitionTimer, transitionBool
    internalTime = timer-transitionTimer
    if internalTime >= 30:
        return 0
    else:
        t = float(internalTime)/65
        return displayHeight*2.5*(3*(1-t)*(1-t)*t) + (3*(1-t)*t*t) + (t*t*t) #bezier curve
