# 1. creating an empty list
my_list = []
print("Created list = ", my_list)

# 2. adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Appended list:", my_list)

# 3. inserting the value 15 at the second postion in the list
my_list.insert(1, 15)
print("After inserting:", my_list)

# 4. extending the list with another list
my_list.extend([50, 60, 70])
print("After extending:", my_list)

# 5. removing the last element from the list
my_list.pop()
print("After removing the last elements",my_list)

# 5. sorting the list in ascenging order
my_list.sort()
print("Sorted list:", my_list)

# 6. finding and printing the index of the value 30
print("Index for value 30 =",my_list.index(30))