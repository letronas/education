class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods
    
    def get(self, request):
        return ""
    
    def post(self, request):
        pass
    
    def put(self, request):
        pass
    
    def delete(self, request):
        pass


class DetailView(GenericView):
    def render_request(self, request, method):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        else:
            if method == 'GET':
                res = self.get(request)
            elif method == 'POST':
                res = self.post(request)
            elif method == 'PUT':
                res = self.put(request)
            elif method == 'delete':
                res = self.delete(request)
            else:
                res = ''  # но вообще лучше тут ошибка или еще что-то
            return res
    
    def get(self, request: dict):
        if type(request) != dict or 'url' not in request.keys():
            raise TypeError('request не содержит обязательного ключа url')
        else:
            return f"url: {request['url']}"


# dv = DetailView()
# html = dv.render_request({'url2': 'https://site.ru/home'}, 'GET')  # url: https://site.ru/home
#
# print(html)


