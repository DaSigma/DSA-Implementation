

list1:  list[int] = [1]
list2: list[int] =[1]
def item_in_common(l1, l2):
     check_dict = {}
     for n in l1:
          check_dict[n] = check_dict.get(n, 0) + 1
     print(check_dict)

     for n in l2:
          if n in check_dict:
                return True
     return False

# itemInCommon(l1, l2)
print(item_in_common(list1, list2))


def propitiation(JESUS):
     if JESUS:
          print('You are saved!')
     else:
          print('You need JESUS')

propitiation(False)


'''Bubble sort Algorithm
1. Define function that takes a list
2. Loop through list in reverse order (from end to start)
3. Inner loop compares adjacent elements from start to current position
4. If left element > right element, swap them
5. After each pass, largest unsorted element "bubbles up" to its correct position
6. Repeat until entire list is sorted
Time Complexity: O(n²), Space Complexity: O(1)
'''

'''Selection sort Algorithm
1. Define function that takes a list
2. Loop through list from start to end
3. Find minimum element in unsorted portion (from current index to end)
4. Swap minimum element with element at current position
5. After each pass, smallest unsorted element is "selected" and placed in correct position
6. Repeat until entire list is sorted
Time Complexity: O(n²), Space Complexity: O(1)
'''

'''Insertion sort Algorithm
1. Define function that takes a list
2. Loop through list starting from second element (index 1)
3. Store current element as temporary value
4. Compare with elements in sorted portion (left side)
5. Shift larger elements one position right
6. Insert temporary value at correct position in sorted portion
7. Repeat until entire list is sorted
Time Complexity: O(n²), Space Complexity: O(1)
'''

'''Merge sort Algorithm
1. Define function that takes a list
2. Base case: if list has 1 or 0 elements, return it (already sorted)
3. Divide list into two halves (find middle index)
4. Recursively sort left half
5. Recursively sort right half
6. Merge the two sorted halves into one sorted list
7. Compare first elements of both halves, take smaller one
8. Repeat comparison until all elements are merged
Time Complexity: O(n log n), Space Complexity: O(n)
'''

'''Quick sort Algorithm
1. Define function that takes a list
2. Base case: if list has 1 or 0 elements, return it (already sorted)
3. Choose a pivot element (typically first, last, or middle element)
4. Partition: rearrange list so elements < pivot are on left, > pivot are on right
5. Recursively sort left partition (elements less than pivot)
6. Recursively sort right partition (elements greater than pivot)
7. Concatenate: left + [pivot] + right
Time Complexity: O(n log n) average, O(n²) worst case, Space Complexity: O(log n)
'''

'''Binary search Algorithm
1. Define function that takes a list
2. Loop through list from start to end with while loop
3. Define middle element of list
4. If middle element is greater than target element, discard everything to the right
5. If middle element is less than target element, discard everything to the left
6. If middle element is equal to target element, return the middle element's index
7. If the target is not found, return -1
'''