def linear(slope, yInt):
    #axis lines
    push()
    strokeWeight(5)
    stroke(255)
    line(displayWidth*0.5, displayHeight*0.15, displayWidth*0.5, displayHeight*0.85)
    line(displayWidth*0.1, displayHeight*0.5, displayWidth*0.9, displayHeight*0.5)
    pop()
    
    #label
    push()
    textSize(30)
    for i in range(-10,11): #x-axis
        if i != 0:
            text(i,displayWidth*0.5 + displayWidth*0.04*i,displayHeight*0.53)
            circle(displayWidth*0.5 + displayWidth*0.04*i,displayHeight*0.50,5)
    
    textAlign(RIGHT,CENTER)
    for i in range(-10,11): #y-axis
        if i != 0:
            text(i,displayWidth*0.495,displayHeight*0.5 + displayHeight*0.035*i)
            circle(displayWidth*0.5,displayHeight*0.5 + displayHeight*0.035*i,5)
            
    #function line
    
    pop()
