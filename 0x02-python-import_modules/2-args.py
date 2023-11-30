#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    arguments = len(sys.argv) - 1
    num = 1
    if arguments != 0:
        print("{} arguments:".format(arguments))
        for i in range (arguments):
            print("{}: {}".format(num, sys.argv[i + 1]))
            num += 1
    elif arguments == 0:
        print("0 arguments.")
