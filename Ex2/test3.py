"""
Convert Decimal number to octal using print() output formatting
Given: num = 8

Expected Output: The octal number of decimal number 8 is 10

"""


def decToOcta(deci):
    result = []
    resp = deci
    remdr = 1

    while resp != 0:
        remdr = resp / 8
        resp = resp % 8
        result.append(int(resp))
        resp = remdr
        if resp <= 8:
            print(resp)
            result.append(int(resp))
            result.reverse()
            result = "".join(str(x) for x in result)
            print(result)
            break


decToOcta(4636756756)
