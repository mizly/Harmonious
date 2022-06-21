from detection import isMouseOverRect, isMouseOverCircle
from graph import drawGrid,linear
from com.jogamp.opengl import GLContext, GL3
def level2(ENABLE_P2D,status,timer,locked, locked2,yInt, slope, yIntLocked,slopeLocked, level): 
    '''
    Displays level 2.
    
    ENABLE_P2D (bool): Uses OpenGL rendering if True.
    status (str): Status of the sketch.
    timer (int): How many frames have passed since the sketch started.
    locked (bool): Checks if back button's mouse press is locked.
    locked2 (bool): Checks if back button's mouse press is locked.
    yInt (int|float): Y-intercept of graphs.
    slope (int|float): Slope of graphs.
    yIntLocked (bool): Check if y-int slider is locked on.
    slopeLocked (bool): Check if slope slider is locked on.
    level (int): Current highest level
    
    Return: status, timer, locked, locked2, yInt, slope, yIntLocked, slopeLocked, level
    '''
    
    #Text
    push()
    background(200)
    fill(55)
    textSize(50)
    textAlign(LEFT)
    text("Level 2", displayWidth/6, displayHeight/6)
    pop()
    
    #Sliderbars
    push()
    noStroke()
    fill(55)
    rect(displayWidth*0.75,displayHeight*0.7,displayWidth*0.15,displayHeight*0.015,30) #slope
    pop()
    
    #Slider text
    push()
    fill(55)
    textAlign(LEFT)
    textSize(50)
    text("%.1f" % slope,displayWidth*0.85,displayHeight*0.71)
    pop()
    
    #Sliderballs
    push()
    noStroke()
    
    #slope
    if isMouseOverCircle(displayWidth*0.75 + displayWidth*(0.15/20*slope),displayHeight*0.7,displayHeight*0.03): #detect if mouse is over circle
        fill(150)
        if(mousePressed) and not yIntLocked: #detect mouse press, and lock on (this is to prevent the cursor from moving "too fast" for the slider)
            slopeLocked = True
    else:
        fill(255)
    if(not mousePressed): #unlock mouse
        slopeLocked = False
    if slopeLocked: #if slider is locked on execute slider movement
        fill(150)
        slope = min(10,max(-10,(mouseX-displayWidth*0.755)/(displayWidth*0.15)*20)) #0.675 to #0.825 is from -10 to 10. Passes through a min/max filter to make sure the value is between -10 and 10
    circle(displayWidth*0.75 + displayWidth*(0.15/20*slope),displayHeight*0.7,displayHeight*0.03) #0.675 to #0.825 is from -10 to 10. The 0.15 is the percentage part in the first parameter
    pop()
    
    #Graph
    linear(yInt,slope,0,-2)
    
    #Check if correct
    if float("%.1f" % yInt) == 0 and float("%.1f" % slope) == -2:
        if level < 3:
            level = 3
            
    #Next button
    if level>2:
        push()
        textSize(50)
        if isMouseOverRect(displayWidth/12*11,displayHeight/15,displayWidth/16,displayHeight/25): #check if mouse is over next button
            if mousePressed: #lock mouse
                locked = True
            fill(0)
        else:
            fill(55)
        text("Next",displayWidth/12*11,displayHeight/12)
        pop()
        
        if locked: #unlock mouse
            if not mousePressed:
                locked = False
                if isMouseOverRect(displayWidth/12*11,displayHeight/15,displayWidth/16,displayHeight/25): #check if mouse is over next button
                    status = "level3"
                    yInt, slope = 0,0
    
    #Invert effect
    push()
    noStroke()
    fill(255)
    blendMode(DIFFERENCE)
    if ENABLE_P2D:
        GLContext.getCurrentGL().getGL3().glBlendFunc(GL3.GL_ONE_MINUS_DST_COLOR, GL3.GL_ZERO)
    rect(displayWidth/4,displayHeight/2,displayWidth/2,displayHeight)
    pop()
    
    #Render grid
    drawGrid()

    #Back button
    push()
    textSize(50)
    #rect(displayWidth/12,displayHeight/15,displayWidth/16,displayHeight/25) #hitbox for back button
    if isMouseOverRect(displayWidth/12,displayHeight/15,displayWidth/16,displayHeight/25): #check if mouse is over back button
        if mousePressed: #lock mouse
            locked2 = True
        fill(255)
    else:
        fill(200)
    text("Back",displayWidth/12,displayHeight/12)
    pop()
    
    if locked2: #unlock mouse
        if not mousePressed:
            locked2 = False
            if isMouseOverRect(displayWidth/12,displayHeight/15,displayWidth/16,displayHeight/25): #check if mouse is over back button
                status = "levelselect"
    
    return (status,timer,locked,locked2,yInt,slope,yIntLocked,slopeLocked, level)
