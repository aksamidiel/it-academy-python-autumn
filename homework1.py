
#task_1
print('Hello, world!')
#task_2
name = input('What is your name?\n')
print('Hi, %s.' % name)
#task_3
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print ("iteration {iteration} is {name}".format(iteration=i, name=name))

#task_4
parents, babies = (1, 1)
while babies < 100:
    print ('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)
#task_5
def greet(name):
    print ('Hello', name)

greet('Jack')
greet('Jill')
greet('Bob')


#test_palindrome
number = input('Enter number: ')
n = number[::-1] #переворот чтение введенного с последнего символа <----
if number == n:
  print("yes, this is palindrome")
else:
  print("no, this is not palindrome")


