from detection import isMouseOverRect, isMouseOverCircle
from com.jogamp.opengl import GLContext, GL3
def options(ENABLE_P2D, status, timer, volMaster, volMusic, volFX, masterLocked, musicLocked, FXLocked, locked): #Options screen
    '''
    Displays options screen.
    
    ENABLE_P2D (bool): Uses OpenGL rendering if True.
    status (str): Status of the sketch.
    timer (int): How many frames have passed since the sketch started.
    volMaster (int|float): Master volume.
    volMusic (int|float): Music volume.
    volFX (int|float): Effects volume.
    masterLocked (bool): Checks if master slider is locked.
    musicLocked (bool): Checks if music slider is locked.
    FXLocked (bool): Checks if effects slider is locked.
    locked (bool): Checks if back button's mouse press is locked.
    
    Return: status, timer, volMaster, volMusic, volFX, masterLocked, musicLocked, FXLocked, locked
    '''
    
    #Text
    push()
    background(200)
    fill(55,float(timer-(10))/30*255)
    textSize(50)
    textAlign(LEFT)
    text("Options", displayWidth/6, displayHeight/6)
    pop()
    
    for i in range(3):
        #Sliders text
        fill(55,float(timer-(10*(i+1)))/30*255)
        push()
        textAlign(RIGHT)
        textSize(50)
        text(["Master Volume","Music Volume","Effects Volume"][i],displayWidth*0.4,displayHeight*(0.415+0.1*i)+(0.24*displayHeight/(0.001*(timer-(10*i))*(timer-(10*i))*(timer-(10*i))+2) - 0.12*displayHeight)+0.12*displayHeight)
        
        textAlign(LEFT)
        text(int([volMaster,volMusic,volFX][i]),displayWidth*0.6,displayHeight*(0.415+0.1*i)+(0.24*displayHeight/(0.001*(timer-(10*i))*(timer-(10*i))*(timer-(10*i))+2) - 0.12*displayHeight)+0.12*displayHeight)
        pop()
        
        #Sliderbars
        push()
        noStroke()
        rect(displayWidth*0.5,displayHeight*(0.4+0.1*i)+(0.24*displayHeight/(0.001*(timer-(10*i))*(timer-(10*i))*(timer-(10*i))+2) - 0.12*displayHeight)+0.12*displayHeight,displayWidth*0.15,displayHeight*0.015,30)
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
    
    #Sliderballs
    push()
    noStroke()
    
    #Master
    i = 0
    if isMouseOverCircle(displayWidth*0.425 + displayWidth*(0.15/100*volMaster), displayHeight*0.4,displayHeight*0.03): #detect if mouse is over circle
        fill(150,float(timer-(10*i))/30*255)
        if(mousePressed) and not musicLocked and not FXLocked: #detect mouse press, and lock on (this is to prevent the cursor from moving "too fast" for the slider)
            masterLocked = True
    else:
        fill(255,float(timer-(10*i))/30*255)
    if(not mousePressed): #unlock mouse
        masterLocked = False
    if masterLocked: #if slider is locked on execute slider movement
        fill(150)
        volMaster = min(100,max(0,(mouseX-displayWidth*0.425)/(displayWidth*0.15)*100)) #0.425 to #0.575 is from 0 to 100. Passes through a min/max filter to make sure the value is between 0 and 100
    circle(displayWidth*0.425 + displayWidth*(0.15/100*volMaster), displayHeight*0.4+(0.24*displayHeight/(0.001*(timer-(10*i))*(timer-(10*i))*(timer-(10*i))+2) - 0.12*displayHeight)+0.12*displayHeight,displayHeight*0.03) #0.425 to #0.575 is from 0 to 100. The 0.15 is the percentage part in the first parameter
    
    #Music
    i = 1
    if isMouseOverCircle(displayWidth*0.425 + displayWidth*(0.15/100*volMusic), displayHeight*0.5,displayHeight*0.03): #detect if mouse is over circle
        fill(150,float(timer-(10*i))/30*255)
        if(mousePressed) and not masterLocked and not FXLocked: #detect mouse press, and lock on (this is to prevent the cursor from moving "too fast" for the slider)
            musicLocked = True
    else:
        fill(255,float(timer-(10*i))/30*255)
    if(not mousePressed): #unlock mouse
        musicLocked = False
    if musicLocked: #if slider is locked on execute slider movement
        fill(150,float(timer-(10*i))/30*255)
        volMusic = min(100,max(0,(mouseX-displayWidth*0.425)/(displayWidth*0.15)*100)) #0.425 to #0.575 is from 0 to 100. Passes through a min/max filter to make sure the value is between 0 and 100
    circle(displayWidth*0.425 + displayWidth*(0.15/100*volMusic), displayHeight*0.5+(0.24*displayHeight/(0.001*(timer-(10*i))*(timer-(10*i))*(timer-(10*i))+2) - 0.12*displayHeight)+0.12*displayHeight,displayHeight*0.03) #0.425 to #0.575 is from 0 to 100. The 0.15 is the percentage part in the first parameter
    
    #Effects
    i = 2
    if isMouseOverCircle(displayWidth*0.425 + displayWidth*(0.15/100*volFX), displayHeight*0.6,displayHeight*0.03): #detect if mouse is over circle
        fill(150,float(timer-(10*i))/30*255)
        if(mousePressed) and not masterLocked and not musicLocked: #detect mouse press, and lock on (this is to prevent the cursor from moving "too fast" for the slider)
            FXLocked = True
    else:
        fill(255,float(timer-(10*i))/30*255)
    if(not mousePressed): #unlock mouse
        FXLocked = False
    if FXLocked: #if slider is locked on execute slider movement
        fill(150)
        volFX = min(100,max(0,(mouseX-displayWidth*0.425)/(displayWidth*0.15)*100)) #0.425 to #0.575 is from 0 to 100. Passes through a min/max filter to make sure the value is between 0 and 100
    circle(displayWidth*0.425 + displayWidth*(0.15/100*volFX), displayHeight*0.6+(0.24*displayHeight/(0.001*(timer-(10*i))*(timer-(10*i))*(timer-(10*i))+2) - 0.12*displayHeight)+0.12*displayHeight,displayHeight*0.03) #0.425 to #0.575 is from 0 to 100. The 0.15 is the percentage part in the first parameter
    
    pop()
    
    #Back button
    push()
    textSize(50)
    #rect(displayWidth/12,displayHeight/15,displayWidth/16,displayHeight/25) #hitbox for back button
    i = 1
    if isMouseOverRect(displayWidth/12,displayHeight/15,displayWidth/16,displayHeight/25): #check if mouse is over back button
        if mousePressed: #lock mouse
            locked = True
        fill(255,float(timer-(10*i))/30*255)
    else:
        fill(200,float(timer-(10*i))/30*255)
    text("Back",displayWidth/12,displayHeight/12)
    pop()
    
    if locked: #unlock mouse
        if not mousePressed:
            locked = False
            if isMouseOverRect(displayWidth/12,displayHeight/15,displayWidth/16,displayHeight/25): #check if mouse is over back button
                status = "intro"
    
    return (status, timer, volMaster,volMusic,volFX, masterLocked,musicLocked,FXLocked,locked)
