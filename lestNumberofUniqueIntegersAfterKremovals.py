1481. Least Number of Unique Integers after K Removals
Solved
Medium
Topics
Companies
Hint
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
Seen this question in a real interview before?
1/4
Yes
No
Accepted
113K
Submissions
200.3K
Acceptance Rate
56.4%


class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        # store = Counter(arr)

        # kvalues = sorted([[x,y] for x,y in store.items()], key=lambda x:x[1])
     

        # for i in range(1,k+1):
        #     if kvalues[0][1] == 0:
        #         kvalues.pop(0)

        #     if kvalues[0][1] > 0:
        #         kvalues[0][1] -= 1
        #     else:
        #         kvalues.pop(0)
   
        # return len([v for k,v in kvalues if v > 0])

        # alternative

        freq_map = Counter(arr)

        sorted_freq = sorted(freq_map.items(), key=lambda x: x[1])

        for num, freq in sorted_freq:
            if k >= freq:
                k -= freq
                del freq_map[num]
            else:
                break

        return len(freq_map)
