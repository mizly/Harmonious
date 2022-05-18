def isMouseOverRect(centerX,centerY,rectWidth,rectHeight,radius = 0): #Checks if mouse is over a rectangle object. Has (questionable) support for rounded corners!
    if abs(mouseX-centerX) <= rectWidth/2 and abs(mouseY-centerY) <= rectHeight/2: #Check if mouse is over general rectangular area
        if abs(abs(mouseX-centerX) - rectWidth/2) < radius and abs(abs(mouseY-centerY) - rectHeight/2) < radius and abs(abs(mouseX-centerX) - (rectWidth/2)-radius)**2 + abs(abs(mouseY-centerY) - (rectHeight/2)-radius) < radius**2: #Check if it's in the outer 4 corners and NOT in circle hitbox
            return False
        return True
    return False

def isMouseOverCircle(centerX,centerY,width):
    if (abs(mouseX-centerX))**2 + (abs(mouseY-centerY))**2 <= (width/2)**2: #Pythagorean theorem
        return True
    return False
