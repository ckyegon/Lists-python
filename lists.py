#!/bin/python3

#1. Creating an empty list

my_list = []

#2. appening to my_list

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("\nMy appended list: ", my_list)

#3. inserting 15 to second position of my list

my_list.insert(1, 15)

print("\nMy list with 15 inserted in second position: ", my_list)

#4. extending my list with other list

other_list = [50, 60, 70]
my_list.extend(other_list)
print("\nMy extended list: ", my_list)

#5. remove the lastelement from my list
my_list.pop()
print("\nMy list with last element removed: ", my_list)

#6.sort my list in ascending order

my_list.sort()
print("\nMy sorted list in ascending order: ", my_list)

#7. find and print the index of value 30

print("\nIndex of element 30 in my list: ", my_list.index(30))
