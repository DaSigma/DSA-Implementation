########## Basic Sorting ##########

import random


def bubble_sort(mylist):
   for i in range(len(mylist) - 1, 0, -1): #renge(start, stop, step)
      for j in range(i):
         if mylist[j] > mylist[j + 1]:
            mylist[j],mylist[j + 1] = mylist[j + 1], mylist[j]

def selection_sort(my_list):
   for i in range(len(my_list) - 1):
      min_index = i
      for j in range(i + 1, len(my_list)):
         if my_list[j] < my_list[min_index]:
            min_index = j
      my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

def insertion_sort(my_list):
   for i in range(1, len(my_list)):
      j = i - 1
      while my_list[j + 1] < my_list[j] and j >= 0:
         my_list[j + 1], my_list[j] = my_list[j], my_list[j + 1]
         j -= 1

def insertion_sort_algo(my_list):
    for i in range(len(my_list)):
        current = i
        while current > 0 and my_list[current-1] > my_list[current]:
            my_list[current], my_list[current-1] = my_list[current-1], my_list[current]
            current -= 1
    return my_list


### Merge Sort ###
# Lists have to be sorted
def merge(list1, list2): 
    # Merge two sorted lists into one sorted list
    combined = []
    # Initialize pointers for both lists
    p1, p2 = 0, 0
    # Compare elements from both lists and add smaller one to combined
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] < list2[p2]:
            combined.append(list1[p1])
            p1 += 1
        else:
            combined.append(list2[p2])
            p2 += 1
    # Append remaining elements from list1 if any
    while p1 < len(list1):
        combined.append(list1[p1])
        p1 += 1
    # Append remaining elements from list2 if any
    while p2 < len(list2):
        combined.append(list2[p2])
        p2 += 1
    return combined

def merge_sort(my_list):
   # Base case: a list of one element is already sorted
   if len(my_list) == 1:
      return my_list
   # Divide: split list into two halves
   mid_index = len(my_list) // 2
   left = merge_sort(my_list[:mid_index])
   right = merge_sort(my_list[mid_index:])
   
   # Conquer: merge the sorted halves
   return merge(left, right)
##################


####### Quick Sort #######+
def swap(my_list, index1, index2):
   my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left, right):
   if left < right:
      pivot_index = pivot(my_list, left, right)
      quick_sort_helper(my_list, left, pivot_index - 1)
      quick_sort_helper(my_list, pivot_index + 1, right)
   return my_list

def quick_sort(my_list):
   return quick_sort_helper(my_list, 0, len(my_list) - 1)
##########################


# l = ['a','z','n','r','q',]
# l2 = [8, 10, 9, 7, 11, 0]
n = 10
l = random.sample(range(1, 100), n)
# print('Unsorted', l, '\n')
# print(mergeSort(l))
# # l = [1,3,7,8]
# # l2 = [2,4,5,6]
# print('Sorted', l)

# l = [4,2,6,5,1,3,8, 10, 9, 7, 11, 0]

# l = [4, 6, 1, 7, 3, 2, 5]
print(f"l {l}")
# quick_sort(l)
print(f"l after sort {insertion_sort_algo(l)}")
