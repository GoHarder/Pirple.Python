a1 = 1
b1 = 1
c1 = 2

a2 = 1
b2 = 2
c2 = 3


def eq(var1, var2, var3):
    output = False
    if var1 == var2 or var1 == var3:
        output = True

    return output


print(eq(a1, b1, c1))
print(eq(a2, b2, c2))
