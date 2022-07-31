from random import randint, random
from hello import mergeSort, data, ShuffleArray,bubble_sort, selection_sort
from time import time
import numpy as np
from matplotlib import pyplot as plt
# Best Case

averagecase = [randint(1,10000) for _ in range (100)]
bestcase = sorted(averagecase)
worstcase = sorted (averagecase,reverse=True)


def test_BubbleWorst():
   start= time()
   assert bubble_sort(worstcase) == bestcase
   print(time()-start)

def test_BubbleBest():
   start= time()
   assert bubble_sort(bestcase) == bestcase
   print(time()-start)

def test_BubbleAvg():
   start= time()
   assert selection_sort(averagecase) == bestcase
   print(time()-start)

def test_SelectionWorst():
   start= time()
   assert selection_sort(worstcase) == bestcase
   print(time()-start)

def test_SelectionBest():
   start= time()
   assert selection_sort(bestcase) == bestcase
   print(time()-start)

def test_SelectionAvg():
   start= time()
   assert selection_sort(averagecase) == bestcase
   print(time()-start)


def test_mergeSortWorst():
    start= time()
    assert mergeSort(worstcase, 0, len(worstcase) - 1) == bestcase
    print(time()-start)

def test_mergeSortBest():
    start= time()
    assert mergeSort(bestcase, 0, len(bestcase) - 1) == bestcase
    print(time()-start)

def test_mergeSortAvg():
    start= time()
    assert mergeSort(averagecase, 0, len (averagecase) - 1) == bestcase
    print(time()-start)

def ShuffleArray(arr):
    oldArray = np.copy(arr)
    newArray = []
    currentLen = len(arr) - 1

    while(currentLen > -1):
        randIndex = randint(0, currentLen)
        newArray.append(oldArray[randIndex])
        oldArray = np.delete(oldArray, randIndex)
        currentLen -= 1
    return newArray

