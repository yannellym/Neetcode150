https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/


2259. Remove Digit From Number to Maximize Result
Solved
Easy
Topics
Companies
Hint
You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.

 

Example 1:

Input: number = "123", digit = "3"
Output: "12"
Explanation: There is only one '3' in "123". After removing '3', the result is "12".
Example 2:

Input: number = "1231", digit = "1"
Output: "231"
Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
Since 231 > 123, we return "231".
Example 3:

Input: number = "551", digit = "5"
Output: "51"
Explanation: We can remove either the first or second '5' from "551".
Both result in the string "51".
 

Constraints:

2 <= number.length <= 100
number consists of digits from '1' to '9'.
digit is a digit from '1' to '9'.
digit occurs at least once in number.
Seen this question in a real interview before?
1/4
Yes
No
Accepted
69.4K
Submissions
154.1K
Acceptance Rate
45.0%

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = float('-inf')

        for i, char in enumerate(number):
            if char == digit:
                lindex = number.rindex(char) 

                right= number[:i] + number[i+1:]
                res = max(res, int(right))
        
        return str(res)

