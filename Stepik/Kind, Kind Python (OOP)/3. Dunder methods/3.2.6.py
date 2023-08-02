class RenderList:
    
    def __init__(self, type_list):
        self.type_list = self.check_type(type_list)
    
    @staticmethod
    def check_type(value):
        return value if value in ('ul', 'ol') else 'ul'
    
    def __call__(self, in_lst):
        v_content = ''
        for i in in_lst:
            v_content += f'<li>{i}</li>\n'
        
        template = f'''<{self.type_list}>\n''' \
                   f'''{v_content}''' \
                   f'''</{self.type_list}>'''
        return template


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3", "Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("osas")
html = render(lst)
print(html)
