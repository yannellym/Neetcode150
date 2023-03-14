# 22. Generate Parentheses
# Medium
# 17.2K
# 695
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8
# Accepted
# 1.4M
# Submissions
# 1.9M
# Acceptance Rate
72.4%

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]


        # only add open parenthesis if open < n
        # only add a closing parenthesis if closed < open 
        # valif if open == closed == n
        """
        # create a list to store all of our subs
        res = []
        # the stack will the temporary parenthesis
        stack = []


        # helper func to backtrack
        def backtrack(openN, closedN):
            # if they're all the same number( Ex, n = 3 and they're all 3 now)
            if openN == closedN == n:
                # join the stack and append it to the res
                res.append(''.join(stack))
                # return so we can exit this func and move on to the next piece
                return
            # if the openN is less than n(our limit)
            if openN < n:
                # we can append an open parenthesis to the stack
                stack.append("(")
                # call backtrack and increase open by 1
                backtrack(openN+1, closedN)
                #pop the last one from the stack so we can clean up at calling the func
                stack.pop()
            # make sure that closedN is less than openN as we dont want to have more closed parenthesis as theyre not valid
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
        # call backtrack with both counts starting a 0
        backtrack(0,0)
        return res
            
            # fist: "((()))"
            # second: "(()())"

