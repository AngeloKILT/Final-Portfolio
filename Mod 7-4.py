
def rare_list(num_list):
    dumb_list = []
    for kite in num_list:
        if kite not in dumb_list:
            dumb_list.append(kite)
    return dumb_list


print(rare_list([1, 3, 1, 6, 2]))
