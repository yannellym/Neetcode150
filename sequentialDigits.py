
Code
Testcase
Testcase
Test Result
1291. Sequential Digits
Solved
Medium
Topics
Companies
Hint
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
Seen this question in a real interview before?
1/4
Yes
No
Accepted
93.4K
Submissions
152.3K
Acceptance Rate
61.3%

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
         # Initialize an empty list to store the result
        res = []
        
        # Define a string of digits for easy access
        digits = "123456789"

        # Get the length of low and high
        low_len = len(str(low))
        high_len = len(str(high))

        # Iterate through all possible lengths of sequential digits
        for length in range(low_len, high_len + 1):
            # Iterate through all possible starting positions
            for start in range(0, 10 - length):
                # Extract the substring and convert it to an integer
                print(int(digits[start : start + length]))
                num = int(digits[start : start + length])
                
                # Check if the generated number is within the given range
                if low <= num <= high:
                    # Add the valid number to the result list
                    res.append(num)

        # Return the final result
        return res

        # The reason for using 10 is that we are working with decimal digits (0 to 9).
        #  So, the loop starts from 0 and goes up to (but not including) the maximum 
        #  possible starting digit for the given length. In the case of length 3, 
        #  we want to avoid starting with a digit that would make the sequence go 
        #  beyond 9 (e.g., starting with 8 and trying to generate a 3-digit sequence
        #  would result in 789, which is not a valid sequential digit).
