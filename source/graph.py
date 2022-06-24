def drawGrid():
    '''
    Draws the grid for a graph
    
    Return: None
    '''
    
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

def linear(yInt,slope,targetYInt,targetSlope):
    '''
    Draws 2 linear lines (target and user), converting raw values to fit the grid
    
    Return: None
    '''
    
    yInt = float("%.1f" % yInt)
    slope = float("%.1f" % slope)
    push()
    textSize(30)
    fill(55)
    text("y = %.1fx + %.1f" %(slope,yInt),displayWidth*0.75,displayHeight*0.1)
    pop()
    
    #start coords
    if (slope*-10)+yInt < -10: #check if out of range
        startPoint = ((-10-yInt)/slope,-10)
    elif (slope*-10)+yInt > 10:
        startPoint = ((10-yInt)/slope, 10)
    else:
        startPoint = (-10,(slope*-10)+yInt)
        
    if (targetSlope*-10)+targetYInt < -10: #check if out of range
        targetPoint = ((-10-targetYInt)/targetSlope,-10)
    elif (targetSlope*-10)+targetYInt > 10:
        targetPoint = ((10-targetYInt)/targetSlope, 10)
    else:
        targetPoint = (-10,(targetSlope*-10)+targetYInt)
        
    #end coords
    if (slope*10)+yInt < -10: #check if out of range
        endPoint = ((-10-yInt)/slope,-10)
    elif (slope*10)+yInt > 10:
        endPoint = ((10-yInt)/slope,10)
    else:
        endPoint = (10,(slope*10)+yInt)
        
    if (targetSlope*10)+targetYInt < -10: #check if out of range
        targetendPoint = ((-10-targetYInt)/targetSlope,-10)
    elif (targetSlope*10)+targetYInt > 10:
        targetendPoint = ((10-targetYInt)/targetSlope,10)
    else:
        targetendPoint = (10,(targetSlope*10)+targetYInt)
    
    #function line
    if(yInt != targetYInt or slope!=targetSlope):
        push()
        strokeWeight(10)
        stroke(0,255)
        line(startPoint[0]*displayWidth*0.04+displayWidth*0.5,-startPoint[1]*displayHeight*0.035+displayHeight*0.50,endPoint[0]*displayWidth*0.04+displayWidth*0.5,-endPoint[1]*displayHeight*0.035+displayHeight*0.50) #drawing the line using coords while scaling it to the screen
        stroke(255,200)
        line(targetPoint[0]*displayWidth*0.04+displayWidth*0.5,-targetPoint[1]*displayHeight*0.035+displayHeight*0.50,targetendPoint[0]*displayWidth*0.04+displayWidth*0.5,-targetendPoint[1]*displayHeight*0.035+displayHeight*0.50) #drawing the line using coords while scaling it to the screen
        pop()
        
def parabola(yInt,slope,quadratic,targetYInt,targetSlope,targetQuadratic):
    '''
    Draws 2 parabolas lines (target and user), converting raw values to fit the grid
    
    Return: None
    '''
    yInt = float("%.1f" % yInt)
    slope = float("%.1f" % slope)
    quadratic = float("%.1f" % quadratic)
    push()
    textSize(30)
    fill(55)
    text("y = %.1fx^2  + %.1fx + %.1f" %(quadratic,slope,yInt),displayWidth*0.75,displayHeight*0.1)
    pop()
    
    point1 = (-10, quadratic*100 + slope*-10 + yInt)
    point2 = (10, quadratic*100 + slope*10 + yInt)
    targetPoint1 = (-10, targetQuadratic*100 + targetSlope*-10 + targetYInt)
    targetPoint2 = (10, targetQuadratic*100 + targetSlope*10 + targetYInt)
    '''
    Control point is the intersection of the two tangents. For f(x) ax^2 + bx + c, the tangent is given by 2ax + b
    f'(-10) = -20a+b. f(-10) = 100a-10b+c. Therefore the equation of the first tangent is then (-20a+b)x + (c-100a)
    The equation of the second tangent is then (20a+b)x + (c-100a)
    The result... x = 0. I should've realized right away haha
    '''
    controlPoint = (0, yInt-(100*quadratic))
    targetControlPoint = (0, targetYInt-(100*targetQuadratic))
    
    if(yInt != targetYInt or slope!=targetSlope or quadratic!=targetQuadratic):
        push()
        noFill()
        strokeWeight(10)
        stroke(0,255)
        beginShape()
        vertex(point1[0]*displayWidth*0.04+displayWidth*0.5,-point1[1]*displayHeight*0.035+displayHeight*0.50)
        quadraticVertex(controlPoint[0]*displayWidth*0.04+displayWidth*0.5,-controlPoint[1]*displayHeight*0.035+displayHeight*0.50,point2[0]*displayWidth*0.04+displayWidth*0.5,-point2[1]*displayHeight*0.035+displayHeight*0.50)
        endShape()
        stroke(255,200)
        beginShape()
        vertex(targetPoint1[0]*displayWidth*0.04+displayWidth*0.5,-targetPoint1[1]*displayHeight*0.035+displayHeight*0.50)
        quadraticVertex(targetControlPoint[0]*displayWidth*0.04+displayWidth*0.5,-targetControlPoint[1]*displayHeight*0.035+displayHeight*0.50,targetPoint2[0]*displayWidth*0.04+displayWidth*0.5,-targetPoint2[1]*displayHeight*0.035+displayHeight*0.50)
        endShape()
        pop()
