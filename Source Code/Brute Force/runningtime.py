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
    for i in range(2, 2000):
        sizeInput.append(i)
        temp = []
        for j in range(i):
            temp.append(random.randint(0, 100))
        start = time.time()
        main.selectionSort(temp)
        end = time.time()
        timer.append((end-start))  # đơn vị time là 10^3 s

    pylab.plot(sizeInput, timer, 'o-')
    pylab.title("Select Sort")
    pylab.show()


# timmerSelectSort()


# ---------------------------


# bubble sort

def timmerBubbleSort():
    sizeInput = []
    timer = []
    for i in range(2, 2000):
        sizeInput.append(i)
        temp = []
        for j in range(i):
            temp.append(random.randint(0, 100))
        start = time.time()
        main.bubbleSort(temp)  # call bubble sort function above
        end = time.time()
        timer.append((end-start))  # đơn vị time là 10^3 s

    pylab.plot(sizeInput, timer, 'o-')
    pylab.title("Bubble Sort")
    pylab.show()


# timmerBubbleSort()


# --------------------------

# sequential search

def timmerSequentialSearch():
    sizeInput = []
    timer = []
    for i in range(1000, 2000):
        sizeInput.append(i)
        temp = []
        for j in range(i):
            temp.append(random.randint(0, 3000))
        k = random.randint(0, 4000)
        start = time.time()
        main.sequentialSearch(temp, k)  # call sequential search above
        end = time.time()
        timer.append(end-start)  # đơn vị time là 10^3 s

    pylab.plot(sizeInput, timer, 'o-')
    pylab.title("Sequential Search")
    pylab.show()


timmerSequentialSearch()
