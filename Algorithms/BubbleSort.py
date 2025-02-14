


def bubbleSort(mylist):
   for i in range(len(mylist) - 1, 0, -1):
      for j in range(i):
         if mylist[j] > mylist[j + 1]:
            temp = mylist[j]
            mylist[j] = mylist[j + 1]
            mylist[j + 1] = temp
l = [4,2,6,5,1,3]
print('Unsorted', l)
bubbleSort(l)
print('Sorted', l)