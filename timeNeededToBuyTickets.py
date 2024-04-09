https://leetcode.com/problems/time-needed-to-buy-tickets/?envType=daily-question&envId=2024-04-09


2073. Time Needed to Buy Tickets
Solved
Easy
Topics
Companies
Hint
There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person at position k (0-indexed) to finish buying tickets.

 

Example 1:

Input: tickets = [2,3,2], k = 2
Output: 6
Explanation: 
- In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
- In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.
Example 2:

Input: tickets = [5,1,1,1], k = 0
Output: 8
Explanation:
- In the first pass, everyone in the line buys a ticket and the line becomes [4, 0, 0, 0].
- In the next 4 passes, only the person in position 0 is buying tickets.
The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.
 

Constraints:

n == tickets.length
1 <= n <= 100
1 <= tickets[i] <= 100
0 <= k < n
Seen this question in a real interview before?
1/5
Yes
No
Accepted
187.3K
Submissions
268.2K
Acceptance Rate
69.8%



class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        # count = 0

        # while tickets[k] != 0:
        #     for j in range(len(tickets)):
        #         if tickets[k] == 0:
        #             return count
        #         else:
        #             if tickets[j] == 0:
        #                 continue
        #             else:
        #                 tickets[j] = tickets[j] - 1
        #                 count +=1 
        # return count

        time = 0
        
        for i in range(len(tickets)):
            # If the current person is before or at the desired person 'k'
            if i <= k:
                # Buy the minimum of tickets available at person 'k' and the current person
                time += min(tickets[k], tickets[i])
            else:
                # If the current person is after 'k', buy the minimum of 
                # (tickets available at person 'k' - 1) and the current person
                time += min(tickets[k] - 1, tickets[i])
        
        return time
