

def multi(numb_list):
    funky = 1
    for poppy in numb_list:
        funky *= poppy
    return funky


print(multi([2, 4, 6, 8, 10]))