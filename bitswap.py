#!usr/bin/python

def SwapBits(x,y,pos1,pos2,NoOfBits):
    x_mask = (1 << NoOfBits) - 1
    x_mask = x_mask << (pos1 - NoOfBits)
    x_part = x & x_mask
    x = x & (~x_mask)

    y_mask = (1 << NoOfBits) - 1
    y_mask = y_mask << (pos2 - NoOfBits)
    y_part = y & y_mask
    y = y & (~y_mask)

    if (pos1 - pos2) > 0:
        x_part = x_part >> (pos1 - pos2)
        y_part = y_part << (pos1 - pos2)
    else:
        x_part = x_part << (pos2 - pos1)
        y_part = y_part >> (pos2 - pos1)
    x = x | y_part
    y = y | x_part
    return x,y




'''if __name__ == '__main__':
    x = 869
    y = 1112
    pos1 = 11
    pos2 = 7
    NoOfBits = 3
    print(SwapBits(x,y,pos1,pos2,NoOfBits))'''

if __name__ == '__main__':
    x = eval(input("Enter Value x : " ))
    y = eval(input("Enter Value y : " ))
    pos1 = eval(input("Enter Value pos1 : " ))
    pos2 = eval(input("Enter Value pos2 : " ))
    NoOfBits = eval(input("Enter Value NoOfBits : " ))
    print(SwapBits(x,y,pos1,pos2,NoOfBits))