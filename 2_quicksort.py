from makelist import makerandomlist
import time
import sys

sys.setrecursionlimit(1500)

randomList = makerandomlist(100000, 99)


def traditionalQuicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return traditionalQuicksort(less) + [pivot] + traditionalQuicksort(greater)

def newQuicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[len(array)//2]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return newQuicksort(less) + [pivot] + newQuicksort(greater)

TradStart = time.time()
traditionalQuicksort(randomList)
TradEnd = time.time()
print("Time for execution of Traditional Quicksort is: {}".format(round(TradEnd-TradStart, 5)))

NewStart = time.time()
newQuicksort(randomList)
NewEnd = time.time()
print("Time for execution of New Quicksort is: {}".format(round(NewEnd-NewStart, 5)))

print("The *new quicksort is actually worse : perhaps due to added complexity of calculating middle of array")

# print(quicksort([10, 5, 2, 3]))

# print(randomList)
