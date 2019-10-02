print("create list with list comprehension ")
# n = int(input("Enter number of range: "))

lst_1 = [[a, b] for a in 'abcd' if 'a' <= a <= 'd' for b in 'abcd' if 'b' <= b <= 'd']
print("Result: ", lst_1)

# flat_list = [item for sublist in lst_1 for item in sublist]

flat_list = []
for sublist in lst_1:
    for item in sublist:
        flat_list.append(item)
print(flat_list)




