# Insertion sort is a method for sorting that starts with a single element (thus forming a trivially sorted list)
# and then incrementally inserts the remaining elements so that the list stays sorted.
# Time Complexity O(n^2)

def insertion_sort(item_list):
	for i in range(1, len(item_list)):
		j = i
		while j > 0 and item_list[j-1] > item_list[j]:
				item_list[j-1], item_list[j] = item_list[j], item_list[j-1]
				j = j-1

	print('Sorted list: ', item_list)


item_list = input('Enter the elements: ')
item_list = list(map(int, item_list.split()))

insertion_sort(item_list)