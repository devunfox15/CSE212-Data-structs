def __init__(self, capacity):
        self.capacity = capacity 
        self.queue = [None] * self.capacity
        self.front_index = 0
        self.rear_index = 0