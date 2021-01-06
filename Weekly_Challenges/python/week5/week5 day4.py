# Circular Queues
# ------------------------------------------------------------------------
# When Queue’s tail or head approaches ‘size’, wrap around to [0] and continue. We cannot let tail and head meet – one can’t “lap” the other. Instead, enqueue(val) should fail: Queue is full. Ditto dequeue() if Queue is empty. Constructor requires a size argument. Starting there, let’s create a circular queue implementation!

def CirQueue():
    def __init__(self, cap):
        self.head = 0
        self.tail = 0
        self.capacity = cap
        self.data = [None]*cap
        self.size = size

# Enqueue
# ------------------------------------------------------------------------
# Create enqueue(val) that adds val to our circular queue. Return false on fail. Wrap if needed!
    def enQ(self, value):
        if((self.tail +1) %self.size == self.head):
            print("Q is full")
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.data[self.tail] = value
        else:
            self.tail = (self.tail+1) % self.size
            self.data[self.tail] = value

# Front
# ------------------------------------------------------------------------
# Return (not remove) the queue’s front value.
    def front(self):
        if self.head == None:
            return None
        else:
            print(f'top is : {self.head.value}')


# Is Empty
# ------------------------------------------------------------------------
# Return whether queue is empty.
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

# Is Full
# ------------------------------------------------------------------------
# Return whether queue is full.
    def isFull(self):
        if self.capacity == self.size:
            return True
        else:
            return False

# Dequeue
# ------------------------------------------------------------------------
# Create cirQueue method dequeue() that removes and returns the front value. Return null on fail.
    def deQ(self):
        if self.head == -1:
            print("Q is empty")
        elif self.head == self.tail:
            temp = self.data[self.head]
            self.front = -1
            self.tail = -1
            return temp
        else:
            temp = self.data[self.head]
            self.head = (self.head + 1) % self.size
            return temp



# Contains
# ------------------------------------------------------------------------
# Return whether given val is within the queue.
    def contain(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                print(f"the value {value} exists!")
                return True

            current = current.next
        # print(f"the value {value} does not exist")
        return False

# Size
# ------------------------------------------------------------------------
# Return number of queued vals (not capacity).
    def size(self):
        temp = self.head
            count = 0 
            while(temp):
                count+=1
                # print('value', temp.value)
                temp = temp.next
            print('size is :', count)
            return count


