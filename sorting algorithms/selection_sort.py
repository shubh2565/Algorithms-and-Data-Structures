# Selection sort is an in-place comparison sort, which repeatedly identifies the smallest remaining unsorted element
# and puts it at the end of the sorted portion of the array.
# Time Complexity O(n^2)

def selection_sort(item_list):
	for i in range(0, len(item_list)-1):
		smallest = i
		for j in range(i+1, len(item_list)):
			if item_list[j] < item_list[smallest]:
				smallest = j
		item_list[smallest], item_list[i] = item_list[i], item_list[smallest]

	print('Sorted list: ', item_list)


item_list = input('Enter the elements: ')
item_list = list(map(int, item_list.split()))

selection_sort(item_list)
