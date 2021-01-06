class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next



class SinglylinkedList:
    def __init__(self):
        self.head = None

    def addFront(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def removeFront(self):
        if (self.head == None):
            return None
        self.head = self.head.next

    def length(self, Node):
        if (self.head == None):
            return None
        node = self.head
        counter = 0
        while (node != None):
            counter += 1
            node = node.next
        # print("The length", counter)
        return counter

    def average(self, node):
        if (self.head == None):
            return None
        node = self.head
        count = self.length(node)
        sum = 0
        while (node != None):
            sum += node.value
            node = node.next
        # print("The average", count, "The average", sum / count)
        return sum / count

    def min(self, node):
        if (self.head == None):
            return None
        node = self.head
        min = node.value
        while (node != None):
            if node.value < min:
                min = node.value
            node = node.next
        return min

    def max(self, node):
        if (self.head == None):
            return None
        node = self.head
        max = node.value
        while (node != None):
            if node.value > max:
                max = node.value
            node = node.next
        return max

    def display(self, node):
        arr = []
        node = self.head

        while (node != None):
            arr.append(node.value)
            node = node.next

        return arr


    def printList(self):
        current_node = self.head
        while(current_node):
            print(current_node.value)
            current_node = current_node.next

    # def container(self,value):
    #     newNode = self.head
    #     while(newNode.next != None):
    #         if value == newNode.value:
    #             print("Yes it is in the list")
    #         else:
    #             newNode = newNode.next
            
    # def addBack(value):
    #     pass
    # def removeBack():





#--------------------------------
singlyLL = SinglylinkedList()
singlyLL.addFront(10)
singlyLL.addFront(10)
singlyLL.addFront(5)
singlyLL.addFront(2)
singlyLL.addFront(1)

# singlyLL.removeFront()
# singlyLL.container(1)
print("------The values in the list------")
singlyLL.printList()
node = Node()
print("The length:",singlyLL.length(node))
print("The average:",singlyLL.average(node))
print("The min:",singlyLL.min(node))
print("The max:",singlyLL.max(node))
print("The list:",singlyLL.display(node))
# print(singlyLL.head.value)