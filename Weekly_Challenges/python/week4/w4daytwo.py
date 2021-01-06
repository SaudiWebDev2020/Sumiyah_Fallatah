# length
# --------------------------------------------------------------------------------------------------
# Create a function that accepts a pointer to first list node, and returns number of nodes in sList.

def length(self):
    temp = self.head
    count = 0 

    while (temp):
        count +=1
        temp = temp.next
    return count 

# average
# --------------------------------------------------------------------------------------------------
# Create a standalone function average(node) that returns (…wait for it … ) the average of all values contained in that list.

def avg(self):
    temp = self.head
    count = 0 
    sum = 0

    while (temp):
        sum += temp.value
        count +=1
        temp = temp.next
    average = sum / count 
    return average

# min, max
# --------------------------------------------------------------------------------------------------
# Create function min(node) and max(node) to returning smallest and largest values in the list.

def min(self):
    temp = self.head
    minimum = 0 
    while (temp):
        if temp < minimum:
            minimum = temp
    return minimum

# display
# --------------------------------------------------------------------------------------------------
# Create display(node) for debugging that returns a string containing all list values. Build what you wish console.log(myList) did!

def display