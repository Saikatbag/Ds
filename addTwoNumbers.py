# +++++++++++++++++++++++++++++++ AddTwoNumber ++++++++++++++++++++++++++++++++++++++++
# You are given two non-empty linked lists representing two non-negative integers.
#  The digits are stored in reverse order, and each of their nodes contains a single digit. 
#  Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# ==================================================================
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l2,l1):
    pri = l1
    st1 = ""
    while pri is not None:
        st1 = st1 + str(pri.val)
        pri = pri.next
            
    pria = l2
    st2= ""
    while pria is not None:
        st2 = st2 + str(pria.val)
        pria=pria.next
        
    ad = int(st1[::-1] ) + int(st2[::-1])
    st = str(ad)
    ad = list(st[::-1])
 
    l3= ListNode(int(ad[0]))
    l=l3
    for i in range (1,len(ad)):
        node=ListNode(int(ad[i])) 
        l.next=node
        l=l.next
            
    return l3

l1=ListNode(5)
l=l1
l2=ListNode(9)
l0=l2
for i in range (3,5):
    node=ListNode(i) 
    l.next=node
    l=l.next
for i in range (4,8):
    node=ListNode(i) 
    l0.next=node
    l0=l0.next



no = addTwoNumbers(l2,l1)
while no is not None:
    print(no.val)
    no = no.next

