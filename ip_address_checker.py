
strng = "123.122.12.23"


def is_valid_IP(strng):
    if strng.count('.') != 3:
        return False
    for i in strng.split('.'):
        if not i.isdigit() or (i[0] == '0' and len(i) > 1) or int(i) > 255:
            return False
    return True


result = is_valid_IP(strng)
print(result)
