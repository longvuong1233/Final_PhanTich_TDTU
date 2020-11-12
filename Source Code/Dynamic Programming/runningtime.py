# Nội dung
#  Draw running time of each algorithm with different inputs size

import main
import random
import time
import pylab

# ------------------------------------------

#  Coin Row Problem


def timmerCoinRow():
    sizeInput = []
    timer = []
    for i in range(4000, 10000):
        sizeInput.append(i)
        temp = []
        for j in range(i):
            temp.append(random.randint(0, 5000))

        start = time.time()
        main.coinRow(temp)
        end = time.time()
        timer.append(end-start)

    pylab.plot(sizeInput, timer, 'o-')
    pylab.title("Coin Row")
    pylab.show()


# timmerCoinRow()

# -----------------------------------------


# Change Making Problem

def timmerchangeMaking():
    sizeInput = []
    timer = []
    for i in range(100, 500):
        sizeInput.append(i)
        temp = []
        temp.append(1)
        for j in range(2, i):
            temp.append(i)
        trade = random.randint(1, 8000)
        start = time.time()
        main.changeMaking(temp, trade)
        end = time.time()
        timer.append(end-start)

    pylab.plot(sizeInput, timer, 'o-')
    pylab.title("Change Making")
    pylab.show()


timmerchangeMaking()

# -------------------------------------

# Coin Collecting Problem


def timmerRobotCoinCollection():
    sizeInput = []
    timer = []
    for i in range(3, 200):
        sizeInput.append(i)
        temp = [[0 for i in range(i)] for j in range(i)]
        for n in range(i):
            for m in range(i):
                temp[n][m] = random.randint(0, 1)
        start = time.time()
        main.robotCoinCollection(temp)
        end = time.time()
        timer.append(end-start)

    pylab.plot(sizeInput, timer, 'o-')
    pylab.title("Robot Coin")
    pylab.show()


# timmerRobotCoinCollection()
