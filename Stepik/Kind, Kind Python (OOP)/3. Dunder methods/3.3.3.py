class Model:
    
    def __init__(self):
        self.model = None
    
    def query(self, **kwargs):
        self.model = kwargs
    
    def __str__(self):
        if self.model:
            return f"Model: {', '.join(f'{keys} = {items}' for keys, items in self.model.items())}"
        else:
            return f"Model"


model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)
