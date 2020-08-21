"""
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
Create a new dictionary.
"""
name = dict(first_name= "Derick", last_name = "Mwenda")
name1 = dict(first_name= "Derick", last_name = "Mwenda")


if __name__ == "__main__":
    print(type(name))
    for (key, value) in name.items():
        print("{key} is {value}".format(key=key, value=value))
    # delattr(name, "first_name")
    # for (key, value) in name.items():
#         print("Python says: {err}".format(attrerr))
