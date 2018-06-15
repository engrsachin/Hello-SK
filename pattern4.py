#!usr/bin/python

#Number Pattern
def pattern4(n):
    num = 1
    for i in range(0, n):
        num = 1
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")
if __name__ == '__main__':
    n = eval(input('Enter number of rows: '))
    pattern4(n)
