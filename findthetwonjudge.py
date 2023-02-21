# 997. Find the Town Judge
# Easy
# 5.2K
# 417
# Companies
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
 

# Constraints:

# 1 <= n <= 1000
# 0 <= trust.length <= 104
# trust[i].length == 2
# All the pairs of trust are unique.
# ai != bi
# 1 <= ai, bi <= n
# Accepted
# 389.4K
# Submissions
# 783.3K
# Acceptance Rate
# 49.7%

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count=[0]*(n+1)
        
        for person1,person2 in trust:
            # is trusting someone so -1
            trust_count[person1]-=1
            # is trusted by someone so +1 
            trust_count[person2]+=1
        print(trust_count)

        # loop 1 through n +1
        for i in range(1,n+1):
            # if the trust count of the person is equal to n-1 :
            # n - 1 because we are counting everyone but the judge
            # if n = 3 we should check if the judge has a count of 2
            if trust_count[i]==n-1:
                # return the judge
                return i
        # if none of the people meet that condition, return -1
        return -1 
