/**
 * Bezier. 
 * 
 * The first two parameters for the bezier() function specify the 
 * first point in the curve and the last two parameters specify 
 * the last point. The middle parameters set the control points
 * that define the shape of the curve. 
 */

void setup() {
  size(displayWidth,displayHeight); 
  stroke(255);
  strokeWeight(5);
  textAlign(CENTER);
}

void draw() {
  // Drawing the grid 
  line(displayWidth/2,0,displayWidth/2,displayHeight);
  line(0,displayHeight/2,displayWidth,displayHeight/2);
  
  fill(0,0,0);
  for (int a = 0; a < 40; a += 1) {
    text(a-20,displayWidth/40*a,displayHeight/2);
    text((a-20)*-1, displayWidth/2, displayHeight/40*a);
  }
  
  text("Plotting y = x^2", displayWidth/1.5, displayHeight/10);
  
  //Plotting
  int startCoordsX;
  int startCoordsY;
  int endCoordsX;
  int endCoordsY;
  startCoordsX = -4;
  startCoordsY = 16;
  endCoordsX = 4;
  endCoordsY = 16;
  
  noFill();
  /*
  beginShape();
  vertex((startCoordsX+20)*displayWidth/40,(startCoordsY*-1+20)*displayHeight/40);
  vertex((0+20)*displayWidth/40,(0+20)*displayHeight/40);
  vertex((endCoordsX+20)*displayWidth/40,(endCoordsY*-1+20)*displayHeight/40);
  endShape();
  */
  
  beginShape();
  vertex((startCoordsX+20)*displayWidth/40,(startCoordsY*-1+20)*displayHeight/40);
  quadraticVertex((0+20)*displayWidth/40,(16+20)*displayHeight/40,(endCoordsX+20)*displayWidth/40,(endCoordsY*-1+20)*displayHeight/40);
  endShape();
}
