#!/usr/bin/python
import sys

#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])
        x1, x2 = find_roots(a, b, c)
        print ("This is x1: %f" %x1)
        print ("This is x2: %f" %x2)
    except ZeroDivisionError:
        print("Leading coefficient cannot be 0.")
    except TypeError:
        print("Sorry, imaginary roots.")
    except ValueError:
        print("Only numerical input is allowed.")


def find_roots(a,b,c):
    mid = b**2 - 4*a*c
    sqrt_mid = mid**(1/2)
    x1 = (-b + sqrt_mid)/(2*a)
    x2 = (-b - sqrt_mid)/(2*a)
    return x1, x2


if __name__=="__main__":
        main()
