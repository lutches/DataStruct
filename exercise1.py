import random

def binarySearch(numList, item):

    lo = 0
    hi = len(numList) - 1
    while (lo <= hi):
        mid = (lo+hi) // 2

        if (item < numList[mid]):
            lo = lo - 1

        elif (item > numList[mid]):
            hi = hi + 1

        else:
            return mid

    return -1

def generateRandList(length):
    list = []
    for i in range(length):
        list.append(random.randint(0, 50))

    list.sort()
    return list



if __name__ == "__main__":
    print(binarySearch(generateRandList(100), 5))

