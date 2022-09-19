# prev, cur = 0, 1
# total = 0
# while True:
#     prev, cur = cur, prev + cur
#     if cur >= 4000000:
#         break
#     if cur % 2 == 0:
#         total += cur
# print(total)

limit = 4000000
sum = 0
a = 1
b = 1
while b < limit:

    if b % 2 == 0:
        sum += b
    h = a + b
    a, b = b, h

print(sum)
