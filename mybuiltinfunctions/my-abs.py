# Return the absolute value of a number
import cmath

x=5
y=-5
z=complex(x,y)

if __name__ == "__main__":
    print(abs(3))
    print(x.__abs__())
    print(y.__abs__())
    print(z)
    #  For a complex number, the magnitude is returned
    print(z.__abs__())
    print(abs(z))
