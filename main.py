class Stack:
    def __init__ (self, n):
        self.n = n
        self.stack = []

    def push(self, v):
        if len(self.stack) < self.n:
            self.stack.append(v)
        else:
            print("Stack full")

    def pop(self):
        if len(self.stack)  == 0:
            print("Not possible, no elements")
        else:
            self.stack.pop(-1)
    
    def top(self):
        if len(self.stack) == 0:
            print("stack empty")
        else:
            print(self.stack[-1])
    
    def size(self):
        print (len(self.stack))

    def display(self):
        print (self.stack)

object_s1 = Stack(7)


object_s1.display()

object_s1.size()

object_s1.push(7)
object_s1.push(9)
object_s1.push(32)
object_s1.push(43)
object_s1.push(85)
object_s1.push(39)
object_s1.push(76)


object_s1.display()



object_s1.size()

object_s1.push(17)

object_s1.pop()

object_s1.display()

object_s1.top()
object_s1.size()

object_s1.pop()
object_s1.pop()
object_s1.display()

object_s1.pop()
object_s1.pop()
object_s1.pop()
object_s1.pop()

object_s1.display()
object_s1.pop()

