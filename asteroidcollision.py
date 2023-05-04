# 735. Asteroid Collision
# Medium
# 5K
# 452
# Companies
# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

# Constraints:

# 2 <= asteroids.length <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0
# Accepted
# 269.6K
# Submissions
# 606.2K
# Acceptance Rate

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """


        stack = []

        for num in asteroids:
            # if theres a stack, the curr asteroid is < 0 and the num at the stack is positive:
            while stack and num < 0 and stack[-1] > 0:
                # take the diff when you add the curr num to the num at the stack
                diff = num + stack[-1]
                # if the diff is less than 0
                if diff < 0:
                    # this means that the negative value wins, so we need to pop
                    stack.pop()
                # if the diff is greater than 0, it means the positive val wins, we set num to 0
                # num is set to 0 so the loop stops executing
                elif diff > 0:
                    num = 0
                # if they're equal 
                else:
                    # destory botha steroids
                    num = 0
                    stack.pop()
            # if the num is greater than 0, add it to the stack
            if num:
                stack.append(num)
        return stack
                    
