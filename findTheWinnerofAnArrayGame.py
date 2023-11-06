

Code

Testcase
Testcase
Test Result

1535. Find the Winner of an Array Game
Solved
Medium
Topics
Companies
Hint
Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.

 

Example 1:

Input: arr = [2,1,3,5,4,6,7], k = 2
Output: 5
Explanation: Let's see the rounds of the game:
Round |       arr       | winner | win_count
  1   | [2,1,3,5,4,6,7] | 2      | 1
  2   | [2,3,5,4,6,7,1] | 3      | 1
  3   | [3,5,4,6,7,1,2] | 5      | 1
  4   | [5,4,6,7,1,2,3] | 5      | 2
So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.
Example 2:

Input: arr = [3,2,1], k = 10
Output: 3
Explanation: 3 will win the first 10 rounds consecutively.
 

Constraints:

2 <= arr.length <= 105
1 <= arr[i] <= 106
arr contains distinct integers.
1 <= k <= 109
Accepted
97.6K
Submissions
169.5K
Acceptance Rate
57.6%

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # Find the maximum element in the array
        max_element = max(arr)
        # Initialize the current winner and their win streak
        curr = arr[0]
        winstreak = 0

        # Iterate through the array starting from the second element
        for i in range(1, len(arr)):
            opponent = arr[i]

            # Check if the current winner has won another round
            if curr > opponent:
                winstreak += 1
            else:
                # Update the current winner and reset the win streak
                curr = opponent
                winstreak = 1

            # Check if the current winner has won k consecutive rounds or if they are the maximum element
            '''
            We can make another observation: let the player with the largest value in arr be maxElement. Since the 
            elements in the array are all unique, this player will never lose a round, so if the current player ever 
            becomes maxElement, it will surely end up winning so many games as long as the simulation continues, no 
            matter how large the required k is. Thus, if curr = maxElement, we can immediately return curr without 
            actually simulating all the games, because we know that all future games will result in curr winning!
            '''
            if winstreak == k or curr == max_element:
                return curr

        # Return the winner
        return curr
