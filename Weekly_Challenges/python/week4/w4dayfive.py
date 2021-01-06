# Second Largest Value
# ------------------------------------------------------------------------------------
# Given a pointer to the first node in a singly linked list, return the second-largest value in the list.

#  traverse the Linked list twice. In the first traversal find the maximum element. In the second traversal find the greatest element less than the element obtained in first traversal. 


def secondlargest(self, node):
    if (self.head == None):
        return None 
    node = self.head

    val1 = node.value
    val2 = node.next.value

    max = max(val1,val2)
    second = min(val1,val2) 
    while (temp != None):
        if temp.value > maximum:
            maximum = node.value
            
            if temp.value > 
        temp = temp.next
    
    # while (temp != None):
    #     if 





# Zip SLists
# ------------------------------------------------------------------------------------
# Provided two pointers to independent linked lists 'zip' the two lists together be alternating nodes.  Start with the first list, and return the new list.

def ziplist(node1, node2):
    head1 = node1.head #yellow1
    head2 = node2.head #green1

    head2.next = head1.next
    head1.next = head2

    head1.next.next.next = head2.next.next

    while (head1):
        print(head1.value)
        head1 = head1.next
