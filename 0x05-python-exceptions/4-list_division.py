#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    list_length = []
    length = list_length
    
    massage, theCase = ("out of range", my_list_1) if len(my_list_1) > len(my_list_2) \
        else ("out of range", my_list_2) if len(my_list_2) > len(my_list_1) \
        else ("", my_list_1 or my_list_2)

    while i < len(theCase):
        if theCase == my_list_1 and i == len(theCase) - 1 and len(my_list_1) > len(my_list_2):
            print(massage)
            list_length.append(0)

        elif theCase == my_list_2 and i == len(theCase) - 1 and len(my_list_2) > len(my_list_1):
            print(massage)
            list_length.append(0)
        
        else:
            try:
                list_length.append(my_list_1[i] / my_list_2[i])
            
            except ZeroDivisionError:
                print("division by 0")
                list_length.append(0)
            
            except TypeError:
                print("wrong type")
                list_length.append(0)
            
            finally:
                h = 0
        i += 1

    return length
