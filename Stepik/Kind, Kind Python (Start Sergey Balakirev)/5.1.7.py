i_start = 0  # начало
i_stop = 0  # конец замены
i = 0  # счетчик для движения
# '---some--words---that--i should repalce ------ to normal view --------'
some_string = input()
new_string = ''  # строка после замены
len_our_string = len(some_string)-1
while i <= len_our_string:
    if some_string[i] == '-' and (i != 0 and some_string[i - 1] != '-'):
        i_start = i
        i_stop = i
        if i == len_our_string and some_string[i-1] != '-': # когда строка закачивается, а до этого не было -
            i += 1  # чтобы не идти в следующую итерацию и закрыть цикл
            new_string += '-'
            
    elif some_string[i] == '-' and some_string[i-1] == '-':
        i_stop = i
        if i == len_our_string and some_string[i-1] == '-': # когда строка закачивается --
            i += 1  # чтобы не идти в следующую итерацию и закрыть цикл
            new_string += '-'

    elif i_stop != 0 and i_stop-i_start >= 1:
        new_string += '-' + some_string[i]
        i_start = 0
        i_stop = 0
    elif i_start == i_stop and i_stop != 0:  # специальный кейс на случай, если отступ всего один
        new_string += some_string[i-1] + some_string[i]
        i_start = 0
        i_stop = 0
    else:
        new_string += some_string[i]
        
        
    i += 1
    
print(new_string)