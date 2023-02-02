# 599. Minimum Index Sum of Two Lists
# Easy
# 1.6K
# 367
# Companies
# Given two arrays of strings list1 and list2, find the common strings with the least index sum.

# A common string is a string that appeared in both list1 and list2.

# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

# Return all the common strings with the least index sum. Return the answer in any order.

 

# Example 1:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only common string is "Shogun".
# Example 2:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
# Example 3:

# Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
# Output: ["sad","happy"]
# Explanation: There are three common strings:
# "happy" with index sum = (0 + 1) = 1.
# "sad" with index sum = (1 + 0) = 1.
# "good" with index sum = (2 + 2) = 4.
# The strings with the least index sum are "sad" and "happy".
 

# Constraints:

# 1 <= list1.length, list2.length <= 1000
# 1 <= list1[i].length, list2[i].length <= 30
# list1[i] and list2[i] consist of spaces ' ' and English letters.
# All the strings of list1 are unique.
# All the strings of list2 are unique.
# There is at least a common string between list1 and list2.
# Accepted
# 181.3K
# Submissions
# 341.5K
# Acceptance Rate
# 53.1%

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """ 
        store = {}
        res = []
        # for every word in list1
        for word1 in list1:
            # if the word is in list2
            if word1 in list2:
                # store the sum of the index in a dictionary:
                # with the word being the key and sum being the value
                store[word1] = list1.index(word1) + list2.index(word1)
        # find the min value amongst all values
        mini = min(store.values())
        # for every word and value in the store's items
        for word,value in store.items():
            # if the value equals the min value we idenfitied 
            if value == mini:
                # append its key to the res array
                res.append(word)
        # return the res array with the min values
        return res
