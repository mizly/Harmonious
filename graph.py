def linear(yInt,slope,targetYInt,targetSlope):
    yInt = float("%.1f" % yInt)
    slope = float("%.1f" % slope)
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
            text(i,displayWidth*0.495,displayHeight*0.5 + displayHeight*0.035*-i)
            circle(displayWidth*0.5,displayHeight*0.5 + displayHeight*0.035*i,5)  
    pop()
    
    #start coords
    if (slope*-10)+yInt < -10: #check if out of range
        startPoint = ((-10-yInt)/slope,-10)
    elif (slope*-10)+yInt > 10:
        startPoint = ((10-yInt)/slope, 10)
    else:
        startPoint = (-10,(slope*-10)+yInt)
        
    #end coords
    if (slope*10)+yInt < -10: #check if out of range
        endPoint = ((-10-yInt)/slope,-10)
    elif (slope*10)+yInt > 10:
        endPoint = ((10-yInt)/slope,10)
    else:
        endPoint = (10,(slope*10)+yInt)
    
    #function line
    push()
    strokeWeight(10)
    stroke(0,200)
    line(startPoint[0]*displayWidth*0.04+displayWidth*0.5,-startPoint[1]*displayHeight*0.035+displayHeight*0.50,endPoint[0]*displayWidth*0.04+displayWidth*0.5,-endPoint[1]*displayHeight*0.035+displayHeight*0.50) #drawing the line using coords while scaling it to the screen
    pop()
