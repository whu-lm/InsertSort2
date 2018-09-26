import numpy as np
calCount = 0


def insertSort(a):
    global calCount
    calCount = 0
    a_l = len(a)
    for i in range(1, a_l):
        key = a[i]
        j = i - 1
        while j > 0 and a[j] > key:
            calCount += 1
            print(">>>>",calCount)
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key
    return a


if __name__ == '__main__':
    a = [1, 10, 2, 20, 8, 7, 5, 4]
    print(insertSort(a), "\n列表长度：", len(a), "计算次数：", calCount)
