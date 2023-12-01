#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    arguments = len(sys.argv) - 1
    sum = 0
    for i in range (arguments):
        sum += int(sys.argv[i + 1])
    print(sum)
