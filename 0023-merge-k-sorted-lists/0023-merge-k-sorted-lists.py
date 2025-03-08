import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        min_heap = []
        
        # Add the first node of each linked list to the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))  # (value, index, node)
        
        dummy = ListNode(0)
        current = dummy
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap)  # Extract smallest node
            current.next = node
            current = current.next
            
            if node.next:  # Push the next node from the same list
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next
