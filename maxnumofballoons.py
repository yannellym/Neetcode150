# 1189. Maximum Number of Balloons
# Easy

# 1216

# 76

# Add to List

# Share
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0
 

# Constraints:

# 1 <= text.length <= 104
# text consists of lower case English letters only.

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # create two hashmaps with the count values of each char in text or "balloon"
        word = Counter(text)
        balloon = Counter("balloon")
        
        # we set the res to equal the length of the text because it is impossible
        # to create more words than there are characters in text
        res = len(text)
        
        # look through the char object
        for char in balloon:
            # take the value of char from the word object and the balloon object.
             # floor division. 
             # choose the minimum between the res and the division. 
            # this will signify the least amount of words we can make from the text
            res = min(res, word[char] // balloon[char])
        return res
