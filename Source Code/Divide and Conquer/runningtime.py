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
    for i in range(2, 2000):
        sizeInput.append(i)
        temp = []
        for j in range(i):
            temp.append(random.randint(0, 2000))

        start = time.time()
        main.mergeSort(temp)  # Call Merge Sort def above
        end = time.time()
        timer.append(end-start)

    pylab.plot(sizeInput, timer, 'o-')
    pylab.title("Merge Sort")
    pylab.show()


# timmerMergeSort()


# ---------------------------


# Quick Sort


def timmerQuickSort():
    sizeInput = []
    timer = []
    for i in range(2, 3000):
        sizeInput.append(i)
        temp = []
        for j in range(i):
            temp.append(random.randint(0, 2000))

        start = time.time()
        main.quickSort(temp, 0, len(temp)-1)
        end = time.time()
        timer.append(end-start)

    pylab.plot(sizeInput, timer, 'o-')
    pylab.title("Quick Sort")
    pylab.show()


timmerQuickSort()


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


# timmerHeight()
