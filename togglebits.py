#!usr/bin/python

# Function to turn off bits from nth position
def ToggleBits(no, pos, noofbits):
    x = (1 << noofbits) - 1
    x = x << (pos - noofbits)
    #x = ~x
    return no^x

if __name__ == '__main__':
    no = eval(input ("Enter Number :  "))
    pos = eval(input("Enter Position:  "))
    noofbits = eval(input("Enter no of bits to turn off from given position: "))
    result = ToggleBits(no, pos, noofbits)
    print("Result= %d" %result)
    print(bin(no))