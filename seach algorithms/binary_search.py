# Binary search compares the target value to the middle element of the array.
# If they are not equal, the half in which the target cannot lie is eliminated and
# the search continues on the remaining half, again taking the middle element to compare to the target value, 
# and repeating this until the target value is found. (Source: Wikipedia)
# Binary search can only be suucessful when all the elements in the given array/list are sorted.
# Time complexity is O(log n)
# NOTE: this program assumes that the elements in the list are already sorted.


def bianry_search(item_list, search):
	lower = 0
	upper = len(item_list) - 1
	while upper >= lower:
		middle = (upper + lower)//2
		if item_list[middle] == search:
			return print('Element find at position: ', middle+1)
		if item_list[middle] > search:
			upper = middle -1
		else:
			lower = middle +1
	return print('Element not found in the list')


item_list = input('Enter the elements in the sorted order: ')
item_list = list(map(int, item_list.split()))

search = int(input('Enter the search element: '))

bianry_search(item_list, search)