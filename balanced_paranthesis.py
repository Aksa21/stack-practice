from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()

    def is_balanced(self,val):
        for ch in val:
            if ch in "{([":
                self.container.append(ch)
            elif ch in "})]":
                if not self.container:
                   return False
               
                top=self.container.pop()
                if(ch=='}' and top!='{') or \
                  (ch==')' and top!='(') or \
                  (ch==']' and top!='['):
                    return False
        return len(self.container)==0

               
    def display(self):
       print(list(self.container))

if __name__ == "__main__":
    s = Stack()
    print(s.is_balanced("{a+(b*c))-[d/e]}"))   # True
       