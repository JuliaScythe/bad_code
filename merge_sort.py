#!/usr/bin/python3

## Comments with double hashes should be removed as they detail the bugs
## included in the code.

include random ## 'include' is not a Python keyword

def merge_sort(to_sort):
  """
  Runs a merge sort on the given list in-place.
    to_sort: The list to be sorted
  """

  # If the list has 0 or 1 elements, it is already sorted
  if len(to_sort) <= 1:
    return to_sort

  # Split the list into two parts
  mid = len(to_sort) / 2 ## Must be converted to an integer
  list_a = to_sort[:mid]
  list_b = to_sort[mid:]

  # Recursively sort each half
  list_a = merge_sort(list_a)
  list_b = merge_sort(list_b)

  lst_sorted = list()

  # Merge the lists
  i = 0
  j = 0
  while i < len(list_a) and j < len(list_b) ## Missing colon
    if list_a[i] < list_b[j]:
      lst_sorted.append(list_a[i])
      i++ ## Python does not have pre/post-increment operators
    else:
      lst_sorted.append(list_b[j])
      j++ ## Python does not have pre/post-increment operators

  # There are only elements from one list left. Combine them in
  if i < len(list_a):
    lst_sorted += list_a[i:]
  elif j < len(list_b):
    lst_sorted += list_b[j:]

  retrun lst_sorted ## Typo on "return"

# Generate 50 random values
to_sort = [for i in range(50): random.randint(0, 100)] ## Invalid list comprehension syntax

print merge_sort(to_sort) ## 'print' is a function in Python 3
