# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        temp=head
        arr=[]
        while temp:
            arr.append(temp.val)
            temp=temp.next

        temp=head
        arr.sort()
        for value in arr:
            temp.val=value
            temp=temp.next

        return head