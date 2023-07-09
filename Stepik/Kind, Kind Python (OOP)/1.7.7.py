from string import ascii_lowercase, digits


class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    
    def __new__(cls, *args, **kwargs):
        # in case it's named use kwargs, else using index of input value
        if kwargs:
            cls.check_name(kwargs['name'])
        else:
            cls.check_name(args[0])
        return super().__new__(cls)
    
    def __init__(self, name, size: int = 10):
        self.name = name
        self.size = size
    
    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
    
    @classmethod
    def check_name(cls, name):
        ln_name = len(name)
        if ln_name > 50 or ln_name < 3 or any([i not in cls.CHARS_CORRECT for i in name]):
            raise ValueError("некорректное поле name")


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    
    def __new__(cls, *args, **kwargs):
        # in case it's named use kwargs, else using index of input value
        if kwargs:
            cls.check_name(kwargs['name'])
        else:
            cls.check_name(args[0])
        return super().__new__(cls)
    
    def __init__(self, name, size: int = 10):
        self.name = name
        self.size = size
    
    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
    
    @classmethod
    def check_name(cls, name):
        ln_name = len(name)
        if ln_name > 50 or ln_name < 3 or any([i not in cls.CHARS_CORRECT for i in name]):
            raise ValueError("некорректное поле name")


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw
    
    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
