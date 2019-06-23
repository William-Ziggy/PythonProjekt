from graphics import *
import time
import math
import time

def main():


    timme = time.localtime()

    size = 800 #Storleken på fönstret
    center = size/2-1 #Centrum på fönstret

    win = GraphWin("Mitt fönster", size, size) #Skapar fönster
    win.autoflush = False
    win.setBackground("black") #Sätter färgen på fönstret till svart


    centerPoint = Point(center, center)

    i = 0
    offset = math.pi/2



    #Generera klockan

    dis = 250
    for i in range(0, 60):
        if i%5==0:
            length = 20
        else:
            length = 15

        angle = 2*math.pi*i/60
        pt1 = Point((dis-length)*math.cos(angle)+center,(dis-length)*math.sin(angle)+center)
        pt2 = Point(dis*math.cos(angle)+center, dis*math.sin(angle)+center)
        line = Line(pt1, pt2)
        if length == 20:
            line.setWidth(4)
        else:
            line.setWidth(1)

        line.setFill("white")
        line.draw(win)


    while True:

        j = i/12
        k = j/12

        secAngle= i*math.pi
        secLength = 200

        secTop = Point(center+secLength*math.cos(secAngle+offset),
            center-secLength*math.sin(secAngle+offset))
        secVisare = Line(centerPoint, secTop)

        secVisare.setWidth(2)
        secVisare.setFill("red")
        secVisare.draw(win)


        minAngle= j*math.pi
        minLength = 200

        minTop = Point(center+minLength*math.cos(minAngle+offset),
            center-minLength*math.sin(minAngle+offset))
        minVisare = Line(centerPoint, minTop)

        minVisare.setWidth(8)
        minVisare.setFill("white")
        minVisare.draw(win)

        timAngle= k*math.pi
        timLength = 150

        timTop = Point(center+timLength*math.cos(timAngle+offset),
            center-timLength*math.sin(timAngle+offset))
        timVisare = Line(centerPoint, timTop)

        timVisare.setWidth(12)
        timVisare.setFill("white")
        timVisare.draw(win)

        midpoint = Circle(centerPoint, 8)
        midpoint.setFill("white")
        midpoint.draw(win)

        i-=0.01

        win.update()
        time.sleep(0.01)

        secVisare.undraw()
        minVisare.undraw()
        timVisare.undraw()

        midpoint.undraw()


    win.getMouse() # Pause to view result
    win.close()


main()
