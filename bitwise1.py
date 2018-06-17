#!usr/bin/python

def CountOneBit(no):
    x = 1
    y = -1
    count = 0
    while y & no != 0:
        if(x & no) !=0:
            count += 1
        x = 1 << (pos - 1)  # left shift by 1
        x = ~x #compliment of x

    return no & x


if __name__ == '__main__':
    no = eval(input ("Enter Num :  "))
    print(CountOneBit(no))
