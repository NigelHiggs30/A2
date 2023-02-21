def check_pwd(pwd):
    if len(pwd)<8:
        return False
    if len(pwd)>20:
        return False
    
    if not any(char.islower() for char in pwd):
        return False
    if not any(x.isupper() for x in pwd):
        return False

    return True