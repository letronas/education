from string import ascii_lowercase, digits


class LengthValidator:
    """Для проверки длины данных в диапазоне [min_length; max_length]"""
    
    def __init__(self, min_length, max_length):
        self.min_length = min_length  # минимально допустимая длина
        self.max_length = max_length  # максимально допустимая длина
    
    def __call__(self, value):
        return self.min_length <= len(value) <= self.max_length


class CharsValidator:
    """Для проверки допустимых символов в строке."""
    
    def __init__(self, chars):
        self.chars = set(chars.lower())  # строка из допустимых символов, которую легче сделать сразу set
    
    def __call__(self, value):
        return set(value) <= self.chars


class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""
    
    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")
    
    def is_validate(self):
        if not self.validators:
            return True
        
        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False
        
        return True
