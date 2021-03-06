
def dicDemo():
    ## Can build up a dict by starting with the the empty dict {}
    ## and storing key/value pairs into the dict like this:
    ## dict[key] = value-for-that-key
    dict = {}
    dict['a'] = 'alpha'
    dict['g'] = 'gamma'
    dict['o'] = 'omega'

    print(dict)                 ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
    print(dict['a'])            ## Simple lookup, returns 'alpha'
    dict['a'] = 6               ## Put new key/value into dict
    print('a' in dict)          ## True
    # print(dict['z'])           ## Throws KeyError, KeyError: 'z'


    if 'z' in dict:
        print(dict['z'])        ## Check to avoid KeyError
    else:
        print("z is not in dict")

    print(dict.get('z')== None) ## None (instead of KeyError), different check


    ## By default, iterating over a dict iterates over its keys.
    ## Note that the keys are in a random order.
    for key in dict:
        print(key)    ## prints a g o

    ## Exactly the same as above
    for key in dict.keys():
        print(key)

    ## Get the .keys() list:
    print(dict.keys())              ## ['a', 'g', 'o']

    ## Likewise, there's a .values() list of values
    print(dict.values())            ## ['alpha', 'omega', 'gamma']

    ## Common case -- loop over the keys in sorted order,
    ## accessing each key/value
    for key in sorted(dict.keys()):
        print(key, dict[key])

    ## .items() is the dict expressed as (key, value) tuples
    print(dict.items())             ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

    ## This loop syntax accesses the whole dict by looping
    ## over the .items() tuple list, accessing one (key, value)
    ## pair on each iteration.
    for k, v in dict.items():
        print(k, '>', v)

    # Delete items
    dict = {'a':1, 'b':2, 'c':3}
    del dict['b']       ## Delete 'b' entry
    print(dict)         ## {'a':1, 'c':3}
dicDemo()