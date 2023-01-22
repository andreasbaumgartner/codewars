
strng = "foobar910"


def increment_string(strng):
    if not strng:
        return '1'

    if strng[-1].isdigit():
        print(strng[-1])
        return strng[:-1] + str(int(strng[-1]) + 1)
    return strng + '1'


result = increment_string(strng)
print(result)
