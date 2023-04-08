
cache_dict = {}
while (some_val := int(input())) != 0:
    if some_val in cache_dict:
        print('значение из кэша: ' + str(cache_dict[some_val]))
    else:
        new_val = round(pow(some_val, .5), 2)
        print(new_val)
        cache_dict[some_val] = new_val

