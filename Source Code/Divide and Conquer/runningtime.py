# Nội dung
#  Draw running time of each algorithm with different inputs size

import main
import random
import time
import pylab

# ------------------------------------------

# Merge Sort


def timmerMergeSort():
    sizeInput = []
    timer = []
    for i in range(2, 101):
        sizeInput.append(i)
        temp = []
        for j in range(i):
            temp.append(random.randint(0, 100))

        start = time.time()
        main.mergeSort(temp)
        end = time.time()
        timer.append((end-start)*1000)  # đơn vị time là 10^3 s

    pylab.plot(sizeInput, timer, 'o-')
    pylab.show()


# timmerMergeSort()


# ---------------------------


# Quick Sort


def timmerQuickSort():
    sizeInput = []
    timer = []
    for i in range(2, 101):
        sizeInput.append(i)
        temp = []
        for j in range(i):
            temp.append(random.randint(0, 100))

        start = time.time()
        main.quickSort(temp, 0, len(temp)-1)
        end = time.time()
        timer.append((end-start)*1000)  # đơn vị time là 10^3 s

    pylab.plot(sizeInput, timer, 'o-')
    pylab.show()


# timmerQuickSort()


# ---------------------------


# Binary tree Traversals


def timmerHeight():
    sizeInput = []
    timer = []
    for i in range(0, 20):
        sizeInput.append(i)
        temp = main.node()
        main.initialBinaryTree(temp, i)  # Hàm này tốn rất nhiều thời gian

        start = time.time()
        main.height(temp)
        end = time.time()
        timer.append((end-start)*1000)  # đơn vị time là 10^3 s
    print(timer)
    pylab.plot(sizeInput, timer, 'o-')
    pylab.show()


timmerHeight()
