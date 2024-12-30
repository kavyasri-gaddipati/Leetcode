# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to act as the starting point
        dummy = ListNode(-1)
        current = dummy  # Pointer to build the new list

        # While both lists are non-empty, compare their current nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining elements of list1 or list2, if any
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        # Return the merged list, skipping the dummy node
        return dummy.next
