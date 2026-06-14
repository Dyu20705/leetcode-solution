# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head: return None
        curr = node = head
        hold = []
        while node:
            node = node.next
            if node:
                node = node.next
                hold.append(curr.val)
                curr = curr.next
        maxVal = -1
        for i in hold[::-1]:
            i += curr.val
            curr = curr.next
            if i > maxVal: maxVal = i
        return maxVal
                


        