def isMouseOverRect(centerX,centerY,rectWidth,rectHeight,radius = 0):
    '''
    Checks if mouse is over a rectangle. Has (questionable) support for rounded corners!
    
    centerX (int|float): X-coordinates of the center of the rectangle.
    centerY (int|float): Y-coordinates of the center of the rectangle.
    rectWidth (int|float): Width of the rectangle in pixels.
    rectHeight (int|float): Height of the rectangle in pixels.
    radius (int|float): Radius of the the rounded corners in pixels.
    
    Return: True if mouse is over the rectangle, False otherwise.
    '''
    
    if abs(mouseX-centerX) <= rectWidth/2 and abs(mouseY-centerY) <= rectHeight/2: #Check if mouse is over general rectangular area
        if abs(abs(mouseX-centerX) - rectWidth/2) < radius and abs(abs(mouseY-centerY) - rectHeight/2) < radius and abs(abs(mouseX-centerX) - (rectWidth/2)-radius)**2 + abs(abs(mouseY-centerY) - (rectHeight/2)-radius) < radius**2: #Check if it's in the outer 4 corners and NOT in circle hitbox
            return False
        return True
    return False

def isMouseOverCircle(centerX,centerY,width):
    '''
    Checks if mouse is over a circle.
    
    centerX (int|float): X-coordinates of the center of the circle.
    centerY (int|float): Y-coordinates of the center of the circle.
    width (int|float): Width of the circle in pixels. Alternatively the diameter of the circle, or 2 times its radius.
    
    Return: True if mouse is over the circle, False otherwise.
    '''
    
    if (abs(mouseX-centerX))**2 + (abs(mouseY-centerY))**2 <= (width/2)**2: #Pythagorean theorem
        return True
    return False
