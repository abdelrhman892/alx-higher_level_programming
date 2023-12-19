#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    length = []
    list_length = my_list_1 if len(my_list_1) > len(my_list_2) \
        else my_list_2 if len(my_list_2) > len(my_list_1) \
        else my_list_1

    while i < len(list_length):
        try:
            length.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            length.append(0)
        except TypeError:
            print("wrong type")
            length.append(0)
        except IndexError:
            print("out of range")
            length.append(0)
        finally:
            h = 0
        i += 1
    return length
