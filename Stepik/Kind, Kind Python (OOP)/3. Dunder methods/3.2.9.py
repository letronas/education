class InputDigits:
    def __init__(self, func):
        self.__func = func
    
    def __call__(self, *args, **kwargs):
        return self.__func()


@InputDigits
def input_dg():
    return [int(i) for i in input().split()]


res = input_dg()
print(res)
