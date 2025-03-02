# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k == 1:
            return head
        
        # Count number of nodes in the list
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        count = 0
        
        while curr:
            count += 1
            curr = curr.next
        
        # Reverse in groups of k
        while count >= k:
            curr = prev.next
            next_node = curr.next
            
            # Reverse k nodes
            for _ in range(k - 1):
                curr.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node
                next_node = curr.next
            
            prev = curr
            count -= k
        
        return dummy.next
