from models import TodoModel

class TodoService:
    def __init__(self):
        self.model = TodoModel()

    def create(self, params):
        return self.model.create(params['text'], params['description'])
    
    def read(self, params):
        return self.model.read(params['item_id'])