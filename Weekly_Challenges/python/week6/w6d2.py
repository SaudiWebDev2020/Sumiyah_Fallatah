# Recursive Fibonacci
# ------------------------------------------------------------------------------------------------------------------------
# Write rFib(num). Recursively compute and return the numth Fibonacci value. As earlier, treat the first two (num = 0, num = 1) Fibonacci values as 0 and 1. Thus:
# rFib(2) = 1 (0+1)
# rFib(3) = 2 (1+1)
# rFib(4) = 3 (1+2)
# rFib(5) = 5 (2+3)
# rFib(3.65) = rFib(3) = 2
# rFib(-2) = rFib(0) = 0.

def rFib(num):
    num = int(num)
    if num < 1:
        return 0
    elif num==1:
        return 1
    else:
        return rFib(num-1)+rFib(num-2)

print(rFib(9)) #should be 34 not 21..
print(rFib(-2))
print(rFib(3.54))
print(rFib(5))
# rListLength
# ------------------------------------------------------------------------------------------------------------------------
# Given the first node of a singly linked list, create a recursive function that returns the number of nodes in that list. You can assume the list contains no loops, and that it is short enough that you will not ‘blow your stack’.
# count =0
# temp = self.head
# def rListLength(self):
#     if self.head == None:
#         return None
#     else:
#         count+=1
#         temp = temp.next
#         return rListLength(self)







# def size(self):
#         # if self.head == None:
#         #     return None
#         # else:
#         temp = self.head
#         count = 0 
#         while(temp):
#             count+=1
#             # print('value', temp.value)
#             temp = temp.next
#         print('size is :', count)
#         return count
