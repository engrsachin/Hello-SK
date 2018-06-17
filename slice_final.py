#!/usr/bin/python
def slice(string, start_index, end_index, step_value = 1):
    if step_value > 0:
        if end_index < 0:
            end_index += len(string)
        if start_index > end_index or start_index > len(string):
            return ''
        if end_index > len(string):
            end_index = len(string)
    elif step_value < 0:
        if start_index < 0:
            start_index += len(string)
        else:
            start_index -= 1
        if start_index < end_index or start_index > 0:
            return ''
        if start_index > len(string):
            start_index = len(string) - 1
    else:
        return ''
    result = ""
    while start_index != end_index:
        result += string[start_index]
        start_index += step_value
    return result

def main():
    #x = input("Enter String:")
    x = "Hello It's Fun"
    print("Expected : Hello It's Fun Result : %s"%(slice(x, 0, len(x))))
    print("Expected : llo Result : %s"%(slice(x, 2, 5)))
    print("Expected :  ol Result : %s"%(slice(x, 5, 2, -1)))
    print("Expected : nuF s'tI olle Result : %s"%(slice(x, len(x), 0, -1)))

    print("Expected : Hello It's Fun Result : %s"%(slice(x, 0, 100)))
    print("Expected : nuF s'tI lle Result : %s"%(slice(x, 100, 0, -1)))
    print("Expected :  Result : %s"%(slice(x, 100, 110, 1)))
    print("Expected :  Result : %s"%(slice(x, 110, 100, -1)))
    print("Expected :  Result : %s"%(slice(x, -100, 0, -1)))

if __name__ == "__main__":
    main()
