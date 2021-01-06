# Node
#    - Constructor
#       -val
#       - next
class SLNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = None


# SinglyLinkList
#    -Constructor
#        - head
class SList:
    def __init__(self):
        self.head = None

#    - addFront(val)
#        - add a new node to the beginning of the list
    def addFront(self, value): 
        if self.head == None:
            self.head = SLNode(value)
        else:
            new_node = SLNode(value)
            new_node.next = self.head
            self.head = new_node


    #    - removeFront()
    #       - removes and returns the first node of the list
    def removeFront(self):
        # if not head:
        #     return None
        # temp = head
        # head = head.next
        # temp = None
        # return head
        self.head = self.head.next
        

    #    - container(val)
    #       - returns a boolean on whether or not the val is in the list
    def container(val):
        current_node = self.head
        if current_node == val:
            print(current_node)
        else:
            pass
        


    #    -  addBack(val)
    #        - add new node to the end of the list
    # def addBack(self, value):
    #     new_node = SLNode(value)
    #     self.last = new_node(value)
        


    #    - removeBack()
    #       - removes and returns the last node of the list
    def removeBack():
        pass

    def printLL(self):
        current_head = self.head
        while(current_head):
            print(current_head.value)
            current_head = current_head.next

    def length(self):
        temp = self.head
        count = 0 

        while (temp):
            count +=1
            print(temp.value)
            temp = temp.next
        return count 

    def avg(self):
        temp = self.head
        count = 0 
        sum = 0

        while (temp):
            sum += temp.value
            count +=1
            temp = temp.next
        average = sum / count 
        print(sum)
        print(count)
        return average

    def min(self):
        temp = self.head
        minimum = 10000
        while (temp != None):
            if temp.value < minimum:
                minimum = int(temp.value)
            temp = temp.next
        return minimum

    def max(self):
        temp = self.head
        maximum = -10000
        while (temp != None):
            if temp.value > maximum:
                maximum = int(temp.value)
            temp = temp.next
        return maximum

    def removeNeg(self, node):
        node = self.head
        nl = SList()
        # arr=[]
        while (node != None):
            if node.value > 0:
                nl.addFront(node.value)
            node = node.next
        return nl.printLL()
    
    def ziplist(self, node1, node2):
        head1 = node1.head #yellow1
        head2 = node2.head #green1

        head2.next = head1.next
        head1.next = head2

        head1.next.next.next = head2.next.next

        while (head1):
            print(head1.value)
            head1 = head1.next

    def findLargestAndSecondLargest(self): 
    
        # Take a Head to iterate list 
        Head = self.head 
    
        # Initialize max and second_max 
        # using first two nodes of the list 
        val1 = Head.value
        val2 = Head.next.value
        Max = max(val1, val2) 
        second_max = min(val1, val2) 
    
        # Move the Head to third node 
        Head = Head.next.next
    
        # Iterate over rest of linked list 
        while(Head != None): 
            
            # If current node value is  
            # greater then Max then 
            if(Head.value > Max): 
                
                # Set the current max to second_max 
                # and current node value to max 
                second_max = Max
                Max = Head.value
    
            # Else if current node value is 
            # greater then second_max value 
            elif(Head.value > second_max): 
                
                # Then current node value 
                # to second_max 
                second_max = Head.value
    
            # Move the head to next node 
            Head = Head.next
    
        # Print the largest and second largest values 
        # print("Largest = ", Max) 
        print("Second Largest = ", second_max) 
        return second_max


sl = SList()
sl.addFront(10)
sl.addFront(15)
sl.addFront(20)
sl.addFront(5)
sl.addFront(29)
sl.addFront(1)
sl.printLL()
print('-'*30)
sl.removeFront()
sl.printLL()
print('-'*30)
# sl.addBack(2)
sl.printLL()

print("length of list is : " , sl.length())

print('-'*30)

print("The average of the list is : ", sl.avg())

print('-'*30)

print( "the minimum of the list is : ", sl.min())

print('-'*30)

print( "the maximum of the list is : ", sl.max())

print('-*-'*30)

# def removeVal(listx,val):
#     for x in listx:
#         if self.head.value[x] == val:
#             self.head = self.head.next
#     return listx

def removeNode(self,value):
    prev = None
    curr = self.head
    while curr:
        if curr.next.value == value:
            if prev:
                prev.setNextNode(curr.next.next)
            else:
                self.head = curr.next.next
            return True

        prev = curr
        curr = curr.getNextNode()
        
    return False

list_new = SList()
list_new.addFront(-1)
list_new.addFront(2)
list_new.addFront(-6)
list_new.addFront(4)
list_new.addFront(5)
list_new.addFront(11)
list_new.addFront(-2)
list_new.addFront(3)
list_new.addFront(9)
list_new.addFront(-5)
list_new.printLL()

print('-'*30)

# print(removeNode(list_new, 3))
node = SLNode()
# print(list_new.removeNeg(node))

list_new.findLargestAndSecondLargest()
print('*'*50)


list1= SList()
list2 = SList()
node1 = SLNode()
node2 = SLNode()

list1.addFront(1)
list1.addFront(1)

list2.addFront(3)
list2.addFront(3)

def ziplist(list1, list2):
    head1 = list1.self.head #yellow1
    head2 = list2.self.head #green1

    head2.next = head1.next
    head1.next = head2

    head1.next.next.next = head2.next.next

    while (head1):
        print(head1.value)
        head1 = head1.next

print(ziplist(list1, list2))