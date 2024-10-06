l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
 
print(f'main list',l1)

#append() - Adds an item to the end of the list
l1.append(16)
print('After append',l1)

#extend() - Extends the list by appending elements from another iterable
l1.extend([17,18])
print('After extend',l1)

#insert() - Inserts an item at a given position
l1.insert(0,0)
print('After insert',l1)

#remove() - Removes the first item from the list with the specified value
l1.remove(0)
print('After remove',l1)

#pop() - Removes and returns an item at the given position (default is the last item)
pop_item=l1.pop()
print('popped item',pop_item)
print('After pop',l1)

#index() - Returns the index of the first item with the specified value
index_value=l1.index(15)
print('value index',index_value)

#count() - Returns the number of times a specified value occurs in a list
count_of_2 = l1.count(2)
print('Count of 2:', count_of_2)

#sort() - Sorts the items of the list in place (ascending order by default)
l1.sort()
print('After sort:', l1)

# reverse() - Reverses the order of the list
l1.reverse()
print('After reverse:', l1)

#copy() - Returns a shallow copy of the list
l2 = l1.copy()
print('Copy of the list:', l2)

#slice - Access a range of items
slice_of_list = l1[1:4] 
print('Slice of the list:', slice_of_list)

#clear() - Removes all items from the list
l1.clear()
print('After clear:', l1)