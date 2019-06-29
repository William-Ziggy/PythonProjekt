from graphics import *
import time
import math
import time



def main():


    timme = time.localtime()

    size = 1000 #Storleken på fönstret
    ctr = size/2-1 #Centrum på fönstret

    win = GraphWin("Mitt fönster", size, size) #Skapar fönster
    win.autoflush = False
    win.setBackground("black") #Sätter färgen på fönstret till svart


    i = 0


    #Generera klockan

    dis = 3*size/8
    disNum = dis - size/15
    for i in range(0, 60):

        angle = 2*math.pi*i/60-math.pi/2

        if i%5==0:
            length = size/40
            p = Point(disNum*math.cos(angle)+ctr, disNum*math.sin(angle)+ctr)
            if i!=0:
                number = Text(p, str(int(i/5)))
            else:
                number = Text(p, str(12))
            number.setSize(int(size/30))

            number.setFill("white")
            number.draw(win)
        else:
            length = size/50

        pt1 = Point((dis-length)*math.cos(angle)+ctr,(dis-length)*
        math.sin(angle)+ctr)
        pt2 = Point(dis*math.cos(angle)+ctr, dis*math.sin(angle)+ctr)
        line = Line(pt1, pt2)
        if length == size/40:
            line.setWidth(size/200)
        else:
            line.setWidth(size/800)

        line.setFill("white")
        line.draw(win)

    boundry = Circle(Point(ctr, ctr), dis)
    boundry.setOutline("white")
    boundry.draw(win)


    secHand = Hand(size/3, size/200, 'red', ctr, 0)
    minHand = Hand(size/3, size/100, 'white', ctr, 0)
    hrHand = Hand(size/4, size/70, 'white', ctr, 0)


    while True:

        speed = -0.5

        secHand.move(speed)
        minHand.move(speed/60)
        hrHand.move(speed/720)

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


main()
