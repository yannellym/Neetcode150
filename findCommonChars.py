# 1002. Find Common Characters
# Easy
# 2.9K
# 240
# Companies
# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.
# Accepted
# 173.4K
# Submissions
# 253.3K
# Acceptance Rate
# 68.4%

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Step 1: count all letter in first word, save result in hash table "count"
        # Step 2: for each letter in first word, check if it exists in all the rest words, if exist:
        # Step 3: find the min counts for that letter, and overwrite the count value in hash table. if doesn't exist:
        # Step 4: overwrite the count of that letter to 0, and break the inner loop
        # Step 5: define an empty list l, for all the letter in hash table, use the l+= [letter] *count to generate final answer
        count = {}
        for x in words[0]:
            count[x] = count.get(x, 0) + 1
            
        
        for x in count:
            for i in range(1,len(words)):
                if x in words[i]:
                    count[x] = min(count[x], words[i].count(x))
                    
                else:
                    count[x] = 0
                    break
        
        ans = []
        for k,v in count.items():
            ans += v * [k]
        return ans

# The last for loop is responsible for generating the final output of the function. It loops through the key-value pairs in the count dictionary, which was created in the first for loop and modified in the second for loop. For each key-value pair, the loop generates a list of the letter (k) repeated v times, where v is the value of the key-value pair. This is done using the expression [k] * v, which creates a list containing v copies of k. The resulting lists are concatenated using the += operator and added to the ans list. Finally, the ans list is returned as the output of the function.
