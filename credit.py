from detection import isMouseOverRect

def credit(status,timer): #Credit screen
    #Text
    push()
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
    
    return (status,timer)
