from detection import isMouseOverRect

def options(status, volMaster,volMusic,volFX): #Credit screen
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
    text("Master Volume",displayWidth*0.4,displayHeight*0.4)
    text("Music Volume",displayWidth*0.4,displayHeight*0.5)
    text("Effects Volume",displayWidth*0.4,displayHeight*0.6)
    
    textAlign(LEFT)
    text(volMaster,displayWidth*0.6,displayHeight*0.4)
    text(volMusic,displayWidth*0.6,displayHeight*0.5)
    text(volFX,displayWidth*0.6,displayHeight*0.6)
    pop()
    
    #Sliders
    push()
    noStroke()
    fill(55)
    rect(displayWidth*0.5,displayHeight*0.385,displayWidth*0.15,displayHeight*0.015,30) #Master
    rect(displayWidth*0.5,displayHeight*0.485,displayWidth*0.15,displayHeight*0.015,30) #Music
    rect(displayWidth*0.5,displayHeight*0.585,displayWidth*0.15,displayHeight*0.015,30) #Effects
    pop()
    
    #Invert effect
    push()
    fill(255)
    blendMode(DIFFERENCE)
    #GLContext.getCurrentGL().getGL3().glBlendFunc(GL3.GL_ONE_MINUS_DST_COLOR, GL3.GL_ZERO)
    rect(displayWidth/4,displayHeight/2,displayWidth/2,displayHeight)
    pop()
    
    #Back button
    push()
    textSize(50)
    #rect(displayWidth/12,displayHeight/15,displayWidth/16,displayHeight/25) #hitbox for back button
    if isMouseOverRect(displayWidth/12,displayHeight/15,displayWidth/16,displayHeight/25):
        if(mousePressed):
            status = "intro"
        fill(255)
    else:
        fill(200)
    text("Back",displayWidth/12,displayHeight/12)
    pop()
    
    return (status, volMaster,volMusic,volFX)
