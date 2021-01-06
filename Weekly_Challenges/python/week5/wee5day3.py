# Create a queue using 2 stacks. A hint: stack1 will hold the contents of the actual queue, stack2 will be used in the enQueueing
# Efficiency is not the goal!
# Efficiency is not the goal!
# Efficiency is not the goal!
# The goal is to practice using one data structure to implement another one, in our case Queue from 2 Stacks
# Queue is FIFO --> First In First out
# Stack is LIFO --> Last  In First Out

class StackNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

class QueueOfStacks:
    class StackNode:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = None
    class Stack:
        def __init__(self):
            self.head = None
            self.tail = None
        # def __init__(self):
            self.stack1 = Stack()
            self.stack2 = Stack()


        def front(self):
            if self.head == None:
                return None
            else:
                print('top is :')
                print (self.head.value)
        
        def isEmpty(self):
            if self.head == None:
                print ("this stack is empty")
            else:
                print ("this stack is not empty")

        def size(self):
            temp = self.head
            count = 0 
            while(temp):
                count+=1
                # print('value', temp.value)
                temp = temp.next
            print('size is :', count)
            return count

        def deQueue(self):
            temp = 0
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                temp = self.head
                self.head = self.head.next
            return temp.value

        def enQueue(self, value): 
            if self.head == None:
                new_node = StackNode(value)
                self.head = new_node
                self.tail = new_node
            else:
                new_node = StackNode(value)
                self.tail.next = new_node
                self.tail = new_node

        # Optional
        # def showQS(self):
        #     pass
        #     head = self.head
        # while(head):
        #     print(head.value)
        #     head = head.next

stack1 = QueueOfStacks.Stack()
stack2 = QueueOfStacks.Stack()

stack1.isEmpty()
print('*'*70)
stack2.isEmpty()
stack1.enQueue(7)
# stack1.showQS()
print(stack1.front())
stack1.isEmpty()
print('*'*70)
print(stack1.deQueue())
stack1.isEmpty()