class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Извлечение из пустого стека")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Просмотр пустого стека")

    def size(self):
        return len(self.items)


def is_balanced(brackets):
    stack = Stack()
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for bracket in brackets:
        if bracket in opening_brackets:
            stack.push(bracket)
        elif bracket in closing_brackets:
            if stack.is_empty():
                return "Несбалансированно"
            if stack.peek() == bracket_pairs[bracket]:
                stack.pop()
            else:
                return "Несбалансированно"

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


if __name__ == '__main__':
    # Примеры использования:
    print(is_balanced("(((([{}]))))"))  # Сбалансированно
    print(is_balanced("[([])((([[[]]])))]{()}"))  # Сбалансированно
    print(is_balanced("{{[()]}}"))  # Сбалансированно
    print(is_balanced("}{}"))  # Несбалансированно
    print(is_balanced("{{[(])]}}"))  # Несбалансированно
    print(is_balanced("[[{())}]"))  # Несбалансированно
