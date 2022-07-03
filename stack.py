#
class Stack:
    def __init__(self) -> None:
        self.val = []

    def add(self, data):
        if data in self.val:
            return False
        self.val.append(data)
        return True

    def remove(self):
        self.val.pop()

    def printStack(self):
        return self.val

    def peek(self):
        return self.val[-1]


if __name__ == '__main__':
    stack = Stack()
    n = int(input('Enter input count: '))
    for i in range(n):
        stack.add(int(input('Enter integer number (i+1): ')))
    print('*'*5,'Stack','*'*5)
    print(stack.printStack())

    #Removing element from stack
    stack.remove()

    print('Stack after removing one element')
    print(stack.printStack())
    print('** Value at the top of the stack **')
    print(stack.peek())