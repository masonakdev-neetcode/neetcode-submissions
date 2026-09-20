# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2 or not list2:
            return list1
        elif not list1:
            return list2
        
        l1ptr = list1
        l2ptr = list2
        mergedHead = None
        mergedPtr = None

        while l1ptr and l2ptr:
            if l1ptr.val < l2ptr.val:
                if not mergedPtr:
                    mergedPtr = l1ptr
                    mergedHead = mergedPtr
                else:
                    mergedPtr.next = l1ptr
                    mergedPtr = mergedPtr.next
                l1ptr = l1ptr.next
            else:
                if not mergedPtr:
                    mergedPtr = l2ptr
                    mergedHead = mergedPtr
                else:
                    mergedPtr.next = l2ptr
                    mergedPtr = mergedPtr.next
                l2ptr = l2ptr.next
        
        if l1ptr:
            mergedPtr.next = l1ptr
        if l2ptr:
            mergedPtr.next = l2ptr
        
        return mergedHead
