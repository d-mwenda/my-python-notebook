"""
Return True if the object argument appears callable, False if not. 
"""

name = "Derick Mwenda"

def my_name():
    return "Derick Mwenda"

class MyName:
    pass

if __name__ == "__main__":
    print(callable(name))
    print(callable(my_name))
    print(callable(MyName))
    