class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        else:
            return super().__new__(cls, lst)
    
    def __str__(self):
        return ' '.join(map(str, self))
    
    def __repr__(self):
        return ' '.join(map(str, self))


try:
    digits = list(map(float, input().split()))
    new_obj = TupleLimit(digits, 5)
except ValueError as vr:
    print(vr)
else:
    print(new_obj)
