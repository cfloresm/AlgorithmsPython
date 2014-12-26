#Modulo QuickSort.py
def quickSort(list):
	if len(list) < 1:
		return list
	else:
		pivot = list[0]
		lesser = quickSort([x for x in list[1:] if x < pivot])
		greater = quickSort([x for x in list[1:] if x >= pivot])
		return lesser + [pivot] + greater
