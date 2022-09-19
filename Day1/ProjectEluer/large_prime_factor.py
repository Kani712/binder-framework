i = 3
factor = []
number = 600851475143
while i * i <= number:
    if number % i != 0:
        i += 2
    else:
        number /= i
        factor.append(i)
while number >= i:
    if number % i != 0:
        i += 2
    else:
        number /= i
        factor.append(i)
print(max(factor))
