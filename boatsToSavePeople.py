# 881. Boats to Save People
# Medium
# 5.3K
# 122
# Companies
# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.

 

# Example 1:

# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# Example 2:

# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# Example 3:

# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
 

# Constraints:

# 1 <= people.length <= 5 * 104
# 1 <= people[i] <= limit <= 3 * 104
# Accepted
# 246.7K
# Submissions
# 442.2K
# Acceptance Rate
# 55.8%

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # sort the array so the heaviest people are on top
        people.sort()
        boats = 0
        i = 0
        j = len(people)-1

        # while i is less than or equal to j (there could be only one person left)
        while i <= j:
            # lets take our limit and subtract the heaviest person (we're essentially putting this person in the boat)
            remaining = limit - people[j]
            # increase the num of boats
            boats +=1
            # decrease j because we already put this certain heavy person in the boat
            j-=1
            # we have to check if the person we have on the left(lightest) can fit in the boat with the heaviest
            if  people[i] <= remaining:
                # if so, put them in the boat, and increment i to look at the next light person
                i+=1
        return boats
