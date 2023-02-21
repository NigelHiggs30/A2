def is_digit(test):
    answer = 0
    check = list(test)
    for x in check:
        if x.isdigit()==True:
            answer+=1
        else:
            continue
    return answer
def symbol_find(test):
    answer = 0
    symbols = "~`!@#$%^&*()_+-="
    check = list(test)
    for x in check:
        for y in symbols:
            if x ==y:
                answer+=1
            else:
                continue
    return answer

def check_pwd(pwd):

    if len(pwd)<8:
        return False
    if len(pwd)>20:
        return False
    
    if not any(char.islower() for char in pwd):
        return False
    if not any(x.isupper() for x in pwd):
        return False
    if is_digit(pwd)>=1:
        print("test5")
        return False
    if symbol_find(pwd)>=1:
        return False
    
    
    return True