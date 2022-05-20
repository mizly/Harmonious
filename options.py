from detection import isMouseOverRect, isMouseOverCircle
from com.jogamp.opengl import GLContext, GL3
def options(ENABLE_P2D, status, volMaster, volMusic, volFX, masterLocked, musicLocked, FXLocked, locked): #Options screen
    '''
    Displays options screen.
    
    ENABLE_P2D (bool): Uses OpenGL rendering if True.
    status (str): Status of the sketch.
    volMaster (int|float): Master volume.
    volMusic (int|float): Music volume.
    volFX (int|float): Effects volume.
    masterLocked (bool): Checks if master slider is locked.
    musicLocked (bool): Checks if music slider is locked.
    FXLocked (bool): Checks if effects slider is locked.
    locked (bool): Checks if back button's mouse press is locked.
    
    Return: status, volMaster, volMusic, volFX, masterLocked, musicLocked, FXLocked, locked
    '''
    
    #Text
    push()
    background(200)
    fill(55)
    textSize(50)
    textAlign(LEFT)
    text("Options", displayWidth/6, displayHeight/6)
    pop()
    
    #Sliders text
    push()
    textAlign(RIGHT)
    textSize(50)
    fill(55)
    text("Master Volume",displayWidth*0.4,displayHeight*0.415)
    text("Music Volume",displayWidth*0.4,displayHeight*0.515)
    text("Effects Volume",displayWidth*0.4,displayHeight*0.615)
    
    textAlign(LEFT)
    text(int(volMaster),displayWidth*0.6,displayHeight*0.4)
    text(int(volMusic),displayWidth*0.6,displayHeight*0.5)
    text(int(volFX),displayWidth*0.6,displayHeight*0.6)
    pop()
    
    #Sliderbars
    push()
    noStroke()
    fill(55)
    rect(displayWidth*0.5,displayHeight*0.4,displayWidth*0.15,displayHeight*0.015,30) #Master
    rect(displayWidth*0.5,displayHeight*0.5,displayWidth*0.15,displayHeight*0.015,30) #Music
    rect(displayWidth*0.5,displayHeight*0.6,displayWidth*0.15,displayHeight*0.015,30) #Effects
    pop()
    
    #Invert effect
    push()
    fill(255)
    blendMode(DIFFERENCE)
    if ENABLE_P2D:
        GLContext.getCurrentGL().getGL3().glBlendFunc(GL3.GL_ONE_MINUS_DST_COLOR, GL3.GL_ZERO)
    rect(displayWidth/4,displayHeight/2,displayWidth/2,displayHeight)
    pop()
    
    #Sliderballs
    push()
    noStroke()
    
    #Master
    if isMouseOverCircle(displayWidth*0.425 + displayWidth*(0.15/100*volMaster), displayHeight*0.4,displayHeight*0.03): #detect if mouse is over circle
        fill(150)
        if(mousePressed) and not musicLocked and not FXLocked: #detect mouse press, and lock on (this is to prevent the cursor from moving "too fast" for the slider)
            masterLocked = True
    else:
        fill(255)
    if(not mousePressed): #unlock mouse
        masterLocked = False
    if masterLocked: #if slider is locked on execute slider movement
        fill(150)
        volMaster = min(100,max(0,(mouseX-displayWidth*0.425)/(displayWidth*0.15)*100)) #0.425 to #0.575 is from 0 to 100. Passes through a min/max filter to make sure the value is between 0 and 100
    circle(displayWidth*0.425 + displayWidth*(0.15/100*volMaster), displayHeight*0.4,displayHeight*0.03) #0.425 to #0.575 is from 0 to 100. The 0.15 is the percentage part in the first parameter
    
    #Music
    if isMouseOverCircle(displayWidth*0.425 + displayWidth*(0.15/100*volMusic), displayHeight*0.5,displayHeight*0.03): #detect if mouse is over circle
        fill(150)
        if(mousePressed) and not masterLocked and not FXLocked: #detect mouse press, and lock on (this is to prevent the cursor from moving "too fast" for the slider)
            musicLocked = True
    else:
        fill(255)
    if(not mousePressed): #unlock mouse
        musicLocked = False
    if musicLocked: #if slider is locked on execute slider movement
        fill(150)
        volMusic = min(100,max(0,(mouseX-displayWidth*0.425)/(displayWidth*0.15)*100)) #0.425 to #0.575 is from 0 to 100. Passes through a min/max filter to make sure the value is between 0 and 100
    circle(displayWidth*0.425 + displayWidth*(0.15/100*volMusic), displayHeight*0.5,displayHeight*0.03) #0.425 to #0.575 is from 0 to 100. The 0.15 is the percentage part in the first parameter
    
    #Effects
    if isMouseOverCircle(displayWidth*0.425 + displayWidth*(0.15/100*volFX), displayHeight*0.6,displayHeight*0.03): #detect if mouse is over circle
        fill(150)
        if(mousePressed) and not masterLocked and not musicLocked: #detect mouse press, and lock on (this is to prevent the cursor from moving "too fast" for the slider)
            FXLocked = True
    else:
        fill(255)
    if(not mousePressed): #unlock mouse
        FXLocked = False
    if FXLocked: #if slider is locked on execute slider movement
        fill(150)
        volFX = min(100,max(0,(mouseX-displayWidth*0.425)/(displayWidth*0.15)*100)) #0.425 to #0.575 is from 0 to 100. Passes through a min/max filter to make sure the value is between 0 and 100
    circle(displayWidth*0.425 + displayWidth*(0.15/100*volFX), displayHeight*0.6,displayHeight*0.03) #0.425 to #0.575 is from 0 to 100. The 0.15 is the percentage part in the first parameter
    
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
    
    return (status, volMaster,volMusic,volFX, masterLocked,musicLocked,FXLocked,locked)
