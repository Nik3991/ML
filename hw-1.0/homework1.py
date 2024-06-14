#1. Пользователь вводит пятизначное число.
# Программа должна зеркально отразить центральные три цифры.
# Первая и последняя остаются на местах.
# Пример:
# 23456 -> 25436
# 30789 -> 38709

def task1():
    print('_____homework_1_task_1_____')
    value = list(str(input()))
    l = len(value)

    if l > 2:
        mid = l // 2
        tmp = value[mid - 1]
        value[mid - 1] = value[mid + 1]
        value[mid + 1] = tmp
        print(''.join(value))
    else:
        print('input should have at least 3 digits')


#2. Отпуск.
# Пользователь вводит сколько дней осталось до ближайшего отпуска.
# Программа должна вывести количество выходных дней до отпуска,
# если учесть что выходные это суббота и воскресенье,
# сегодня понедельник и праздники мы не учитываем.
# Пример:
# 4 -> 0
# 6 -> 1
# 14 -> 4

def task2():
    print('_____homework_1_task_2_____')
    days = int(input())
    if days <= 5:
        print(0)
    else:
        print(days % 5)

#3. Пользователь вводит длинну и ширину плитки шоколада,
# а так же размер куска, который хочет отломить,
# программа должна вычислить - можно ли совершить подобный разлом или нет,
# если учесть, что ломать можно только по прямой
# Пример:
# 3, 4, 6 -> True
# 5, 7, 8 -> False
# 4, 5, 12 -> True

def task3():
    print('_____homework_1_task_3_____')
    h = int(input())
    w = int(input())
    r = int(input())
    print(h * w >= r and (r % h == 0 or r % w == 0))    


#4. Пользователь вводит целое положительное число,
#    программа должна вернуть строку в виде римского числа
#   Пример:
#   3 -> III
#   15 -> XV
#   234 -> CCXXXIV
roman_numbers = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
                 ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
                 ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

def task4():
    print('_____homework_1_task_4_____')
    num = int(input())
    result = ''
    for (key, value) in roman_numbers:
        while num >= value:
            result += key
            num -= value
            
    print(result)

#5. Пользователь вводит данные,
#   проверить - являються ли они положительным вещественным числом.
#   Не использовать встроенные функции для проверки,
#   только методы данных и конструкцию IF.
#   (Дополнительное задание, по желанию - проверка на отрицательные вещественные числа)
# Пример:
# 5.6 -> True
# .78 -> True
# .67. -> False
# 5 -> True

digits = {'0','1','2','3','4','5','6','7','8','9'}

def task5():
    print('_____homework_1_task_5_____')
    value = input()
    dots = 0
    result = True
    for c in value:
        if c == '.':
            if dots == 1:
                result = False
                break
            else:
                dots += 1
        elif c not in digits:
            result = False
            break
        
    print(result)

if __name__ == '__main__':
    task1()
    task2()
    task3()
    task4()
    task5()
