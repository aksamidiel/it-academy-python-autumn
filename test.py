# Tuple practice
# Create the list ['a', 'b', 'c'], then create a tuple from that list

print("Create list: ")
lst = [i for i in input("Enter a, b, c or other symbols "
                        "without spaces or symbols of punctuation: ")]

print(lst)

# Create the tuple ('a', 'b', 'c'),
# then create a list from that tuple.
# (Hint: the material needed to do this has been covered,
# but it's not entirely obvious)

print("Create tuple: ")
tpl = tuple(lst)
print(tpl)

lst_1 = list(tpl)
print(lst_1)

# Make the following instantiations simultaneously:
# a = 'a', b=2, c='gamma'. (That is, in one line of code)

a, b, c = ('a', 2, 'gamma')
print((a, b, c))

# Create a tuple containing just a single element which in
# turn contains the three elements 'a', 'b', and 'c'.
# Verify that the length is actually 1 by using the len() function.

print("Create one - element tuple: ")
lst_3 = [k for k in input("enter some symbols: ")]
print(type(lst_3))
print("lst_3: ", lst_3)
tpl_2 = tuple([lst_3], )
print("length tuple: ", len(tpl_2))
print("tuple: ", tpl_2)


