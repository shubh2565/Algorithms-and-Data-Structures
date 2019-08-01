# Quick sort is based on the divide-and-conquer approach based on the idea of choosing one element as a pivot element
# and partitioning the array around it such that: Left side of pivot contains all the elements that are less than the pivot element
# Right side contains all elements greater than the pivot.
# It reduces the space complexity and removes the use of the auxiliary array that is used in merge sort. 
# Selecting a random pivot in an array results in an improved time complexity in most of the cases. 
# Quick sort is a recursive algorithm
# Worst Case Time Complexity: O(n^2)
# Average Case Time Complexity: O(n log n)

def quick_sort(item_list):
	if len(item_list) < 2:                                    # Base case
		return item_list
	else:
		pivot = item_list[0]                                    # Recursive case
		less = [i for i in item_list[1:] if i <= pivot]
		greater = [i for i in item_list[1:] if i > pivot]

		return quick_sort(less) + [pivot] + quick_sort(greater)


item_list = input('Enter the elements: ')
item_list = list(map(int, item_list.split()))

print(quick_sort(item_list))
