"""
# Time Complexity :
- init: O(1)
- push: O(1)
- pop: O(1)
- top: O(1)
- getmin: O(1)
# Space Complexity :
- O(n)
# Did this code successfully run on Leetcode : Yes.
# Any problem you faced while coding this : No
"""

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        popped_value = self.stack.pop()
        if popped_value == self.minstack[-1]:
            self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()