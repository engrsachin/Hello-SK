#!usr/bin/python
# To demonstrate star pattern
#Simple pyramid pattern
def pattern1(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")
if __name__ == '__main__':
    n = eval(input('Enter number of rows: '))
    pattern1(n)
