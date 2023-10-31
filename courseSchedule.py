207. Course Schedule
Solved
Medium
Topics
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
Accepted
1.4M
Submissions
3M
Acceptance Rate
46.3%

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # dfs
        # ex: {0: [], 1: []}
        preMap = {i: [] for i in range(numCourses)}


        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # ex {0: [], 1: [0]}
        
        visiting = set()

        # lets check for prerequesites 
        def dfs(crs):
            # if we already checked that course(its in visited), 
            # that means we have a cycle and cant finish all courses
            if crs in visiting:
                return False
            # if the prerequisite is empty, 
            # return true because we can complete all courses
            if preMap[crs] == []:
                return True
            # lets add the course to the visiting array
            visiting.add(crs)
            # for each prerequisite of the course in preMap
            for pre in preMap[crs]:
                # search to see if we can complete the prerequisite
                # if we can't complete it, return False
                if not dfs(pre):
                    return False
            # remove the course from visiting so we can move on to the next one
            visiting.remove(crs)
            # mark the course prerequsites as [] empty so we know it can be taken
            preMap[crs] = []
            # if we get to this point, we can return true
            return True

        # for every course in numCourses
        # we need to go through each because it might not be a connected  
        for c in range(numCourses):
            # if we look through the course's prerequesites and it returnes false, return False
            if not dfs(c):
                return False
        # else return true
        return True
   
