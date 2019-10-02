# for j in range(first_position, last_position):
#    print("Result: ", lst[j])

# 2. Use a list comprehension to construct the
# list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].

print("create list with list comprehension ")
# n = int(input("Enter number of range: "))

lst_1 = [[a + b] for a in 'abcd' if 'a' <= a <= 'd' for b in 'abcd' if 'b' <= b <= 'd']
print("Result: ", lst_1)

flat_list = [item for sublist in lst_1 for item in sublist][:6]
print(flat_list)

# 3. Use a slice on the above list to construct the
# list ['ab', 'ad', 'bc'].
print(flat_list[0::2])

# 4. Use a list comprehension to construct the list ['1a', '2a', '3a', '4a']

print("create new list with list comprehension ")
lst_2 = [[str(i) + 'a'] for i in range(1, 5)]
flat_list_2 = [item for sublist in lst_2 for item in sublist]
print("Result: ", flat_list_2)

# 5. Simultaneously remove the element '2a'
# from the above list and print it.
print("pop '2a' ")
print(flat_list_2.pop(1))

# 6. Copy the above list and add '2a'
# back into the list such that the
# original is still missing it.

print("velcom back")
print(flat_list_2)
flat_list_3 = flat_list_2.copy()

print(flat_list_3)

flat_list_3.insert(1, '2a')

print(flat_list_3)
