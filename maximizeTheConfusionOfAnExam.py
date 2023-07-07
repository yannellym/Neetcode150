# 2024. Maximize the Confusion of an Exam
# Medium
# 2.4K
# 34
# company
# Facebook
# company
# Amazon
# company
# Arcesium
# A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

# You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

# Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
# Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

 

# Example 1:

# Input: answerKey = "TTFF", k = 2
# Output: 4
# Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
# There are four consecutive 'T's.
# Example 2:

# Input: answerKey = "TFFT", k = 1
# Output: 3
# Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
# Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
# In both cases, there are three consecutive 'F's.
# Example 3:

# Input: answerKey = "TTFTTFTT", k = 1
# Output: 5
# Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
# Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
# In both cases, there are five consecutive 'T's.
 

# Constraints:

# n == answerKey.length
# 1 <= n <= 5 * 104
# answerKey[i] is either 'T' or 'F'
# 1 <= k <= n
# Accepted
# 79.9K
# Submissions
# 117.8K
# Acceptance Rate
67.8%

class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """

        store = {}
        win_s = 0 
        longest = 0

        # for every char in answerKey
        for win_e in range(len(answerKey)):
            # add it to the store and +1 to the count
            store[answerKey[win_e]] = 1 + store.get(answerKey[win_e], 0)
            # get the max value from the store's values
            max_val = max(store.values())
            # if the window's length - the maxvalue is greater than the value of k :
            while ((win_e - win_s + 1) - max_val) > k:
                # we need to subtract from the value at win_s index from answerkey in the store 
                store[answerKey[win_s]] -=1
                # make our window smaller
                win_s += 1
            # compute the longest window we have seen so far.
            longest = max(longest, win_e - win_s + 1)
        return longest
