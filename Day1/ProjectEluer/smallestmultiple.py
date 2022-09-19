check = range(10, 21)
a = 21
b = False

while b == False:
    if a % 2520 == 0:
        if all(a % n == 0 for n in check):
            b = True
        else:
            a = a + 2520
    else:
        a = a + 1
print(a)
