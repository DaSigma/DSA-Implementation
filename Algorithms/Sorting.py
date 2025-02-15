########## Basic Sorting ##########

import random


def bubbleSort(mylist):
   for i in range(len(mylist) - 1, 0, -1):
      for j in range(i):
         if mylist[j] > mylist[j + 1]:
            mylist[j],mylist[j + 1] = mylist[j + 1], mylist[j]

def selectionSort(myList):
   for i in range(len(myList) - 1):
      minIndex = i
      for j in range(i + 1, len(myList)):
         if myList[j] < myList[minIndex]:
            minIndex = j
      myList[i], myList[minIndex] = myList[minIndex], myList[i]

def insertionSort(myList):
   for i in range(1, len(myList)):
      j = i - 1
      while myList[j + 1] < myList[j] and j >= 0:
         myList[j + 1], myList[j] = myList[j], myList[j + 1]
         j -= 1


### Merge Sort ###
# Lists have to be sorted
def merge(list1, list2): 
    combined = []
    p1, p2 = 0, 0
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] < list2[p2]:
            combined.append(list1[p1])
            p1 += 1
        else:
            combined.append(list2[p2])
            p2 += 1
    while p1 < len(list1):
        combined.append(list1[p1])
        p1 += 1
    while p2 < len(list2):
        combined.append(list2[p2])
        p2 += 1
    return combined

def mergeSort(myList):
   if len(myList) == 1:
      return myList
   midIndex = len(myList)//2
   left = mergeSort(myList[:midIndex])
   right = mergeSort(myList[midIndex:])
   
   return merge(left, right)
##################


####### Quick Sort #######+
def swap(myList, index1, index2):
   myList[index1], myList[index2] = myList[index2], myList[index1]

def pivot(myList, pivotIndex, endIndex): 
    swapIndex = pivotIndex
    for i in range(pivotIndex + 1, endIndex + 1):
        if myList[i] < myList[pivotIndex]:
            swapIndex += 1
            swap(myList, swapIndex, i)
    swap(myList, pivotIndex, swapIndex)
    return swapIndex


def quickSortHelper(myList, left, right):
   if left < right:
      pivotIndex = pivot(myList, left, right)
      quickSortHelper(myList, left, pivotIndex -1)
      quickSortHelper(myList, pivotIndex + 1, right)
   return myList

def quickSort(myList):
   return(quickSortHelper(myList, 0, len(myList) - 1))
##########################


# l = ['a','z','n','r','q',]
# l2 = [8, 10, 9, 7, 11, 0]
n = 100
l = random.sample(range(1, 1000), n)
# print('Unsorted', l, '\n')
# print(mergeSort(l))
# # l = [1,3,7,8]
# # l2 = [2,4,5,6]
# print('Sorted', l)

# l = [4,2,6,5,1,3,8, 10, 9, 7, 11, 0]

# l = [4, 6, 1, 7, 3, 2, 5]
print(l)
quickSort(l)
print(l)
