# Nội dung:
#  code python 3 thuật toán cơ bản giải quyết 3 vấn đề về Dynamic Programming gồm
#  Coin Row Problem, Change Making Problem và Coin Collecting Problem


# ----------------------

#  Coin Row Problem


def coinRow(C):
    # Mục tiêu: áp dụng công thức * để giải quyết bài toán từ dưới lên.
    # Input: Một mảng C các đồng xu với các giá trị C[i] là dương.
    # Ouput: Tổng giá trị nhiều nhất các đồng xu có thể lấy được.

    F = []
    F.append(0)
    F.append(C[1])

    for i in range(2, len(C)):
        F.append(max(C[i]+F[i-2], F[i-1]))

    return F[len(C)-1]


# ---------------------------------

# Change Making Problem

def changeMaking(D, n):
    # Mục đích: Áp dụng Dynamic Programming để tìm số đồng xu tối thiểu để quy đổi cho n
    # Input: Mảng D gồm các giá trị của các loại đồng xu có kích thước m, và giá trị tiền cần đổi n. Và D[1] = 1
    # Output: Tổng số đồng xu tối thiểu
    F = []
    F.append(0)
    for i in range(1, n+1):
        temp = float('inf')
        j = 1
        while j <= len(D)-1 and i >= D[j]:
            temp = min(F[i-D[j]], temp)
            j = j+1
        F.append(temp+1)
    return F[n]


# --------------------------

# Coin Collecting Problem

def robotCoinCollection(C):
    # Mục tiêu: Áp dụng kĩ thuật Dynamic Programming để tìm số lượng đồng xu nhiều nhất nhặt được
    # tại vị trí n m khi đi từ vị trí (1,1). Và chỉ được di chuyển từ trên xuống hoặc trái qua phải.
    # Input: Một mảng C 2 chiều có kích thước n x m, nếu tại vị trí (i,j) có đồng xu thì C[i][j] = 1, ngược lại = 0.
    # Output: Số lượng đồng xu nhiều nhất có thể nhặt được
    F = [[0 for m in range(len(C[0]))] for n in range(len(C))]
    F[0][0] = C[0][0]
    for j in range(1, len(C[0])):
        F[0][j] = F[0][j-1]+C[0][j]
    for i in range(1, len(C)):
        F[i][0] = F[i-1][0]+C[i][0]
        for j in range(1, len(C[0])):
            F[i][j] = max(F[i-1][j], F[i][j-1])+C[i][j]

    return F[len(C)-1][len(C[0])-1]
