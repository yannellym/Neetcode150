
Code
Testcase
Testcase
Test Result
Test Result
Accepted
1550. Three Consecutive Odds
Solved
Easy
Topics
Companies
Hint
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
Seen this question in a real interview before?
1/5

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # keep track of the number of odds we encounter
        odd_total = 0 
        # keep track of the begining of the window
        win_s = 0

        # look through each number in arr
        for win_end in range(len(arr)):
            # if its odd, add 1 to our odd count
            if arr[win_end] % 2 != 0:
                odd_total +=1
            # if the size of our window is 3
            if ((win_end - win_s) + 1) == 3:
                # and our count of odd total is 3
                if odd_total == 3:
                    return True
                # if the beginning of our window is odd
                if arr[win_s] % 2 != 0:
                    # subtract  1 from our odd total since our 
                    # window will be smaller now
                    odd_total -= 1
                # shrink our window
                win_s += 1
        # if we don't find any 3 consecutive odd numbers, return false
        return False

