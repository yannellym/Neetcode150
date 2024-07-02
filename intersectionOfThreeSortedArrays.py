1213. Intersection of Three Sorted Arrays
Solved
Easy
Topics
Companies
Hint
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
Example 2:

Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
Output: []
 

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
Seen this question in a real interview before?
1/5
Yes
No
Accepted
87.2K
Submissions
109.2K
Acceptance Rate
79.8%

class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        # Step 1: Convert lists to sets
        set1 = set(arr1)
        set2 = set(arr2)
        set3 = set(arr3)

        # Step 2: Find the intersection of the sets
        common_elements = set1 & set2 & set3  # or set1.intersection(set2).intersection(set3)

        # Step 3: Convert the intersection to a list
        common_list = list(common_elements)

        # Step 4: Sort the list
        sorted_common_list = sorted(common_list)
        return sorted_common_list
