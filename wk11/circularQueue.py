# circularQueue.py
# Author: Devun Durst

# The Circular Queue class provides users with a clear understanding
# of how to implement and utilize a circular queue data structure 
# in Python. Through its concise design and intuitive methods, users 
# learn about key queue operations like enqueue and dequeue, as well 
# as how circular indexing optimizes memory usage. By addressing 
# edge cases and providing feedback, such as when the queue is full 
# or empty, users gain insights into error handling and program flow.
# Overall, this class serves as a practical and educational tool 
# for users to grasp the concepts and applications of circular queues
# within their Python programs.


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.queue = [None] * self.capacity
        self.front_index = 0
        self.rear_index = 0
#------------------------------------------------------------------------
#------------------------------------------------------------------------
    def enqueue(self, data):
    # Enqueue:
    # Description: Adds an element to the rear of the circular queue.
    # Input: Data to be enqueued.
    # Output: None.
    # Behavior:
    # If the queue is full, print "Queue is full".
    # Otherwise, assign the provided data to the position indicated by rear_index in the queue.
    # Update rear_index to the next position using circular indexing.
        pass
#------------------------------------------------------------------------
#------------------------------------------------------------------------
    # Dequeue:
    def dequeue(self):
    # Description: Removes and returns the element from the front of the circular queue.
    # Input: None.
    # Output: Data dequeued from the queue.
    # Behavior:
    # If the queue is empty, print "Queue is empty" and return None.
    # Otherwise, retrieve the data from the position indicated by front_index in the queue.
    # Set the position indicated by front_index to None to indicate removal.
    # Update front_index to the next position using circular indexing.
    # Return the retrieved data. 
        pass
#------------------------------------------------------------------------
#------------------------------------------------------------------------
    # Size:
    def size(self):
    # Description: Computes and returns the current size of the circular queue.
    # Input: None.
    # Output: Current size of the circular queue.
    # Behavior:
    # Calculate the size of the queue using the formula (rear_index - front_index + capacity) % capacity.
    # Return the calculated size.
        pass
#------------------------------------------------------------------------
#------------------------------------------------------------------------
    # isEmpty:
    def isEmpty(self):
    # Description: Checks if the circular queue is empty.
    # Input: None.
    # Output: Boolean indicating whether the queue is empty.
    # Behavior:
    # Check if front_index and rear_index are equal and the element at front_index is None.
    # Return True if both conditions are met, otherwise return False.
        pass
#------------------------------------------------------------------------
#------------------------------------------------------------------------
    # isFull:
    def isFull(self):
    # Description: Checks if the circular queue is full.
    # Input: None.
    # Output: Boolean indicating whether the queue is full.
    # Behavior:
    # Check if the next position after rear_index using circular indexing is equal to front_index, and the element at front_index is not None.
    # Return True if both conditions are met, otherwise return False.
        pass
#------------------------------------------------------------------------
#------------------------------------------------------------------------
    # Front:
    def front(self):
    # Description: Retrieves the element at the front of the circular queue without removing it.
    # Input: None.
    # Output: Element at the front of the circular queue.
    # Behavior:
    # If the queue is empty, print "Queue is empty".
    # Otherwise, return the element at the position indicated by front_index in the queue.
        pass
#------------------------------------------------------------------------
#------------------------------------------------------------------------
    # Rear:
    def rear(self):
    # Description: Retrieves the element at the rear of the circular queue without removing it.
    # Input: None.
    # Output: Element at the rear of the circular queue.
    # Behavior:
    # If the queue is empty, print "Queue is empty".
    # Otherwise, return the element at the position indicated by (rear_index - 1 + capacity) % capacity in the queue.
        pass
#------------------------------------------------------------------------
#------------------------------------------------------------------------
    def printQueue(self):
        print(self.queue)

# Driver Code

print("Testing Circular Queue")
queue = CircularQueue(4)
queue.enqueue('5')
queue.enqueue('6')
queue.enqueue('3')
queue.enqueue('8')
queue.printQueue() # ['1', '2', '3', '4', None]
print("------------------------------------------------------------------------")
print("Testing size")
print(queue.size()) #Testing size: 4
print("------------------------------------------------------------------------")
print("Testing isEmpty")
print(queue.isEmpty()) #Testing isEmpty: False
print("------------------------------------------------------------------------")
print("Testing isFull")
print(queue.isFull()) #Testing isFull: True
print("------------------------------------------------------------------------")
print("Testing front")
print(queue.front()) # Testing front: 5
print("------------------------------------------------------------------------")
print("Testing rear")
print(queue.rear()) # Testing rear: 8
print("------------------------------------------------------------------------")
print("Testing dequeue")
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.printQueue() # [None, None, None, '8', None]