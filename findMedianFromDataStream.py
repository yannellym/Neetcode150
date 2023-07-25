# 295. Find Median from Data Stream
# Hard
# 10.8K
# 210
# company
# Amazon
# company
# Uber
# IXL
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
 

# Constraints:

# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.
 

# Follow up:

# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# Accepted
# 655.6K
# Submissions
# 1.3M
# Acceptance Rate
# 51.5


class MedianFinder(object):
    def __init__(self):
        self.store = []  # List to store the numbers
        self.size = 0    # Variable to keep track of the number of elements in the list

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.store.append(num)  # Add the new number to the list
        self.size += 1         # Increment the size counter

    def findMedian(self):
        """
        :rtype: float
        """
        self.store.sort()  # Sort the list before finding the median

        if self.size > 1 and self.size % 2 == 0:
            # If there are more than one element and the number of elements is even
            mid_right = self.size // 2         # Index of the right middle element
            mid_left = mid_right - 1           # Index of the left middle element
            median = (float(self.store[mid_left] + self.store[mid_right]) / 2)
            # Calculate the average of the two middle elements as the median
        else:
            median = float(self.store[self.size // 2])
            # If there's only one element or the number of elements is odd,
            # the median is the middle element

        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
