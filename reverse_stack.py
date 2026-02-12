#from inspect import stack
from collections import deque
from inspect import stack
class Stack:
    def __init__(self):
        self.container=deque()

    def insert(self,val):
        for ch in val:
         self.container.append(ch)

    def reverse_string(self):
        temp=deque()
        
        while self.container:
           temp.append(self.container.pop())

        self.container=temp    

    def display(self):
        print("".join(self.container))


if __name__ == "__main__":
    s = Stack()
    s.insert("We will conquer")
    s.reverse_string()
    s.display()