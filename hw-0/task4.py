
"""
Шифр Цезаря. Написать функцию, которая будет принимать два аргумента:
слово (str) и ключ (int). Результат выполнения функции - шифрованое слово по методоту Шифр Цезаря.
Написать вторую функцию, которая будет проводить обратный процесс
(или написать одну, выполняющую оба действия)
'dog', 3 -> 'grj', 'python', 5 -> 'udymts'
"""


def cesar(word: str, key: int, encrypt: bool):
    result_list = []
    for c in word:
        number_in_alph = ord(c) - ord('a')
        shifted_number = (number_in_alph + (key if encrypt else -key)) % 26
        result_list.append(chr(ord('a') + shifted_number))

    return ''.join(result_list)


if __name__ == '__main__':
    print('--------------------- Test -----------------------')
    word = "abcdwxyz"
    encrypted_str = cesar(word, 33, True)
    decrypted_str = cesar(encrypted_str, 33, False)

    print("word to encrypt =", word)
    print("encrypted =", encrypted_str)
    print("decrypted =", decrypted_str)
    print('--------------------------------------------')
