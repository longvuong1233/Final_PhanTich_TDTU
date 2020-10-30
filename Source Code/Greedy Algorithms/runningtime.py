# Nội dung
#  Draw running time of each algorithm with different inputs size


import main
import random
import time
import pylab


# ------------------------------------------

testcase = [[0, 9, 0, 4, 0, 2, 7, 1, 8, 2, 0, 0, 4, 3, 8, 8, 4, 5, 8, 1], [
            9, 0, 9, 1, 5, 7, 6, 5, 8, 4, 3, 1, 7, 0, 2, 0, 7, 8, 8, 5], [
            0, 9, 0, 0, 8, 7, 4, 6, 6, 8, 7, 0, 0, 9, 3, 5, 5, 6, 3, 0], [
            4, 1, 0, 0, 0, 7, 8, 6, 8, 5, 0, 5, 7, 3, 8, 7, 5, 6, 5, 1], [
            0, 5, 8, 0, 0, 5, 6, 4, 9, 9, 5, 2, 0, 2, 1, 5, 4, 0, 7, 7], [
            2, 7, 7, 7, 5, 0, 4, 6, 1, 6, 2, 6, 3, 1, 0, 2, 7, 9, 9, 6], [
            7, 6, 4, 8, 6, 4, 0, 1, 8, 8, 9, 3, 0, 3, 9, 8, 7, 1, 2, 9], [
            1, 5, 6, 6, 4, 6, 1, 0, 8, 2, 0, 7, 2, 5, 5, 7, 8, 4, 0, 4], [
            8, 8, 6, 8, 9, 1, 8, 8, 0, 9, 2, 6, 7, 4, 5, 0, 2, 3, 3, 9], [
            2, 4, 8, 5, 9, 6, 8, 2, 9, 0, 4, 2, 1, 6, 3, 6, 6, 8, 1, 5], [
            0, 3, 7, 0, 5, 2, 9, 0, 2, 4, 0, 1, 6, 1, 0, 6, 8, 8, 2, 6], [
            0, 1, 0, 5, 2, 6, 3, 7, 6, 2, 1, 0, 4, 9, 0, 2, 3, 4, 2, 0], [
            4, 7, 0, 7, 0, 3, 0, 2, 7, 1, 6, 4, 0, 3, 2, 5, 6, 3, 1, 2], [
            3, 0, 9, 3, 2, 1, 3, 5, 4, 6, 1, 9, 3, 0, 8, 0, 2, 9, 7, 5], [
            8, 2, 3, 8, 1, 0, 9, 5, 5, 3, 0, 0, 2, 8, 0, 7, 3, 3, 7, 4], [
            8, 0, 5, 7, 5, 2, 8, 7, 0, 6, 6, 2, 5, 0, 7, 0, 8, 2, 5, 8], [
            4, 7, 5, 5, 4, 7, 7, 8, 2, 6, 8, 3, 6, 2, 3, 8, 0, 0, 1, 1], [
            5, 8, 6, 6, 0, 9, 1, 4, 3, 8, 8, 4, 3, 9, 3, 2, 0, 0, 3, 0], [
            8, 8, 3, 5, 7, 9, 2, 0, 3, 1, 2, 2, 1, 7, 7, 5, 1, 3, 0, 4], [
            1, 5, 0, 1, 7, 6, 9, 4, 9, 5, 6, 0, 2, 5, 4, 8, 1, 0, 4, 0]
            ]

# Prim


def timmerPrim():
    sizeInput = []
    timer = []
    for i in range(2, 21):
        sizeInput.append(i)
        temp = [[testcase[n][m] for m in range(i)] for n in range(i)]

        start = time.time()
        print(main.dijkstra(temp, 0))
        end = time.time()
        timer.append((end-start)*1000)  # đơn vị time là s

    pylab.plot(sizeInput, timer, 'o-')
    pylab.show()


timmerPrim()


# ------------------------------------

# Thuật toán Kruskal
g_1 = main.Graph(4)
g_1.addEdge(0, 1, 10)
g_1.addEdge(0, 2, 6)
g_1.addEdge(0, 3, 5)
g_1.addEdge(1, 3, 15)
g_1.addEdge(2, 3, 4)

g_2 = main.Graph(10)
g_2.addEdge(0, 1, 10)
g_2.addEdge(0, 2, 6)
g_2.addEdge(0, 3, 5)
g_2.addEdge(0, 4, 8)
g_2.addEdge(0, 5, 9)
g_2.addEdge(0, 6, 12)
g_2.addEdge(0, 7, 14)
g_2.addEdge(0, 8, 4)
g_2.addEdge(0, 9, 2)
g_2.addEdge(1, 9, 1)
g_2.addEdge(2, 3, 4)

g_3 = main.Graph(15)
g_3.addEdge(0, 1, 10)
g_3.addEdge(0, 2, 6)
g_3.addEdge(0, 3, 5)
g_3.addEdge(0, 4, 8)
g_3.addEdge(0, 5, 9)
g_3.addEdge(0, 6, 12)
g_3.addEdge(0, 7, 14)
g_3.addEdge(0, 8, 4)
g_3.addEdge(0, 9, 2)
g_3.addEdge(0, 10, 1)
g_3.addEdge(0, 11, 8)
g_3.addEdge(0, 12, 7)
g_3.addEdge(0, 13, 14)
g_3.addEdge(1, 14, 20)
g_3.addEdge(2, 3, 4)

g_4 = main.Graph(25)
g_4.addEdge(0, 1, 10)
g_4.addEdge(0, 2, 6)
g_4.addEdge(0, 3, 5)
g_4.addEdge(0, 4, 8)
g_4.addEdge(0, 5, 9)
g_4.addEdge(0, 6, 12)
g_4.addEdge(0, 7, 14)
g_4.addEdge(0, 8, 4)
g_4.addEdge(0, 9, 2)
g_4.addEdge(0, 10, 1)
g_4.addEdge(0, 11, 8)
g_4.addEdge(0, 12, 7)
g_4.addEdge(0, 13, 14)
g_4.addEdge(1, 14, 28)
g_4.addEdge(1, 15, 22)
g_4.addEdge(1, 16, 21)
g_4.addEdge(1, 17, 20)
g_4.addEdge(1, 18, 15)
g_4.addEdge(1, 19, 13)
g_4.addEdge(2, 3, 4)
g_4.addEdge(2, 20, 77)
g_4.addEdge(2, 21, 8)
g_4.addEdge(2, 22, 9)
g_4.addEdge(2, 23, 3)
g_4.addEdge(23, 24, 2)


mycase = [g_1, g_2, g_3, g_4]


def timmerKruskal():
    sizeInput = []
    timer = []
    for i in range(len(mycase)):
        sizeInput.append(mycase[i].V)
        start = time.time()
        print(main.kruskal(mycase[i]))
        end = time.time()
        timer.append((end-start)*1000)  # đơn vị time là s
    pylab.plot(sizeInput, timer, 'o-')
    pylab.show()


# timmerKruskal()
