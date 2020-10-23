# Nội dung:
#  code python 3 thuật toán cơ bản về divide and conquer gồm merge sort, quick sort và Binary Tree Traversals


# ----------------------


# thuật toán merge sort


def mergeSort(A):
    # sắp xếp mảng bởi đệ quy merge sort.
    # input :1 mảng A có kích thước n phần tử
    # output: Mảng được sắp xếp tăng dần

    if len(A) > 1:
        B = []
        C = []
        for i in range(len(A)//2):
            B.append(A[i])
        for i in range(len(A)//2, len(A)):
            C.append(A[i])
        mergeSort(B)
        mergeSort(C)
        merge(B, C, A)


def merge(B, C, A):
    # purpose : Hợp 2 mảng B C thành mảng A theo thứ tự tăng dần.
    # Input: mảng B có kích thước p, mảng C có kích thước q, mảng A có kích thước p+q
    # Ouput: Sắp xếp mảng A từ mảng B và C
    i = 0
    j = 0
    k = 0
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            A[k] = B[i]
            i = i+1
        else:
            A[k] = C[j]
            j = j+1
        k = k+1
    if i == len(B):
        for n in range(j, len(C)):
            A[k] = C[n]
            k = k+1
    else:
        for n in range(i, len(B)):
            A[k] = B[n]
            k = k+1


# -----------------------

# Quick Sort

def quickSort(A, l, r):
    # mục đích: sắp xếp mảng theo thuật toán quicksort
    # input: một mảng A và l là index đầu và r là index của phần tử cuối trong mảng
    # output: mảng A được sắp xếp tăng dần.
    if l < r:
        s = partition(A, l, r)
        quickSort(A, l, s-1)
        quickSort(A, s+1, r)


def partition(A, l, r):
    # mục đích, đẩy các giả trị nhỏ hơn pivot sang bên trái và giá trị lớn hơn sang bên phải
    # input Mảng A và index l của phần tử đầu tiền và index r của phần tử cuối cùng trong Mảng A hiện tại
    # output Trả về index của pivot hiện tại trong mảng A.

    p = A[l]
    i = l
    j = r
    while i < j:
        i = i+1
        while A[i] < p:
            i = i+1
            if i > r:
                i = r
                break
        while A[j] > p:
            j = j-1
            if j < l:
                j = l
                break
        A[i], A[j] = A[j], A[i]
    A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


# ----------------------------

# Binary tree Traversals

def height(T):
    # Tính chiều cao của cây nhị phân
    # input: Cây nhị phân T
    # output chiều cao cây T
    if T == None:
        return -1
    return max(height(T.left), height(T.right))+1


class node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


# Hàm tạo cây binary tree để thuận tiên test running time
def initialBinaryTree(T, n):
    if n == 0:
        return
    T.left = node()
    T.right = node()
    initialBinaryTree(T.left, n-1)
    initialBinaryTree(T.right, n-1)
