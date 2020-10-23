# Nội dung:
#  code python 3 thuật toán cơ bản về brute force gồm selection sort, bubble sort và sequential search



# ----------------------


# Thuật toán sắp xếp brute force
def selectionSort(A):
    # Purpose: Sắp xếp mảng theo thứ tự tăng dần
    # Input: Một mảng có kích thước n phần tử
    # Output: Mảng đầu vào đã được sắp xếp theo thứ tự tăng dần
    for i in range(0, len(A)-1):
        min = i
        for j in range(i+1, len(A)):
            if A[j] < A[min]:
                min = j
        A[min], A[i] = A[i], A[min]


# -----------------

# Thuật toán bubble sort

def bubbleSort(A):
    # Purpose: Sắp xếp mảng theo thứ tự tăng dần.
    # Input: Một mảng có kích thước n phần tử
    # Output: Mảng đầu vào đã được sắp xếp theo thứ tự tăng dần
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            if A[j+1] < A[j]:
                A[j+1], A[j] = A[j], A[j+1]


# -------------**

# Thuật toán sequential search


def sequentialSearch(A, k):
    # Purpose:Tìm kiếm key k trong mảng một cách tuần tự
    # Input: Một mảng cần duyệt có kích thước n phần tử A[0,n-1] và giá trị cần tìm k
    # Output: index của phần tử cần tìm trong A hoặc -1 nếu không tìm thấy
    A.append(k)
    i = 0
    while A[i] != k:
        i = i+1

    if i < len(A)-1:
        return i
    return -1
