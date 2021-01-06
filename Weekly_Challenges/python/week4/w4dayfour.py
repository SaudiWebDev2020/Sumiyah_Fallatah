# Remove Negatives
# ------------------------------------------------------------------------------------
# Given a pointer to the head node of a singly linked list, remove any nodes containing negative values and return the list.

def removeNeg(self, node):
    node = self.head
    arr=[]
    while (node != None):
        if node.value > 0:
            arr.append(node.value)
        node = node.next
    return arr


# Partition
# ------------------------------------------------------------------------------------
# Create partition(ListNode, value) that locates the first node with that value, and moves all nodes with values less than that value to be earlier, and all nodes with values greater than that value to be later.  Otherwise, original order need not ve perfectly preserved. return the new head ListNode.

def partition(node, value):
    node = self.node
    head= self.head
    if value == node.value:
        pass
    while (node != None):
        pass