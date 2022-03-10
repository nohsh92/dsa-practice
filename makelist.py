import random

def makerandomlist(listlength, maxnum):
    randomlist = []
    for i in range(0,listlength):
        n = random.randint(1,maxnum)
        randomlist.append(n)
    return randomlist