# Nội dung
#  Draw running time of each algorithm with different inputs size

import main
import random
import time
import pylab
# ------------------------------------------

# Selection sort


def timmerSelectSort():
    sizeInput = []
    timer = []
    for i in range(2, 101):
        sizeInput.append(i)
        temp = []
        for j in range(i):
            temp.append(random.randint(0, 100))
        start = time.time()
        main.selectionSort(temp)
        end = time.time()
        timer.append((end-start)*1000)  # đơn vị time là 10^3 s

    pylab.plot(sizeInput, timer, 'o-')
    pylab.show()


timmerSelectSort()


# ---------------------------


# bubble sort

def timmerBubbleSort():
    sizeInput = []
    timer = []
    for i in range(2, 101):
        sizeInput.append(i)
        temp = []
        for j in range(i):
            temp.append(random.randint(0, 100))
        start = time.time()
        main.bubbleSort(temp)
        end = time.time()
        timer.append((end-start)*1000)  # đơn vị time là 10^3 s

    pylab.plot(sizeInput, timer, 'o-')
    pylab.show()


# timmerBubbleSort()


# --------------------------

# sequential search

def timmerSequentialSearch():
    sizeInput = []
    timer = []
    for i in range(2, 101):
        sizeInput.append(i)
        temp = []
        for j in range(i):
            temp.append(random.randint(0, 100))
        k = random.randint(0, 100)
        start = time.time()
        print(main.sequentialSearch(temp, k))
        end = time.time()
        timer.append((end-start)*1000)  # đơn vị time là 10^3 s

    pylab.plot(sizeInput, timer, 'o-')
    pylab.show()


# timmerSequentialSearch()
