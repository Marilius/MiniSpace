import turtle
import math
import random
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename


class SolarSystem:
    def __init__(self, width, height):
        self.thesun = None
        self.planets = []
        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen()
        self.ssscreen.setworldcoordinates(-width, -height, width, height)
        self.ssscreen.tracer(50)

    def addPlanet(self, aplanet):
        self.planets.append(aplanet)

    def addSun(self, asun):
        self.thesun = asun

    def showPlanets(self):
        for aplanet in self.planets:
            print(aplanet)

    def freeze(self):
        self.ssscreen.exitonclick()

    def movePlanets(self):
        G = .1
        dt = .01

        for i in range(len(self.planets)):
            for j in range(i, len(self.planets)):
                if i != j:
                    rx = self.planets[j].getXPos() - self.planets[i].getXPos()
                    ry = self.planets[j].getYPos() - self.planets[i].getYPos()
                    r = math.sqrt(rx ** 2 + ry ** 2)
                    self.planets[i].ax += G * self.planets[j].getMass() * rx / r ** 3
                    self.planets[i].ay += G * self.planets[j].getMass() * ry / r ** 3

                    self.planets[j].ax -= G * self.planets[i].getMass() * rx / r ** 3
                    self.planets[j].ay -= G * self.planets[i].getMass() * ry / r ** 3

        for p in self.planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())

            rx = self.thesun.getXPos() - p.getXPos()
            ry = self.thesun.getYPos() - p.getYPos()
            r = math.sqrt(rx ** 2 + ry ** 2)

            accx = G * self.thesun.getMass() * rx / r ** 3
            accy = G * self.thesun.getMass() * ry / r ** 3

            # print(p.getName(), p.ax, p.ay, accx, accy)
            p.setXVel(p.getXVel() + dt * (accx + p.ax))
            p.ax = 0

            p.setYVel(p.getYVel() + dt * (accy + p.ay))
            p.ay = 0
            # a = self.planets[:]

            # for i in range(len(a)):
            #     for j in range(len(a)):
            #         if i != j:
            #             if ((a[i].getXPos() - a[j].getXPos()) ** 2 + (
            #                     a[i].getYPos() - a[j].getYPos()) ** 2) ** 0.5 < 0.03:
            #                 if a[i] in self.planets:
            #                     print(a[i].name)
                                # a[i].color = 'white'
                                # a[i].moveTo(a[i].x, a[i].y)
                                # accx.set_color= "white"
                                # del self.planets[self.planets.index(a[i])]
                            # if a[j] in self.planets:
                            #     a[j].color = 'white'
                               # print(a[j].name)
                               #  a[j].moveTo(a[j].x, a[j].y)
                               #  accx.set_color= "white"
                                # del self.planets[self.planets.index(a[j])]


class Sun:
    def __init__(self, iname, irad, im, itemp):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.temp = itemp
        self.x = 0
        self.y = 0

        self.sturtle = turtle.Turtle()
        self.sturtle.shape("circle")
        self.sturtle.color("yellow")

    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getTemperature(self):
        return self.temp

    def getVolume(self):
        v = 4.0 / 3 * math.pi * self.radius ** 3
        return v

    def getSurfaceArea(self):
        sa = 4.0 * math.pi * self.radius ** 2
        return sa

    def getDensity(self):
        d = self.mass / self.getVolume()
        return d

    def setName(self, newname):
        self.name = newname

    def __str__(self):
        return self.name

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y


class Planet:
    def __init__(self, iname, irad, im, idist, ivx, ivy, ic):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.distance = idist
        self.x = idist
        self.y = 0
        self.velx = ivx
        self.vely = ivy
        self.color = ic
        self.ay = 0
        self.ax = 0

        self.pturtle = turtle.Turtle()
        self.pturtle.up()
        self.pturtle.color(self.color)
        self.pturtle.shape("circle")
        self.pturtle.goto(self.x, self.y)
        self.pturtle.down()

    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getDistance(self):
        return self.distance

    def getVolume(self):
        v = 4.0 / 3 * math.pi * self.radius ** 3
        return v

    def getSurfaceArea(self):
        sa = 4.0 * math.pi * self.radius ** 2
        return sa

    def getDensity(self):
        d = self.mass / self.getVolume()
        return d

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


def read(x):
    ss = SolarSystem(2, 2)
    f = open(x, 'r').readlines()
    n = int(f[0])
    for i in range(1, n+1):
        print(f[i])
        a = f[i].strip().split(' ')
        for j in range(1, 6):
            a[j] = float(a[j])
        for j in a:
            print(j)
        m = Planet(a[0], a[1], a[2], a[3], a[4], a[5], a[6])
        m.x = float(a[7])
        m.y = float(a[8])
        ss.addPlanet(m)
    return ss


def createSSandAnimate(x):
    ss = read(x)
    sun = Sun("SUN", 5000, 12, 5800)
    sun.x = 0
    ss.addSun(sun)
    for i in range(10):
        #         def __init__(self, iname, irad, im, idist, ivx, ivy, ic):
        m = Planet(str(i), random.uniform(1, 100), random.uniform(0.001, 0.1), random.uniform(0.5, 1.9),
                   random.uniform(-1.5, 1.5), random.uniform(-0.3, -0.3), "blue")
        m.x = random.uniform(-1, -1)
        m.y = random.uniform(-1, 1)
        print(m.name, m.radius, m.mass, m.distance, m.velx, m.vely, m.color, m.x, m.y)
        ss.addPlanet(m)

    numTimePeriods = 0
    #     for amove in range(numTimePeriods):
    time.sleep(2)
    while True:
        numTimePeriods += 1
        ss.movePlanets()

        # if numTimePeriods % 50 == 0:
        #     print('smert')
        #     turtle.reset()

    ss.freeze()


#createSSandAnimate()

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
createSSandAnimate(filename)
