#How to implement a circular queue in Python
#https://www.geeksforgeeks.org/circular-queue-set-1-introduction-and-array-implementation/
#
# step 1: create a class
# step 2: create a constructor
# step 3: create a enqueue method
# step 4: create a dequeue method
# step 5: create a front method
# step 6: create a rear method
# step 7: create a isEmpty method
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.queue = [None] * self.capacity
        self.front_index = 0
        self.rear_index = 0

    def enqueue(self, data):
        if self.isFull():
            print("Queue is full")
        else:
            self.queue[self.rear_index] = data
            self.rear_index = (self.rear_index + 1) % self.capacity

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            data = self.queue[self.front_index]
            self.queue[self.front_index] = None  # Reset the dequeued element to None
            self.front_index = (self.front_index + 1) % self.capacity
            return data

    def size(self):
        return (self.rear_index - self.front_index + self.capacity) % self.capacity

    def isEmpty(self):
        return self.front_index == self.rear_index and self.queue[self.front_index] is None

    def isFull(self):
        return (self.rear_index + 1) % self.capacity == self.front_index and self.queue[self.front_index] is not None

    def front(self):
        if self.front_index == self.rear_index:
            print("Queue is empty")
        else:
            return self.queue[self.front_index]

    def rear(self):
        if self.front_index == self.rear_index:
            print("Queue is empty")
        else:
            return self.queue[(self.rear_index - 1 + self.capacity) % self.capacity]

    def printQueue(self):
        print(self.queue)

# Driver Code

print("Testing Circular Queue")
queue = CircularQueue(5)
queue.enqueue('5')
queue.enqueue('6')
queue.enqueue('3')
queue.enqueue('8')
queue.printQueue()
print("------------------------------------------------------------------------")
print("Testing size")
print(queue.size())
print("------------------------------------------------------------------------")
print("Testing isEmpty")
print(queue.isEmpty())
print("------------------------------------------------------------------------")
print("Testing isFull")
print(queue.isFull())
print("------------------------------------------------------------------------")
print("Testing front")
print(queue.front())
print("------------------------------------------------------------------------")
print("Testing rear")
print(queue.rear())
print("------------------------------------------------------------------------")
print("Testing dequeue")
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.printQueue()