class DigitRetrieve:
    
    def __call__(self, var: str):
        try:
            return int(var)
        except ValueError:
            return None


dg = DigitRetrieve()

st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)
