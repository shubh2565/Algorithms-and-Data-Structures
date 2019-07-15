# A linear search, also known as sequential search is a method for finding an element within a given list of items.
# It sequentially checks each element of the list until a match is found or the whole list has been searched.
# Time complexity O(n)
# NOTE: This code search only for the first occurence of item required to be search.

def linear_search(item_list, search):
	for i in item_list:
		if i == search:
			return  print('Item found in the list at index: ', item_list.index(i) + 1)
		
	return print('Item not found')

item_list = input('Enter the list of numbers: ')
item_list = list(map(int, item_list.split()))

search = int(input('Enter the seach item: '))

linear_search(item_list, search)
