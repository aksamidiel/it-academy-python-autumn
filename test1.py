some_simple_string = input("Enter some string: ").replace(' ', '_')
while "__" in some_simple_string:
    some_simple_string = some_simple_string.replace('__', '_')
print(some_simple_string)


