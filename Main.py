from graphics import *
import time
import math
import time

class Hand():

    offset = math.pi/2

    def __init__(self, length, width, color, center, angle):
        self.length = length
        self.width = width
        self.color = color
        self.center = center
        self.angle = angle

        self.centerPoint = Point(self.center, self.center)



    def setAngle(self, angle):
        self.angle = angle

    def move(self, angle):
        self.angle = self.angle + angle

    def getLine(self):

        tipPoint = Point(self.center+self.length*math.cos(self.angle+self.offset),
            self.center-self.length*math.sin(self.angle+self.offset))

        line = Line(self.centerPoint, tipPoint)
        line.setWidth(self.width)
        line.setFill(self.color)

        return line



def main():


    timme = time.localtime()

    size = 800 #Storleken på fönstret
    ctr = size/2-1 #Centrum på fönstret

    win = GraphWin("Mitt fönster", size, size) #Skapar fönster
    win.autoflush = False
    win.setBackground("black") #Sätter färgen på fönstret till svart


    i = 0


    #Generera klockan

    dis = 250
    for i in range(0, 60):
        if i%5==0:
            length = 20
        else:
            length = 15

        angle = 2*math.pi*i/60
        pt1 = Point((dis-length)*math.cos(angle)+ctr,(dis-length)*math.sin(angle)+ctr)
        pt2 = Point(dis*math.cos(angle)+ctr, dis*math.sin(angle)+ctr)
        line = Line(pt1, pt2)
        if length == 20:
            line.setWidth(4)
        else:
            line.setWidth(1)

        line.setFill("white")
        line.draw(win)

    secHand = Hand(200, 2, 'red', ctr, 0)
    minHand = Hand(200, 6, 'white', ctr, 0)
    hrHand = Hand(150, 12, 'white', ctr, 0)


    while True:

        speed = -0.01

        secHand.move(speed)
        minHand.move(speed/60)
        hrHand.move(speed/3600)

        sec = secHand.getLine()
        min = minHand.getLine()
        hr = hrHand.getLine()
        sec.draw(win)
        min.draw(win)
        hr.draw(win)

        midpoint = Circle(Point(ctr, ctr), 8)
        midpoint.setFill("white")
        midpoint.draw(win)

        win.update()
        time.sleep(0.01)

        sec.undraw()
        min.undraw()
        hr.undraw()

        midpoint.undraw()


    win.getMouse()
    win.close()


main()
