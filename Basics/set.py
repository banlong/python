# A set is an unordered “bag” of unique values. A single set can contain values of any immutable datatype.
# Once you have two sets, you can do standard set operations like union, intersection, and set difference.

# To create an empty set, call set() with no arguments.
a_set = set()
print('a_set = ',a_set)
print('type(a_set) = ', type(a_set))
print('len(a_set) = ', len(a_set))
not_sure = {}
print('not_sure = {}')
print('type(not_sure) = ', type(not_sure))

# To create a set with multiple values, separate the values with commas and wrap it all up with curly brackets.
a_set = {1, 2}
a_set.add(4)
print(a_set)
print(len(a_set))
# Duplicate value is ignored
a_set.add(1)
print(a_set)
print(len(a_set))

# You can also create a set out of a list.
a_list = ['a', 'b', 'b', 'mpilgrim', True, False, 42]
a_set = set(a_list)
print(a_set)
print(len(a_set))
print(a_list)

# 1. To test whether a value is a member of a set, use the in operator. This works the same as lists.
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
print(30 in a_set)
print(31 in a_set)

# 2. The union() method returns a new set containing all the elements that are in either set.
print(a_set.union(b_set))

# 3. The intersection() method returns a new set containing all the elements that are in both sets.
print(a_set.intersection(b_set))

# 4. The difference() method returns a new set containing all the elements that are in a_set but not b_set.
print(a_set.difference(b_set))

# 5. The symmetric_difference() method returns a new set containing all the elements that are in exactly one of the sets.
print(a_set.symmetric_difference(b_set))

# 6. In a boolean context, an empty set is false. Any set with at least one item is true.
#    Any set with at least one item is true. The value of the items is irrelevant.
def is_it_true(anything):
    if anything:
        print("yes, it's true")
    else:
        print("no, it's false")

print(is_it_true(set()))
print(is_it_true({'a'}))
print(is_it_true({False}))






