myUniqueList = []


def add(value):
    if value in myUniqueList:
        return False
    else:
        myUniqueList.append(value)
        return True


print(add('ding'))
print(myUniqueList)
print(add('ding'))
print(myUniqueList)
print(add('dong'))
print(myUniqueList)
print(add('ping'))
print(myUniqueList)
print(add('dong'))
print(myUniqueList)
