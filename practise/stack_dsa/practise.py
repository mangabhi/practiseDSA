# class Stack_brute:
#     def __init__(self):
#         self.arr=[]

#     def push(self,x):
#         self.arr.append(x)

#     def pop(self):
#         if not self.arr:
#             raise IndexError("Stack UnderFlow")
#         return self.arr.pop()

#     def peek(self):
#         if not self.arr:
#             return -1
#             # raise IndexError("Stack UnderFlow")
#         return self.arr[-1]

#     def isEmpty(self):
#         return len(self.arr)==0

#     def printstack(self):
#         if not self.arr:
#             return -1
#         for num in self.arr:
#             print(num)

# stack=Stack_brute()
# # stack.push(20)
# # stack.push(30)
# # stack.push(10)
# print(stack.peek())
# print(stack.printstack())

# class Node:
#     def __init__(self,val):
#         self.val=val 
#         self.next=None

# class StackLinkedList:
#     def __init__(self):
#         self.head=None

#     #push
#     def push(self,x):
#         node=Node(x)
#         if not self.head:
#             self.head=node
#             return
#         curr=self.head
#         while curr.next:
#             curr=curr.next
#         curr.next=node 


A,B=10,20
A=A^B
B=A^B
A=A^B
print(A,B)