#dummy list

items_list = [1,2,3,4,5]


#sort the list - this returns a new list which is sorted
sorted(items_list)
sorted(items_list, reverse=True)

#sortin in place i.e. modifying the list itself to be sorted
items_list.sort()

#reverse list
items_list.reverse()

#insert element to the list
#the code below inserts value 1 to index 0
items_list.insert(0,1)

#remove element from list
items_list.pop()
#below removes element at 1st index
items_list.pop(1)


#list comprehensiions -- an easy way to create lists
even_numbers_only = [x for x in items_list if x % 2 === 0]
square_each_element = [x ** 2 for x in items_list]


#list of strings
string_list = ["abc", "def", "xyz"]

#list comprehensiions
strings_length_greater_than_3 = [x for x in items_list if len(x) >= 3]
strings_starting with_a  = [x for x in items_list if x[0] == "a"]


#join all strings in a list as single string - concatenation
''.join(string_list)


"""

USING  - queue - FIFO


"""
 from collections import deque

queue = deque([1,2,3,4,5])

#you can remove the first element in the queue easily. It is optimized for that
queue.popleft()

#you can also remove the last element
queue.pop()

#you can add element on left or right of the queue
queue.append(6)
queue.appendleft(0)

