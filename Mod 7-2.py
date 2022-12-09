

def check_number(shoot):
    if shoot > 10:
        return False
    elif shoot < 1:
        return False
    else:
        return True


dookie = int(input("Input a number"))
answer = check_number(dookie)
print(answer)

