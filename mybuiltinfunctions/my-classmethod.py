"""
Transform a method into a class method.
A class method receives the class as implicit first argument.
"""
class C:
    @classmethod
    def f(cls, arg1, arg2):
        return arg1 + arg2


class D:
    def f(arg1, arg2):
        return arg1 + arg2


if __name__ == "__main__":
    # Called on an instance of a class
    print(C().f(1, 2))
    # Called on a class
    print(C.f(4,6))
    # Called on a class
    print(D.f(4,6))
    # The following throws a type error as f is not a class method.
    print(D().f(1, 2))
