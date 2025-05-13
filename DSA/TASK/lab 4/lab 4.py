# task 1
class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, element):
        """Push an element onto the stack."""
        self.stack.append(element)

    def pop(self):
        """Pop the top element from the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.stack)

# Test cases for StackArray
if __name__ == "__main__":
    stack_arr = StackArray()

    print("Is stack empty?", stack_arr.is_empty())  # True
    stack_arr.push(1)
    stack_arr.push(2)
    stack_arr.push(3)

    print("Top element:", stack_arr.peek())  # 3
    print("Size of stack:", stack_arr.size())  # 3

    print("Pop element:", stack_arr.pop())  # 3
    print("Size of stack after pop:", stack_arr.size())  # 2
    print("Is stack empty?", stack_arr.is_empty())  # False

#Stack Using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, element):
        """Push an element onto the stack."""
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """Pop the top element from the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def size(self):
        """Return the number of elements in the stack."""
        return self.size

# Test cases for StackLinkedList
if __name__ == "__main__":
    stack_ll = StackLinkedList()

    print("Is stack empty?", stack_ll.is_empty())  # True
    stack_ll.push(1)
    stack_ll.push(2)
    stack_ll.push(3)

    print("Top element:", stack_ll.peek())  # 3
    print("Size of stack:", stack_ll.size())  # 3

    print("Pop element:", stack_ll.pop())  # 3
    print("Size of stack after pop:", stack_ll.size())  # 2
    print("Is stack empty?", stack_ll.is_empty())  # False


# taske 2

def evaluate_postfix(expression):
    """Evaluate a postfix expression using a stack."""
    stack = []
    
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit(): 
            stack.append(int(token))
        else: 
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            # Perform the operation based on the operator
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            
            stack.append(result)
    
    return stack.pop()

# Test cases
if __name__ == "__main__":
    # Test Case 1: Example given in the prompt
    expression1 = "5 1 2 + 4 * + 3 -"
    print("Result of expression 1:", evaluate_postfix(expression1))
    
    # Test Case 2: Another example
    expression2 = "3 4 + 2 * 7 /"
    print("Result of expression 2:", evaluate_postfix(expression2))
    
    # Test Case 3: A more complex expression
    expression3 = "10 6 9 3 + -11 * / * 17 + 5 +"
    print("Result of expression 3:", evaluate_postfix(expression3))
    
    # Test Case 4: Expression with negative numbers
    expression4 = "3 4 - 2 *"
    print("Result of expression 4:", evaluate_postfix(expression4))


# task 3
# Circular Queue Code

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  
        self.front = -1  
        self.rear = -1   

    def enqueue(self, element):
        if self.is_full():
            print("Queue is full!")
        else:
            if self.front == -1:  
                self.front = 0
            self.rear = (self.rear + 1) % self.size  
            self.queue[self.rear] = element
            print(f"Enqueued {element}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        else:
            element = self.queue[self.front]
            if self.front == self.rear: 
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            return element

    def front(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[self.front]

    def rear(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[self.rear]

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        idx = self.front
        while idx != self.rear:
            print(self.queue[idx], end=" -> ")
            idx = (idx + 1) % self.size
        print(self.queue[self.rear])


# Test Circular Queue
cq = CircularQueue(5)

# Enqueue elements
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)

cq.enqueue(60)  

print("Dequeued:", cq.dequeue())  

cq.enqueue(60)

cq.display() 


print("Front:", cq.front())  
print("Rear:", cq.rear())

# Linear Queue Implementation (Using a List)

class LinearQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)
        print(f"Enqueued {element}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[0]

    def rear(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[-1]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        print(" -> ".join(map(str, self.queue)))


# Test Linear Queue
lq = LinearQueue()


lq.enqueue(10)
lq.enqueue(20)
lq.enqueue(30)
lq.enqueue(40)
lq.enqueue(50)

print("Dequeued:", lq.dequeue()) 

lq.enqueue(60)

lq.display()  

print("Front:", lq.front()) 
print("Rear:", lq.rear())  

