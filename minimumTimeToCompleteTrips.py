# 2187. Minimum Time to Complete Trips
# Medium
# 2K
# 119
# Companies
# You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

# Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

# You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.

 

# Example 1:

# Input: time = [1,2,3], totalTrips = 5
# Output: 3
# Explanation:
# - At time t = 1, the number of trips completed by each bus are [1,0,0]. 
#   The total number of trips completed is 1 + 0 + 0 = 1.
# - At time t = 2, the number of trips completed by each bus are [2,1,0]. 
#   The total number of trips completed is 2 + 1 + 0 = 3.
# - At time t = 3, the number of trips completed by each bus are [3,1,1]. 
#   The total number of trips completed is 3 + 1 + 1 = 5.
# So the minimum time needed for all buses to complete at least 5 trips is 3.
# Example 2:

# Input: time = [2], totalTrips = 1
# Output: 2
# Explanation:
# There is only one bus, and it will complete its first trip at t = 2.
# So the minimum time needed to complete 1 trip is 2.
 

# Constraints:

# 1 <= time.length <= 105
# 1 <= time[i], totalTrips <= 107
# Accepted
# 72K
# Submissions
# 190.6K
# Acceptance Rate

class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """

        # Sort the bus times in increasing order
        time.sort()
        
        # Set the time range within which we'll search for the minimum time
        left = 0
        # he right endpoint is the time taken by the fastest bus multiplied by totalTrips. This is an upper bound on the minimum time required, since if all buses complete totalTrips trips as fast as possible, this is the time it will take.
        right = time[0] * totalTrips
        
        # Perform binary search to find the minimum time
        while left < right:
            mid = (left + right) // 2
            # Calculate the total number of trips that can be completed within mid time
            num_trips = sum(mid // t for t in time)
            # If the total number of trips is less than totalTrips, increase the time range
            if num_trips < totalTrips:
                left = mid + 1
            # If the total number of trips is greater than or equal to totalTrips, decrease the time range
            else:
                right = mid
        
        # Return the minimum time required to complete totalTrips trips
        return left

# num_trips = sum(mid // t for t in time)
# This line of code calculates the total number of trips that can be completed within mid time, given the array of bus times time.

# Here's how it works:

# We use a generator expression to calculate mid // t for each bus time t in time. mid // t is the number of trips that can be completed by a single bus within mid time, rounded down to the nearest integer. For example, if t = 2 and mid = 5, then mid // t = 2, because a bus with time 2 can complete 2 trips in 5 time units, but not 3.
# We use the built-in sum() function to sum up the generator expression. This gives us the total number of trips that can be completed within mid time, across all buses.
# For example, suppose time = [1, 2, 3] and mid = 4. Then the generator expression will be (4 // 1, 4 // 2, 4 // 3), which evaluates to (4, 2, 1) after rounding down. The sum() function then adds up these values to give us 7, which is the total number of trips that can be completed within 4 time units across all buses.

# We use this num_trips value to determine whether we need to increase or decrease the time range in the binary search. If num_trips is less than totalTrips, we need to increase the time range because we haven't completed enough trips yet. If num_trips is greater than or equal to totalTrips, we need to decrease the time range because we've completed enough trips already.
