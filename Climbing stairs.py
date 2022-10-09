You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(self, n: int) -> int:
        if n<=2: return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
BigO

We iterate all dp array, it will cost O(n), each value will add up last two value as result, it will cost (1+2), in total will be O(n+2n) and It is O(n)
