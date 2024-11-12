class Queue:
    def __init__(self):
        self.data = []

    def push(self,obj):
        self.data.append(obj)

    def pop(self):
        element = self.data[0]
        del self.data[0]
        return element
    
    def read(self):
        return self.data[0]