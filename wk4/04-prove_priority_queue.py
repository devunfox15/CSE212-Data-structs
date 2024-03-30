"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Priority_Queue:
    """
    This queue follows the same FIFO process except that higher priority
    nodes will be dequeued before lower priority nodes.  Nodes of the same
    priority will follow the same FIFO process.
    """

    class Node:
        """
        Each node is the queue will have both a value and a priority.
        """

        def __init__(self, value, priority):
            """
            Initialize a new node
            """
            self.value = value
            self.priority = priority

        def __str__(self):
            """
            Display a single node
            """
            return "{} (Pri:{})".format(self.value, self.priority)

    def __init__(self):
        """ 
        Initialize an empty priority queue
        """
        self.queue = []

    def enqueue(self, value, priority):
        """
        Add a new value to the queue with an associated priority.  The
        node is always added to the back of the queue irregardless of 
        the priority.
        """
        new_node = Priority_Queue.Node(priority, value) # switch these parameters
        self.queue.append(new_node)

    def dequeue(self):
        """
        Remove the next value from the queue based on the priority.  The 
        highest priority item will be removed.  In the case of multiple
        values with the same high priority, the one closest to the front
        (in traditional FIFO order) will be removed.  Priority values are
        interpreted as higher numbers have higher priority.  For example, 
        10 is a higher priority than 5.
        """
        if len(self.queue) == 0:  # Verify the queue is not empty
            print("The queue is empty.")
            return None

        high_pri_indices = [0]  # Initialize with the first index
        highest_priority = self.queue[0].priority

        # Find all indices with the highest priority
        for index in range(1, len(self.queue)):
            current_priority = self.queue[index].priority
            if current_priority > highest_priority:
                high_pri_indices = [index]
                highest_priority = current_priority
            elif current_priority == highest_priority:
                high_pri_indices.append(index)

        # Find the index of the item closest to the front (FIFO order) among the highest priorities
        closest_to_front_index = min(high_pri_indices)

        # Remove and return the item with the highest priority and closest to the front
        value = self.queue.pop(closest_to_front_index).value
        return value
    
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        priority queue.  This is useful for debugging.  If you have a 
        Priority_Queue object called pq, then you run print(pq) to see the 
        contents.
        """
        result = "["
        for node in self.queue:
            result += str(node)  # This uses the __str__ from the Node class
            result += ", "
        result += "]"
        return result


print("Test case: 1")
# Scenario: node order test case
# Expected Result: The enqueue function shall add a node to the back of the queue.
    
    # results: [website (Pri:5), backend (Pri:10), site work (Pri:7), debugging (Pri:2), ]
main = Priority_Queue()
main.enqueue(5, "website")
main.enqueue(10, "backend")
main.enqueue(7, "site work")
main.enqueue(2, "debugging")
print(main)

print("=================")

print("Test case: 2")
# Scenario: The dequeue function shall remove the node with the highest priority and return its value.
# designed this test to pop out highest proiry amongst all

# results: [website (Pri:2), backend (Pri:1), site work (Pri:3), debugging (Pri:1), website (Pri:2), site sever (Pri:3), debugging (Pri:1),]
#thing that happened: 'backend' with priorty of 8 was popped out of previous list
main = Priority_Queue()
main.enqueue(2, "website")
main.enqueue(1, "backend")
main.enqueue(3, "site work")
main.enqueue(1, "debugging")
main.enqueue(2, "website")
main.enqueue(8, "backend")
main.enqueue(3, "site sever")
main.enqueue(1, "debugging")
print(main.dequeue())
# print(main) # uncomment for debugging
print("=================")

print("Test case: 3")
# Scenario/ expected results: If there are more than one node with the highest priority,
# then the item closest to the front of the queue will be removed and its value returned.

# Result: debugging 2, debugging 1, website, and backend 1, were prioritized
main = Priority_Queue()
main.enqueue(5, "website")
main.enqueue(5, "backend 2")
main.enqueue(5, "site work")
main.enqueue(6, "debugging 1")
main.enqueue(6, "website")
main.enqueue(6, "backend 1")
main.enqueue(1, "site sever")
main.enqueue(10, "debugging 2")
for i in range(4): 
    deleted = main.dequeue()
    print(deleted)

print("=================")

print("Test case: 4")
# Scenario: Try to get the next person from an empty queue
# Expected Result: Error message should be displayed if empty list
main = Priority_Queue()
print(main.dequeue())

print("=================")

#After writing the test cases the only adjustments i needed to make to this code was to add 
#pop to remove an item from the queue besides that everything in the code was unaltered and 
#function according to what i wanted to see which was the list of things on the queue with 
#out the itme that was popped  