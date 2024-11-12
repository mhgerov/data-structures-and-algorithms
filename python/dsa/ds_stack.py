class Stack:
    def __init__(self):
        self.data = []

    def push(self,obj):
        self.data.append(obj)

    def pop(self):
        # There is already a pop function for lists, but this is more verbose
        element = self.data[-1]
        del self.data[-1]
        return element
    
    def read(self):
        return self.data[-1]