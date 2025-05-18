"""
# Time Complexity :
- init: O(1)
- add: O(1)
- remove: O(1)
- contains: O(1)
# Space Complexity :
- O(n)
# Did this code successfully run on Leetcode : Yes.
# Any problem you faced while coding this : No
"""

class MyHashSet(object):

    def __init__(self):
        self.bucket = [False]*(pow(10,6)+1)

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.bucket[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.bucket[key] = False
        
    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.bucket[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)