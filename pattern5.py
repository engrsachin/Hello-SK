#!usr/bin/python
#Character Pattern

def alphapat(n):
     
    # initializing value corresponding to 'A' 
    # ASCII value
    num = 65
 
    for i in range(0, n):
        for j in range(0, i+1):
            # explicitely converting to char
            ch = chr(num)

            print(ch, end=" ")

        num = num + 1

        print("\r")
 
if __name__ == '__main__':
    n = eval(input('Enter number of rows: '))
    alphapat(n)
