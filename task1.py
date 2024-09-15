class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not self.stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def peek(self):
        return self.stack[-1] if self.stack else None

    def size(self):
        stack_size = len(self.stack)
        return stack_size

    class Stack:
        def __init__(self) -> None:
            self.stack = []

        def is_empty(self) -> bool:
            return not self.stack

        def push(self, item: object) -> None:
            self.stack.append(item)

        def pop(self) -> object:
            return self.stack.pop() if not self.is_empty() else None

        def peek(self) -> object:
            return self.stack[-1] if not self.is_empty() else None

        def size(self) -> int:
            return len(self.stack)

    def is_balanced(self, brackets: str) -> str:
        stack = Stack()
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in brackets:
            if char in "([{":
                stack.push(char)
            elif char in ")]}":
                if stack.is_empty() or stack.pop() != pairs[char]:
                    return "Несбалансированно"

        return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


