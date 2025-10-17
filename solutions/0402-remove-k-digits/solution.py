"""
402. Remove K Digits - Solved using Direct Linked List

Given a string num representing a non-negative integer and an integer k,
return the smallest possible integer after removing k digits from num.

Algorithm:
- Use a doubly linked list to store digits
- Traverse the number and maintain a monotonic increasing sequence
- Remove larger digits that come before smaller digits
- Handle edge cases: leading zeros, removing all digits
"""

class Node:
    """Doubly linked list node to store a digit"""
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Remove k digits from num to get the smallest possible number.
        
        Time: O(n) where n is the length of num
        Space: O(n) for the linked list
        """
        if k >= len(num):
            return "0"
        
        if k == 0:
            return num
        
        # Create a dummy head for the linked list
        dummy = Node('0')
        tail = dummy
        
        # Build the linked list while maintaining monotonic property
        removals = 0
        
        for digit in num:
            # Remove larger digits from the tail while we can
            while removals < k and tail != dummy and tail.val > digit:
                # Remove the tail node
                prev_node = tail.prev
                prev_node.next = None
                tail = prev_node
                removals += 1
            
            # Add the current digit
            new_node = Node(digit)
            new_node.prev = tail
            tail.next = new_node
            tail = new_node
        
        # If we haven't removed k digits yet, remove from the end
        while removals < k:
            prev_node = tail.prev
            prev_node.next = None
            tail = prev_node
            removals += 1
        
        # Build the result string from the linked list
        result = []
        current = dummy.next
        
        # Skip leading zeros
        while current and current.val == '0':
            current = current.next
        
        # Collect remaining digits
        while current:
            result.append(current.val)
            current = current.next
        
        # Return "0" if result is empty
        return ''.join(result) if result else "0"


