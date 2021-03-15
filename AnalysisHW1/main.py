"""
Assignment 1
name: sergey pechyoni
ID: 320734304
"""
import sys


def main():
    print("the wrong number is : ", abs(3.0*(4.0/3.0-1)-1))
    print("the correct number is : ", abs(3.0*(4.0/3.0-1)-1)-sys.float_info.epsilon)
    print("the epsilon representing the machine precision is:", sys.float_info.epsilon)
    pass


if __name__ == '__main__':
    main()