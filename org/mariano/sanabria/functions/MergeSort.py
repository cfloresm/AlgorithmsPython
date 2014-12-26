#Modulo MergeSort.py
from Merge import merge

def mergeSort(list):
     if len(list) < 2:
         return list
     middle = len(list) / 2
     left = mergeSort(list[:middle])
     right = mergeSort(list[middle:])
     return merge(left, right)
