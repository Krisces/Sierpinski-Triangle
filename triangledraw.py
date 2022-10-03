from ezgraphics import GraphicsWindow
import random

def main():
    numSides = 3
    MAXWIN = 600

    while True:
        points = []
        userBackground = input("What background color would you like? ")
        userColor = input("What color do you want for the triangle? ")
        numPoints = int(input("How many points (between 4000 and 10000)? "))
                        
        for i in range(numSides):
            points.append([random.randint(1,MAXWIN),
                           random.randint(1,MAXWIN)])
            
        #set up graphics window
        win = GraphicsWindow(MAXWIN,MAXWIN)
        win.setTitle("Sierpinski Triangle")
        canvas = win.canvas()
        canvas.setBackground(userBackground)
        canvas.setColor(userColor)
        
        #draw vertices 
        for point in points:
            canvas.drawOval(point[0],point[1], 3, 3)
        
        
        #set first point to a vertex
        nextPoint = points[0]
        
        win.pause(100)
        
        canvas.setColor(userColor)
        
        for i in range(numPoints):
                            
            pointNdx = random.randint(0,numSides-1)
            nextPoint = findMid(nextPoint,points[pointNdx])
            canvas.drawOval(nextPoint[0],nextPoint[1], 2, 2)
        
        canvas.drawText(5,5,"Close this window to start over")
        win.wait()
        win.close()




def findMid(point1, point2):
    midx = (point1[0] + point2[0])/2
    midy = (point1[1] + point2[1])/2
    return midx,midy

main()
