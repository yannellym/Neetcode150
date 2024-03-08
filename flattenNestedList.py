https://leetcode.com/problems/flatten-nested-list-iterator/submissions/1197157441/?envType=daily-question&envId=2024-03-07

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator:
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # Initialize a stack to store the nested list in reverse order
        self.stack = nestedList[::-1]
        print(self.stack)

    def next(self):
        """
        :rtype: int
        """
        # Pop the top element from the stack and return its integer value
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        # Continue until the stack is empty
        while self.stack:
            # Get the top element of the stack
            top = self.stack[-1]
            # If the top element is an integer, there are more elements to iterate over
            if top.isInteger():
                return True
            # If the top element is a nested list, flatten it and add its elements to the stack
            self.stack = self.stack[:-1] + top.getList()[::-1]
        # If the stack is empty, there are no more elements to iterate over
        return False



Code
Testcase
Testcase
Test Result
341. Flatten Nested List Iterator
Solved
Medium
Topics
Companies
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.

 

Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
 

Constraints:

1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-106, 106].
Seen this question in a real interview before?
1/4
Yes
No
Accepted
440.4K
Submissions
684.5K
Acceptance Rate
64.3%
