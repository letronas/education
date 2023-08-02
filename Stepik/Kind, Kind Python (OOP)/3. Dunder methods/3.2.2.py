from random import randint, choices


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length
    
    def __call__(self, *args, **kwargs):
        pass_len = randint(self.min_length, self.max_length)
        return ''.join(choices(self.psw_chars, k=pass_len))


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd() for _ in range(3)]


#
# # Soludion with decorator inside
# from random import randint, choices
#
#
# class RandomPassword:
#     def __init__(self, psw_chars, min_length, max_length):
#         self.psw_chars = psw_chars
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def __call__(self, func):
#         def __func():
#             res = func(self.psw_chars, self.min_length, self.max_length)
#             return res
#         return __func
#
#
# min_length = 5
# max_length = 20
# psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
#
#
# @RandomPassword(psw_chars, min_length, max_length)
# def generate_password(psw_chars, min_length, max_length):
#     pass_len = randint(min_length, max_length)
#     return ''.join(choices(psw_chars, k=pass_len))
#
#
# rnd = RandomPassword(psw_chars, min_length, max_length)
# lst_pass = [generate_password() for _ in range(3)]
# print(lst_pass)
# # for i in range(1000):
# #     psw = rnd()
# #     print(psw)
