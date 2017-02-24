# List Operation
colors = ['red', 'blue', 'green']
print(colors[0])    ## red
print(colors[2])    ## green
print(len(colors))  ## 3

#APPEND
list = ['larry', 'curly', 'moe']
list.append('shemp')            ## append elem at end, returns None
list.insert(0, 'xxx')           ## insert elem at index 0, returns None
list.extend(['yyy', 'zzz'])     ## add list of elems at end, returns None
print(list)                     ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print(list.index('curly'))      ## 2
list.remove('curly')            ## search and remove that element
list.pop(1)                     ## removes and returns 'larry', can remove any item with index
print(list)                     ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']

#List SLICE
#Slices work on lists just as with strings, and can also be used to change sub-parts of the list.
list = ['a', 'b', 'c', 'd']
print(list[1:-1])       ## ['b', 'c']
list[0:2] = 'z'         ## replace ['a', 'b'] with ['z']
print(list)             ## ['z', 'c', 'd']

# List with FOR
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum)  ## 30

# List with 'in'
list = ['larry', 'curly', 'moe']
if 'curly' in list:
    print('yay')

# Using RANGE print the numbers from 0 through 99
for i in range(100):
    print(i)

## Using WHILE to access every 3rd element in a list
a = [1, 2, 3, 4, 5, 6]
i = 0
while i < len(a):
    print(a[i])
    i = i + 3