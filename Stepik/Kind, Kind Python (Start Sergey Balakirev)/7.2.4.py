
def is_even(in_num: int) -> bool:
    return True if in_num % 2 == 0 else False


while (i_value := int(input())) != 1:
    print(i_value) if is_even(i_value) else 'Не выводим ничего'

