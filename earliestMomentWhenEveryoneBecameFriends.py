
Code
Submissions
Submissions
Testcase
Testcase
Test Result
Test Result
Accepted
1101. The Earliest Moment When Everyone Become Friends
Solved
Medium
Topics
Companies
Hint
There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.

 

Example 1:

Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
Output: 20190301
Explanation: 
The first event occurs at timestamp = 20190101, and after 0 and 1 become friends, we have the following friendship groups [0,1], [2], [3], [4], [5].
The second event occurs at timestamp = 20190104, and after 3 and 4 become friends, we have the following friendship groups [0,1], [2], [3,4], [5].
The third event occurs at timestamp = 20190107, and after 2 and 3 become friends, we have the following friendship groups [0,1], [2,3,4], [5].
The fourth event occurs at timestamp = 20190211, and after 1 and 5 become friends, we have the following friendship groups [0,1,5], [2,3,4].
The fifth event occurs at timestamp = 20190224, and as 2 and 4 are already friends, nothing happens.
The sixth event occurs at timestamp = 20190301, and after 0 and 3 become friends, we all become friends.
Example 2:

Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
Output: 3
Explanation: At timestamp = 3, all the persons (i.e., 0, 1, 2, and 3) become friends.
 

Constraints:

2 <= n <= 100
1 <= logs.length <= 104
logs[i].length == 3
0 <= timestampi <= 109
0 <= xi, yi <= n - 1
xi != yi
All the values timestampi are unique.
All the pairs (xi, yi) occur at most one time in the input.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
94.8K
Submissions
145.8K
Acceptance Rate
65.0%

class Solution(object):
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int
        """
        '''
        [[20190101, 0, 1], [20190104, 3, 4], 
        [20190107, 2, 3], [20190211, 1, 5], 
        [20190224, 2, 4], [20190301, 0, 3], 
        [20190312, 1, 2], [20190322, 4, 5]]
        '''
        logs.sort(key= lambda x:x[0])

        # default dict so it wont throw an error
        graph = collections.defaultdict(set)

        # for every number in range n
        for num in range(n):
            # add it and its set with itself to graph
            '''
            defaultdict(<type 'set'>, {0: [0], 1: [1],
            2: [2], 3: [3], 4: [4], 5: [5]})
            '''
            graph[num] = {num}

        for timestamp, p1, p2 in logs:
            # adds to p1 all friends of p1 and p2
            graph[p1] = graph[p1].union(graph[p2])

            # we updated p1 now we need to let other acquantices know they have new friends
            for acquantice in graph[p1]:
                # it'll be their friends plus the new friends/acquantices
                graph[acquantice] = graph[acquantice].union(graph[p1])
            # if theres a person with n friends(including itself), everyone is acquainted
            if len(graph[1]) == n:
                return timestamp
        return -1
            
