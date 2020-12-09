n = int(input('Введите число: '))
summ = 0
mult = 1

while n > 0:
    digit = n % 10
    summ += digit
    mult = mult * digit
    n = n // 10
print(summ)
print(mult)