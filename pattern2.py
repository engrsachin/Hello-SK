#!usr/bin/python
#Simple pyramid pattern - mirror image
def pattern2(n):
    k = 2*n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")

if __name__ == '__main__':
    n = eval(input('Enter number of rows: '))
    pattern2(n)