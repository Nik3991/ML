"""
Вводится целое число (любого размера).
Написать функцию, которая разобьет это число на разряды символом "пробел",
Функция возвращает тип данных str
Описание/Пошаговая инструкция выполнения домашнего задания:
1234567 -> 1 234 567, 267 -> 267, 34976 -> 34 976`
"""

def splitter(num: int):
    converted = list(str(num))
    converted.reverse()
    result_list = list()

    counter = 0
    for n in converted:
        if counter % 3 == 0:
            result_list.append(' ')

        result_list.append(n)
        counter += 1

    result_list.reverse()
    return ''.join(result_list)


if __name__ == "__main__":
    print(splitter(10))
    print(splitter(100))
    print(splitter(1000))
    print(splitter(10000))
    print(splitter(100000))
    print(splitter(1000000))
    print(splitter(10000000))
    print(splitter(100000000))
    print(splitter(1000000000))
    print('\n')