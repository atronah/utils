import sys


snils = sys.argv[1] if len(sys.argv) > 1 else '45454545499'
snils = ''.join([d for d in snils if d.isdigit()])

result, error = True, ''

"""
Проверка контрольного числа Страхового номера проводится только для номеров больше номера 001-001-998.

Контрольное число Страхового номера рассчитывается следующим образом:
- каждая цифра Страхового номера умножается на номер своей позиции (позиции отсчитываются с конца)
- полученные произведения суммируются
- сумма делится на 101
- последние две цифры остатка от деления являются Контрольным числом.
Например: Указан страховой номер 112-233-445 95
Проверяем правильность контрольного числа:
"""

total = 0
previous_digit = None
repeting_count = 0
for idx, digit in enumerate(snils[-3::-1]):
    total += int(digit) * (idx + 1)

    repeting_count = 0 if digit != previous_digit else (repeting_count + 1)
    if repeting_count > 2:
        result, error = False, f'digit {digit} appears more than 2 times in a row: {repeting_count} times'

    previous_digit = digit

checksum = str(total % 101)[-2:]

if checksum != snils[-2:]:
    result, error = False, f'incorrect checksum, must be "{checksum}" insted of {snils[-2:]}'

print(f'for "{snils}" result is {"ok" if result else "error: " + error}')