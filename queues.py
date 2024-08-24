class Queues:
    def __init__(self) -> None:
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        return self.items.popleft()
    