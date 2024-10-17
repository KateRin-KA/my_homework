import random
def password():
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = list(range(3, 21))
    password = random.choice(numbers)
    return password
print(password())
n = password()
print('Число из первой вставки   :', n)
pairs_of_numbers = list(range(1, n))
pairs_of_numbers1 = list(range(1, n))
pairs = []
result = ''
for i in pairs_of_numbers:
    for j in pairs_of_numbers1:
        p = i
        p1 = j
        if p >= p1:
            continue
        else:
            multiple = n % (p + p1)
            if multiple == 0:
                pairs.append([p, p1])
                result = result + str(p) + str(p1)
print(*pairs)
print('Пароль', result)
