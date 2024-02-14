"""
Написать функцию, которая заменяет принимает строку текста и
изменяет снейк_кейс на КамелКейси наоборот
my_first_func -> MyFirstFunc, AnotherFunction -> nother_function
"""


def replace_snake(s: str):
    result_list = []
    upper_case = True

    for i in range(len(s)):
        if s[i] == '_':
            upper_case = True
        elif s[i].isupper():
            result_list.append('_' if i != 0 else '')
            result_list.append(s[i].lower())
            upper_case = False
        else:
            result_list.append(s[i].upper() if upper_case else s[i])
            upper_case = False

    return ''.join(result_list)

if __name__ == '__main__':
    print('-------------------- Test --------------------')
    print(replace_snake('first_test_string'))
    print(replace_snake('second_test_string_'))
    print(replace_snake('third_test_strin_g'))
    print(replace_snake('_fourth_test_string'))
    print(replace_snake('_f_i_f_t_h_t_e_s_t_s_t_r_i_n_g_'))
    print(replace_snake('FirstTestString'))
    print(replace_snake('SecondTestString_'))
    print(replace_snake('Third_Test_String'))
    print(replace_snake('FOURTHTESTSTRING'))
    print('---------------------------------------------')
    print('\n')
