# Node
#    - Constructor
#       -val
#       - next
class StackNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = None



#    -Constructor
#        - head
class Stack:
    def __init__(self):
        self.head = None
        temp = self.head

    # Stack Push
    # ------------------------------------------------
    # Create push(val) that adds val to our stack.
    def push(self, val):
        if self.head == None:
            self.head = StackNode(val)
        else:
            print('pushing...')
            new_val = StackNode(val)
            new_val.next = self.head
            self.head = new_val

    
    # Stack Top
    # ------------------------------------------------
    # Return (not remove) the stack’s top value.
    def top(self):
        if self.head == None:
            return None
        else:
            print('top is :')
            print (self.head.value)

    
    # Stack Is Empty
    # ------------------------------------------------
    # Return whether the stack is empty.
    def isEmpty(self):
        if self.head == None:
            print ("this stack is empty")
        else:
            print ("this stack is not empty")


    # Stack Pop
    # ------------------------------------------------
    # Create pop() to remove and return the top val.
    def pop(self):
        if self.head == None:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            print('popping ...')
            return f"the value {value} has been removed"

    
    # Stack Contains
    # ------------------------------------------------
    # Return whether given val is within the stack.
    def contain(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                print(f"the value {value} exists!")
                return True

            current = current.next
        # print(f"the value {value} does not exist")
        return False



    # Stack Size
    # ------------------------------------------------
    # Return the number of stacked values.
    def size(self):
        # if self.head == None:
        #     return None
        # else:
        temp = self.head
        count = 0 
        while(temp):
            count+=1
            # print('value', temp.value)
            temp = temp.next
        print('size is :', count)
        return count


    def printstack(self):
        head = self.head
        while(head):
            print(head.value)
            head = head.next

    
    def rListLength(self):
        count =0
        if self.head == None:
            return None
        else:
            count+=1
            self.head.next
            return rListLength(self)


lifo = Stack()
lifo.isEmpty()
print('-'*30)
lifo.push(5)
lifo.push(9)
lifo.printstack()
print('-'*30)
lifo.pop()
lifo.printstack()
print('-'*30)
lifo.isEmpty()
print('-'*30)
lifo.size()
print('-'*30)
lifo.top()
print('-*'*30)
lifo.pop()

lifo.printstack()
print('-'*30)
lifo.isEmpty()
print('-'*30)
lifo.top()
lifo.push(5)
lifo.push(4)
lifo.push(7)
print(lifo.contain(5))
print(lifo.contain(9))
print('-'*30)
print('-'*30)
lifo.rListLength()