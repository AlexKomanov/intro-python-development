my_list = [1, 2, 3, 4, 5]
print(my_list[0])

# print(my_list[7])   --> IndexError: list index out of range

print("length ", len(my_list))

print(my_list[len(my_list) - 1])

print(my_list[-1])

# Slicing
print(my_list[0:3])
print(my_list[::-1])

# Modifying list
my_list[0] = "a"
print(my_list)

my_list[0:2] = []

print(my_list)

print(my_list.pop())

print(my_list)

my_list.remove(3)
print(my_list)

my_list.append(5)

print(my_list)

my_list.insert(0, 3)
print(my_list)
