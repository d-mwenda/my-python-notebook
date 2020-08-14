# Takes an iterable and returns True if all elements in the iterable are true or if the iterable is empty

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
dict_5 = {}

if __name__ == "__main__":
    print(all(list_1))
    print(all(list_2))
    print(all(list_3))
    print(all(list_4))
    print(all(list_5))


