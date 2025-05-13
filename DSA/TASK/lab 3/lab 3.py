# task 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if not current:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_by_value(self, value):
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def display(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " → ".join(result) if result else "Empty"


# Test cases
if __name__ == "__main__":
    sll = SinglyLinkedList()

    # Insert at end
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.insert_at_end(4)
    print("Initial List:", sll.display())

    # Insert at end
    sll.insert_at_end(5)
    print("After Insert(5):", sll.display())

    # Delete node with value 3
    sll.delete_by_value(3)
    print("After Delete(3):", sll.display())

    # Search for value 4
    pos = sll.search(4)
    print(f"Search(4): Found at position {pos}" if pos != -1 else "Not found")

    # Insert at beginning
    sll.insert_at_beginning(0)
    print("After Insert(0):", sll.display())

    # Insert at position 3
    sll.insert_at_position(99, 3)
    print("After Insert(99) at pos 3:", sll.display())

# task 2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if not current:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_by_value(self, value):
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def display(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " → ".join(result) if result else "Empty"

    # Floyd's Cycle Detection Algorithm
    def detect_loop(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True, slow  # loop detected
        return False, None

    def find_loop_start(self):
        has_loop, meet_node = self.detect_loop()
        if not has_loop:
            return None
        slow = self.head
        while slow != meet_node:
            slow = slow.next
            meet_node = meet_node.next
        return slow  # start of loop

    def remove_loop(self):
        loop_start = self.find_loop_start()
        if not loop_start:
            return False  # no loop
        ptr = loop_start
        while ptr.next != loop_start:
            ptr = ptr.next
        ptr.next = None
        return True


# Test cases
if __name__ == "__main__":
    sll = SinglyLinkedList()

    # Insert at end
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.insert_at_end(4)
    sll.insert_at_end(5)
    print("Initial List:", sll.display())

    # Create loop manually: connect node 5 to node 3
    loop_start_node = sll.head.next.next  # node with value 3
    last_node = sll.head
    while last_node.next:
        last_node = last_node.next
    last_node.next = loop_start_node

    # Detect and remove loop
    loop_detected, _ = sll.detect_loop()
    print("Loop detected:", loop_detected)

    if loop_detected:
        loop_start = sll.find_loop_start()
        print("Loop starts at node with value:", loop_start.data)
        sll.remove_loop()
        print("Loop removed.")

    # Display the list again
    print("Final List:", sll.display())

# task 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the list."""
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_at_position(self, position):
        """Delete a node at a specific position."""
        if self.head is None:
            return
        current = self.head
        if position == 0:
            self.head = current.next
            if self.head:
                self.head.prev = None
            current = None
            return
        count = 0
        while current and count < position:
            count += 1
            current = current.next
        if current is None:
            raise IndexError("Position out of range")
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
        current = None

    def traverse_forward(self):
        """Traverse the list in forward direction."""
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " → ".join(result) if result else "Empty"

    def traverse_reverse(self):
        """Traverse the list in reverse direction."""
        current = self.head
        if not current:
            return "Empty"
        while current.next:
            current = current.next
        result = []
        while current:
            result.append(str(current.data))
            current = current.prev
        return " ← ".join(result)

# Test cases
if __name__ == "__main__":
    # Create DLL instance
    dll = DoublyLinkedList()

    # Insert nodes at the end
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    dll.insert_at_end(5)
    
    print("Forward Traversal:", dll.traverse_forward())  # 1 → 2 → 3 → 4 → 5
    print("Reverse Traversal:", dll.traverse_reverse())  # 5 ← 4 ← 3 ← 2 ← 1

    # Insert at the beginning
    dll.insert_at_beginning(0)
    print("After Inserting at Beginning:", dll.traverse_forward())  # 0 → 1 → 2 → 3 → 4 → 5

    # Delete a node at position 2 (3rd node)
    dll.delete_at_position(2)
    print("After Deleting at Position 2:", dll.traverse_forward())  # 0 → 1 → 2 → 4 → 5

    # Delete the first node (position 0)
    dll.delete_at_position(0)
    print("After Deleting at Position 0:", dll.traverse_forward())  # 1 → 2 → 4 → 5
