greeting = "Hello world"

def trim(sourceStr):
    space = ' '
    tab = '\t'
    resultStr = ''

    inWordLeft = False
    inWordRight = False

    strLength = len(sourceStr)
    i = 0
    j = strLength - 1

    while i < strLength:
        if (sourceStr[i] != space) and (sourceStr[i] != tab):
            inWordLeft = True

        if (sourceStr[j] != space) and (sourceStr[j] != tab):
            inWordRight = True

        if inWordLeft and inWordRight:
            break
        else:
            if not inWordLeft:
                i = i + 1

            if not inWordRight:
                j = j - 1

    while i <= j:
        resultStr = resultStr + sourceStr[i]
        i = i + 1

    return resultStr

print(trim("  Hello World     "))
