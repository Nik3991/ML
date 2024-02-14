
""""
Написать функцию, которая принимает на вход квадратное уравнение
(одной строкой) и возвращает его корни, либо сообщает, что их нет
"x**2 - 11*x + 28 = 0" -> x_1 = 4, x_2 = 7
"""
import math


def get_digit_part_as_int(l: list):
    result_list = []
    negative = False

    # check if number should be negative
    if l[0] == '-':
        negative = True
        l = l[1:]

    for i in l:
        if i.isdigit():
            result_list.append(i)
        else:
            break

    result = 0
    if result_list:
        result = int(''.join(result_list))
        if negative:
            result *= -1
    else:
        result = -1 if negative else 1

    return result


def get_part(part: list, s: str):
    if s[0] == '-':
        part.append('-')
        s = s[1:].strip()

    for i in range(len(s)):
        if s[i] in '+-=':
            s = s[i + (0 if s[i] == '-' else 1):]
            break
        elif s[i] == ' ':
            pass
        else:
            part.append(s[i])

    return s.strip()


def square_equation(s: str):
    a_part = []
    s = get_part(a_part, s)

    b_part = []
    if 'x' in s:  # b != 0
        s = get_part(b_part, s)
    else:
        b_part.append('0')

    c_part = []
    if s[0] != '=':  # c != 0
        s = get_part(c_part, s)
    else:
        c_part.append('0')

    a = get_digit_part_as_int(a_part)
    b = get_digit_part_as_int(b_part)
    c = get_digit_part_as_int(c_part)

    d = (b**2) - (4*a*c)

    if d < 0:
        print("D < 0, no answer!")
    elif d == 0:
        x = -b / (2 * a)
        print("D == 0, x =", x)
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("D > 0, x1 =", x1, 'x2 =', x2)


if __name__ == "__main__":
    print('-------------------- Test --------------------')
    square_equation("x**2 - 11*x + 28 = 0")
    square_equation("10*x**2 - 5*x + 28 = 0")
    square_equation("10*x**2 + 28 = 0")
    square_equation("10*x**2 - 5*x = 0")
    square_equation("10*x**2 + x = 0")
    square_equation("10*x**2 + x + 1 = 0")
    square_equation("x**2 + 1 = 0")
    square_equation("x**2 + x = 0")
    square_equation("x**2 + x + 10 = 0")
    square_equation("x**2 + 2*x = 0")
    print('--------------------------------------------')