########## Sorting ##########

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
         
      
        
l = ['a','z','n','r','q',]
# l = [4,2,6,5,1,3]
print('Unsorted', l)
insertionSort(l)
print('Sorted', l)