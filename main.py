import turtle
import math
import random
import time


class SolarSystem:
    def __init__(self, width, height):
        self.planets = []
        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen()
        self.ssscreen.setworldcoordinates(-2*width, -2*height, 2*width, 2*height)
        self.ssscreen.tracer(50)

    def addPlanet(self, aplanet):
        self.planets.append(aplanet)

    def showPlanets(self):
        for aplanet in self.planets:
            print(aplanet)

    def freeze(self):
        self.ssscreen.exitonclick()

    def movePlanets(self):
        G = .1
        dt = .001

        for i in range(len(self.planets)):
            for j in range(i, len(self.planets)):
                if i != j:
                    rx = self.planets[j].getXPos() - self.planets[i].getXPos()
                    ry = self.planets[j].getYPos() - self.planets[i].getYPos()
                    r = math.sqrt(rx**2 + ry**2)
                    self.planets[i].ax += G * self.planets[j].getMass()*rx/r**3
                    self.planets[i].ay += G * self.planets[j].getMass()*ry/r**3

                    self.planets[j].ax -= G * self.planets[i].getMass()*rx/r**3
                    self.planets[j].ay -= G * self.planets[i].getMass()*ry/r**3

        for p in self.planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())

            # print(p.getName(), p.ax, p.ay)
            p.setXVel(p.getXVel() + dt * p.ax)
            p.ax = 0

            p.setYVel(p.getYVel() + dt * p.ay)
            p.ay = 0
            # a = self.planets[:]

            # for i in range(len(a)):
            #     for j in range(len(a)):
            #         if i != j:
            #             if ((a[i].getXPos() - a[j].getXPos())**2 + (a[i].getYPos() - a[j].getYPos())**2) ** 0.5 < 0.03:
            #                 if a[i] in self.planets:
            #                     print(a[i].name)
            #                     del self.planets[self.planets.index(a[i])]
            #                 if a[j] in self.planets:
            #                     print(a[j].name)
            #                     del self.planets[self.planets.index(a[j])]


class Planet:
    def __init__(self, iname, im, ivx, ivy, ix, iy, ic):
        self.name = iname
        self.mass = im
        self.y = 0
        self.velx = ivx
        self.vely = ivy
        self.color = ic
        self.ay = 0
        self.ax = 0
        self.x = ix
        self.y = iy

        self.pturtle = turtle.Turtle()
        self.pturtle.up()
        self.pturtle.color(self.color)
        self.pturtle.shape("circle")
        self.pturtle.goto(self.x, self.y)
        self.pturtle.down()

    def getName(self):
        return self.name

    def getMass(self):
        return self.mass

    def setName(self, newname):
        self.name = newname

    def show(self):
        print(self.name)

    def __str__(self):
        return self.name

    def moveTo(self, newx, newy):
        self.x = newx
        self.y = newy
        self.pturtle.goto(newx, newy)

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

    def getXVel(self):
        return self.velx

    def getYVel(self):
        return self.vely

    def setXVel(self, newvx):
        self.velx = newvx

    def setYVel(self, newvy):
        self.vely = newvy

def createSSandAnimate():
    print(4)
    ss = SolarSystem(2, 2)
    m = Planet("SUN", 20, 0, 0, 0, 0, 'yellow')
    ss.addPlanet(m)
    print("SUN", 20, 0, 0, 0, 0, 0, 'yellow')
    for i in range(8):

        #         def __init__(self, iname, im, ivx, ivy, ix, iy, ic):

        m = Planet(str(i),  random.uniform(0.01, 0.1),
                   random.uniform(-1.5, 1.5), random.uniform(-1, 1),
                   random.uniform(-0.5, 0.5)*5, random.uniform(-1, 1), "blue")
        ss.addPlanet(m)

    m = Planet("SUN", 12, 0, 0, 3, 3, 'yellow')
    ss.addPlanet(m)

    numTimePeriods = 0
#     for amove in range(numTimePeriods):
    time.sleep(2)
    while True:
        numTimePeriods += 1
        ss.movePlanets()

        # if numTimePeriods % 50 == 0:
            # print('smert')
            # ss.reset()
        # ss.freeze()

createSSandAnimate()
