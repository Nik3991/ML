#1. Пользователь вводит целое число,
# программа складывает все цифры числа,
# с полученым числом - тоже самое и так до тех пор,
# пока не получится однозначное число.
# Пример:
# 545 -> 5
# 12345 -> 6

def task1():
    print("_____homework_2_1_____")
    value = int(input())
    result = value
    
    while len(str(result)) > 1:
        value = result
        result = 0
        while value != 0:
            digit = value % 10
            result += digit
            value //= 10

    print(result)


#2. Кинотеатр. Дан список списков, каждый вложенный список состоит из 1 и 0,
#   Количество вложенных списков - количество рядов.
#   Пользователь вводит сколько билетов ему требуется.
#   Программа должна найти ряд,
#   где можно приобрести нужно количество билетов (места должны быть рядом).
#   Если таких рядов несколько то ближайший к экрану (ближайшим считается нулевой ряд).
#   Ели таких мест нет, то вывести False
# Пример:
# [[0,1,1,0], [1, 0, 0, 0], [0,1,0,0]], 2 -> 1
# [[0,1,1,0], [1, 0, 1, 0], [1,1,0,1]], 2 -> False

import random

def generateLists(lists: list):
    countOfLists = random.randint(2,5)
    countOfItemsInList = random.randint(3,7)
    for _ in range(countOfLists):
        l = []
        for _ in range(countOfItemsInList):
            l.append(random.randint(0,1))
        print(l)
        lists.append(l)

def task2():
    print("_____homework_2_2_____")
    lists = []
    generateLists(lists)
    value = int(input())

    for l in lists:
        freePlaces = 0
        for v in l:
            if v == 0:
                freePlaces += 1
                if freePlaces == value:
                    print(True)
                    return
            else:
                freePlaces = 0
    print(False)

#3. Написать упрощенную версию алгоритма RLE.
# Алгоритм RLE объединяет подряд идущие символы в коэффициент и символ.
# Пример:
# aaabbbbccccc -> 2a4b5c
# asssdddsssddd -> 1a3s3d3s3d
# abcba -> 1a1b1c1b1a

def task3():
    print("_____homework_2_3_____")
    value = input()
    value += '_'
    result = ''

    current = value[0]
    count = 1
    size = len(value)
    for index in range(1, size):
        if current != value[index]:
            result += str(count)
            result += current
            count = 1
            current = value[index]
        else:
            count += 1
            
    print(result)


#4. Шифр Цезаря. Пользователь вводит строку и ключ шифра,
#   программа должна вывести зашфированную строку (со сдвигом по ключу).
#   Сдвиг циклический. Используем только латинский алфавит, пробелы не шифруются.
#   Пример:
#   Dog, 2 -> Fqi
#   Zak zak -> Cdn cdn
#   Python is the BEST -> Udymts nx ymj GJXY

def cesar():
    print("_____homework_2_4_____")
    result_list = []

    word = input("type word: ")
    key  = int(input("type key: "))
    
    for c in word:
        if c == ' ':
            result_list.append(' ')
            continue
        
        start = ord('a') if ord(c) >= ord('a') else ord('A')
        number_in_alph = ord(c) - start
        shifted_number = (number_in_alph + key) % 26
        result_list.append(chr(start + shifted_number))

    print(''.join(result_list))

#5. Табель успеваемости.
#   Пользователь в бесконечном цикле (пока не будет введена пустая строка)
#   вводит строки вида: 'название предмета' 'фамилия ученика' 'оценка'.
#   После окончания ввода программа выводит в консоль Название предмета,
#   далее список учеников и все их оценки в виде таблицы

def task5():
    print("_____homework_2_5_____")
    items = dict()

    value = input(':')
    while value:
        data = value.split()

        if len(data) != 3:
            print('incorrect data')
            continue

        if data[0] in items:
            if data[1] in items[data[0]]:
                items[data[0]][data[1]].append(data[2])
            else:
                items[data[0]][data[1]] = [data[2]]
        else:
            items[data[0]] = {data[1]:[data[2]]}
        
        value = input(':')

    for item in items.keys():
        print('item: ', item)
        for person in items[item].keys():
            print("  ", person, ' '.join(items[item][person]))
        print()
    
if __name__ == "__main__":
    task1()
    task2()
    task3()
    cesar()
    task5()
