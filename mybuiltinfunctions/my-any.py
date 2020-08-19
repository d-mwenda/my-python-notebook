# Takes an iterable and returns True if any of the elements in the iterable is true.


list_1 = [1, 2, 3, 4]
list_2 = [0, 1, 2, 3, 4]
list_3 = [1, 'two', 3, 'four']
list_4 = []
list_5 = ['',]

tuple_1 = (1, 2 ,3, 4)
tuple_2 = (0, 1, 2 ,3, 4)
tuple_3 = (0, 1, 'two', 3, 'four')
tuple_4 = ()
tuple_5 = ('',)

dict_1 = {'one' :1, 'two': 2, 'three': 3, 'four': 4}
dict_2 = {'zero':0, 'one': 1, 'two': 2, 'three': 3, 'four': 4}
dict_3 = {}

if __name__ == "__main__":
    print(list_1, 'is: ', any(list_1))
    print(list_2, "is: ", any(list_2))
    print(list_3, "is: ", any(list_3))
    print(list_4, "is: ", any(list_4))
    print(list_5, "is: ", any(list_5))

    print(tuple_1, "is: ", any(tuple_1))
    print(tuple_2, "is: ", any(tuple_2))
    print(tuple_3, "is: ", any(tuple_3))
    print(tuple_4, "is: ", any(tuple_4))
    print(tuple_5, "is: ", any(tuple_5))

    print(dict_1, "is: ", any(dict_1))
    print(dict_2, "is: ", any(dict_2))
    print(dict_3, "is: ", any(dict_3))
    # Observation: An empty iterable always returns false
