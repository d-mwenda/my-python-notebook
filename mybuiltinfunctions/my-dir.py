"""
dir([object])
Without arguments, return the list of names in the current local scope. With an argument,
attempt to return a list of valid attributes for that object.
"""

class A:
    name = "Derick"
    age = 30

class Shape:
    def __dir__(self):
        return ['area', 'location', 'shape',]

def b():
    c = 1

if __name__ == "__main__":
    print("-------Calling dir with no arguments-------")
    print(dir())
    print("-------Calling dir on a class that does not implement the __dir__ method-------")
    print(dir(A))
    print("-------Calling dir on a class that implements the __dir__ method-------")
    s = Shape()
    print(dir(s))
    print("-------Calling dir on a function-------")
    print(dir(b))
    
