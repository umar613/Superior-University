# Node for Linked List
class StudentNode:
    def __init__(self, name):
        self.name = name
        self.next = None

# Linked List for maintaining student order
class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, name):
        new_node = StudentNode(name)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def display_students(self):
        curr = self.head
        while curr:
            print(curr.name, end=" -> ")
            curr = curr.next
        print("None")


# Queue for submissions
class SubmissionQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, student):
        self.queue.append(student)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0


# Stack for grade check history
class HistoryStack:
    def __init__(self):
        self.stack = []

    def push(self, student):
        self.stack.append(student)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def show_history(self):
        print("Grade Check History:", self.stack)


# BST Node
class StudentBSTNode:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.left = None
        self.right = None


# BST for searching students
class StudentBST:
    def __init__(self):
        self.root = None

    def insert(self, name, grade):
        self.root = self._insert(self.root, name, grade)

    def _insert(self, root, name, grade):
        if root is None:
            return StudentBSTNode(name, grade)
        if name < root.name:
            root.left = self._insert(root.left, name, grade)
        else:
            root.right = self._insert(root.right, name, grade)
        return root

    def search(self, name):
        return self._search(self.root, name)

    def _search(self, root, name):
        if root is None:
            return None
        if root.name == name:
            return root.grade
        elif name < root.name:
            return self._search(root.left, name)
        else:
            return self._search(root.right, name)


# Main Grade Checker Class
class StudentGradeChecker:
    def __init__(self):
        self.linked_list = StudentLinkedList()
        self.queue = SubmissionQueue()
        self.stack = HistoryStack()
        self.bst = StudentBST()

    def add_student(self, name, grade):
        self.linked_list.add_student(name)
        self.queue.enqueue(name)
        self.bst.insert(name, grade)

    def process_next_submission(self):
        student = self.queue.dequeue()
        if student:
            grade = self.bst.search(student)
            if grade is not None:
                print(f"Student: {student}, Grade: {grade}")
                self.stack.push(student)
            else:
                print(f"Student {student} not found in grade records.")
        else:
            print("No submissions to process.")

    def undo_last_check(self):
        student = self.stack.pop()
        if student:
            print(f"Undid last check for: {student}")
        else:
            print("No history to undo.")

    def show_student_order(self):
        print("Students in linked list order:")
        self.linked_list.display_students()

    def show_check_history(self):
        self.stack.show_history()


# Example Usage
checker = StudentGradeChecker()
checker.add_student("Alice", 85)
checker.add_student("Bob", 92)
checker.add_student("Charlie", 78)

checker.show_student_order()
checker.process_next_submission()
checker.process_next_submission()
checker.show_check_history()
checker.undo_last_check()
checker.show_check_history()
