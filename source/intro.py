from detection import isMouseOverRect
from com.jogamp.opengl import GLContext, GL3
yOffset,yOffset2,yOffset3,yOffset4,spacing = 0,0,0,0,0
def intro(ENABLE_P2D, status, timer):
    '''
    Displays the intro screen.
    
    ENABLE_P2D (bool): Uses OpenGL rendering if True.
    spacing (int|float): How far apart the letters of "Harmonious" are.
    status (str): Status of the sketch.
    timer (int): How many frames have passed since the sketch started.
    yOffset (int|float): Y offset of the title text.
    yOffset2 (int|float): Y offset of the start button.
    yOffset3 (int|float): Y offset of the options button.
    yOffset4 (int|float): Y offset of the credits button.
    
    Return: spacing, status, timer, yOffset, yOffset2, yOffset3, yOffset4
    '''
    global yOffset,yOffset2,yOffset3,yOffset4,spacing
    if timer > 0:
        if timer <= 60:
            spacing = ((timer-60)*(timer-60)*(timer-60)*(timer-60)*0.00000848765+90) #Quartic function to ease spacing animation
            yOffset = 0
        else:
            spacing = 90
    if timer > 60:
        if timer <= 90:
            yOffset = 0.28*displayHeight/(0.001*(timer-60)*(timer-60)*(timer-60)+2) - 0.14*displayHeight #Rational function to ease move up title screen
        else:
            yOffset = 0.28*displayHeight/(0.001*(90-60)*(90-60)*(90-60)+2) - 0.14*displayHeight
    if timer > 90:
        if timer <= 120:
            yOffset2 = (0.24*displayHeight/(0.001*(timer-80)*(timer-80)*(timer-80)+2) - 0.12*displayHeight) #Rational function to ease move up start button
        else:
            yOffset2 = (0.24*displayHeight/(0.001*(40)*(40)*(40)+2) - 0.12*displayHeight)
    if timer > 120:
        if timer <= 150:
            yOffset3 = (0.24*displayHeight/(0.001*(timer-110)*(timer-110)*(timer-110)+2) - 0.12*displayHeight) #Rational function to ease move up options button
        else:
            yOffset3 = (0.24*displayHeight/(0.001*(40)*(40)*(40)+2) - 0.12*displayHeight)
    if timer > 150:
        if timer <= 180:
            yOffset4 = (0.24*displayHeight/(0.001*(timer-140)*(timer-140)*(timer-140)+2) - 0.12*displayHeight) #Rational function to ease move up credits button
        else:
            yOffset4 = (0.24*displayHeight/(0.001*(40)*(40)*(40)+2) - 0.12*displayHeight)

            
    push()
    noStroke()
    background(200)
    fill(55,float(timer-(0))/30*255)
    textList = [char for char in "Harmonious"]
    for i in range(len(textList)):
        text(textList[i], displayWidth/2 + (i-4.5)*spacing, displayHeight/2+yOffset)
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
    
    #Buttons
    push()
    strokeWeight(2)
    textSize(displayWidth/30)
    
    # Start button
    if(not isMouseOverRect(displayWidth/2,displayHeight/2+yOffset2+ 0.10*displayHeight, displayWidth/6, displayHeight/10, 28)):
        fill(255,float(timer-90)/30*255) #Opacity is the 2nd parameter, takes the frames between 90 and 120 and uses that
    else:
        if(mousePressed):
            timer = 0
            status = "levelselect"
        fill(180,float(timer-90)/30*255) #Opacity is the 2nd parameter, takes the frames between 90 and 120 and uses that
    stroke(0,float(timer-90)/30*255)
    rect(displayWidth/2,displayHeight/2+yOffset2+ 0.10*displayHeight, displayWidth/6, displayHeight/10, 28);
    fill(0,float(timer-90)/30*255)
    text("Start",displayWidth/2,displayHeight/1.93+yOffset2 + 0.10*displayHeight)
    
    # Options button
    if(not isMouseOverRect(displayWidth/2,displayHeight/2+yOffset3+ 0.23*displayHeight, displayWidth/6, displayHeight/10, 28)):
        fill(255,float(timer-120)/30*255) #Opacity is the 2nd parameter, takes the frames between 120 and 150 and uses that
    else:
        if(mousePressed):
            timer = 0
            status = "options"
        fill(180,float(timer-120)/30*255) #Opacity is the 2nd parameter, takes the frames between 120 and 150 and uses that
    stroke(0,float(timer-120)/30*255)
    rect(displayWidth/2,displayHeight/2+yOffset3+ 0.23*displayHeight, displayWidth/6, displayHeight/10, 28);
    fill(0,float(timer-120)/30*255)
    text("Options",displayWidth/2,displayHeight/1.93+yOffset3 + 0.23*displayHeight)
    
    # Instruction button
    if(not isMouseOverRect(displayWidth/2,displayHeight/2+yOffset4+ 0.36*displayHeight, displayWidth/6, displayHeight/10, 28)):
        fill(255,float(timer-150)/30*255) #Opacity is the 2nd parameter, takes the frames between 150 and 180 and uses that
    else:
        if(mousePressed):
            timer = 0
            status = "instruction"
        fill(180,float(timer-150)/30*255) #Opacity is the 2nd parameter, takes the frames between 150 and 180 and uses that
    stroke(0,float(timer-150)/30*255)
    rect(displayWidth/2,displayHeight/2+yOffset4+ 0.36*displayHeight, displayWidth/6, displayHeight/10, 28);
    fill(0,float(timer-150)/30*255)
    textSize(30)
    text("Instructions",displayWidth/2,displayHeight/1.93+yOffset4 + 0.35*displayHeight)
    pop()
    
    #Quit button
    push()
    if(not isMouseOverRect(displayWidth*0.94,displayHeight*0.05 + displayWidth*0.01, displayWidth*0.02, displayWidth*0.02)):
        stroke(55,float(timer-150)/30*255) #Opacity is the 2nd parameter, takes the frames between 150 and 180 and uses that
    else:
        stroke(0,float(timer-150)/30*255)
        if mousePressed:
            exit()
    strokeWeight(10)
    line(displayWidth*0.93, displayHeight*0.05,displayWidth*0.95,displayHeight*0.05+displayWidth*0.02)
    line(displayWidth*0.93, displayHeight*0.05+displayWidth*0.02,displayWidth*0.95,displayHeight*0.05)
    pop()
    
    return(status, timer)
