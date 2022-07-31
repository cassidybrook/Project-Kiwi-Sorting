from array import array
from posixpath import split
import numpy as np
from typing import Text
import time
import pytest as pt
from random import randint
from matplotlib import pyplot as plt

with open('C:\\Users\\cassi\\OneDrive\\Desktop\\PYTHON\\hello\\kiwidata.txt') as file: 
     dataString = file.read() 
dataString = dataString.split(',')
dataString.remove('')
data = np.array(dataString).astype(np.float64)


# startTime = time.time()
# def bubble_sort(kiwi):  #Bubble_sort function.
#        for i in range(0,len(kiwi)-1):  #i =index.
#            for j in range(len(kiwi)-1): #The function len() returns the length of an object.
#                if(kiwi[j]>kiwi[j+1]):  #If value in list is greater than value to the right of it.
#                    temp = kiwi[j]  
#                    kiwi[j] = kiwi[j+1]  #Switch the values if they are not in higher to lower order.
#                    kiwi[j+1] = temp  #Temp = Temporary files, or "tempfiles", are mainly used to store intermediate information on disk for an application.
    
#        return kiwi         

# endTime = time.time()-startTime
# print("The sorted list is:", bubble_sort(data))  #Prints the data.
# print("Seconds code takes to run =", endTime - startTime)





    
# # #............................................................................................................................................................

# startTime = time.time()
# def selection_sort(kiwi): #Create function selection_sort, sequence is (kiwi).
#     indexing_length = (len(kiwi)-1) #Specifying indexing length..using -1 bc when have 1 item left in unsorted list no comparrision needed.
#     for i in range(indexing_length): #For loop, setting i to 0.
#             min_value = i #Each itteration first element in unsorted list to be default min.

#     if kiwi[indexing_length] < kiwi[min_value]: #List in J position less than current min value then need to replace min value.                  
#         min_value = indexing_length #Going through all the elements to the right of index. If something smaller change to min value.

#         if min_value != i: #Switching the min value. if we find item at lower value then need to switch those items.
#                    kiwi[min_value], kiwi[i] = kiwi[i], kiwi[min_value] #Kiwi in min value pos, kiwi in high pos, = kiwi in high pos,
#                    # kiwi in low pos.
#     return kiwi #Line up with FOR statement.
# endTime = time.time()-startTime
# print("The data list is:",selection_sort(data)) #funtion selection sort, passing (data).
# print("Seconds code takes to run =", endTime - startTime)

#.......................................................................................................................................

# Python program for implementation of MergeSort.

# Merges two subarrays of arr[].
# First subarray is arr[l..m].
# Second subarray is arr[m+1..r].

# Python program for implementation of MergeSort,
# Merges two subarrays of arr[].
# First subarray is arr[l..m].
# Second subarray is arr[m+1..r].

def merge(arr, l, m, r): #We define a function (merge) when we need to sort a list of unsorted elements (1 array).
    n1 = m - l + 1
    n2 = r - m
#Create temp arrays.
    L = [0] * (n1)
    R = [0] * (n2)         
    for i in range(0, n1): #Declare left variable to 0 and right variable to n-1. 
        L[i] = arr[1 + i] #Data is copied to temp arrays L and R.

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

  	# Merge the temp arrays back into arr[l..r].
    i = 0	 #Index of first subarray.
    j = 0	 #Index of second subarray.
    k = l	 #Index of merged subarray.
     #Declare array and left, right, mid variable. 
     #If the elements are more than 1, then we are trying to get the median value,
     #of the list to divide the whole list into two parts (left and right) for further, 
     #recursive call. Each recursive call divides the list into left and right until two,
     #adjacent entries are acquired.
    while i < n1 and j < n2:
        if L[i] <= R[j]:  #If i is less than or equal to j then its checking the left most element in the left subarray,
                         #And the right subarry.  
            arr[k] = L[i] #Ads the lowest element to the merged array.
            i += 1 #Adding 1 to i, if i less than j then we need to increase i to check next element.else:
        else:
            arr[k] = R[j] #K refers to index in merged array. left most index in merged array is equal to the left most index in right array.
            j += 1 #Adding 1 to j, if less than i we need to incease j to check next element. 
        k += 1 #In both cases increase K.

	
    while i < n1: #Checking second element.
        arr[k] = L[i] #Checking left most in left array with the second to left most in left array.
        i += 1 #Adding 1 to i if less than n1, 
        k += 1 #Adding 1 to k if less than n1,

    while j < n2: #Checking right sub array.
        arr[k] = R[j] #Checking right most in right array .
        j += 1 #Adding 1 to j if less than n2.
        k += 1 #Adding 1 to k if less than n2.

	
def mergeSort(arr, l, r): #New function mergeSort. 
    if l < r: #If index of left most and index of right most.. if theres more than 1 item. 
        m = l+(r-l)//2 #Splitting.
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
    return arr #Perform merge function.


unsortedList = np.copy(data) #Copying the data.
startTime = time.time()
sortedList= mergeSort(unsortedList,0,len(unsortedList)-1) #Calling the function, sorting the list 0,-1 length. 
endTime = time.time()
print(sortedList)
print("Seconds code takes to run =", endTime - startTime) #Timing the efficency.

#Sorting the unsorted data and printing the sorted to the output.

indexes = [0] * (len(data)) #creating an array for the graph 
for i in range (len(indexes)): #populating
    indexes [i] = i



plt.figure(1)
plt.scatter(indexes, sortedList)
plt.figure(2)
plt.scatter (indexes,data)
plt.show()