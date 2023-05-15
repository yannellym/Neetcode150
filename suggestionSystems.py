# 1268. Search Suggestions System
# Medium
# 4.1K
# 194
# Companies
# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return a list of lists of the suggested products after each character of searchWord is typed.

 

# Example 1:

# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
# Example 2:

# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
# Explanation: The only word "havana" will be always suggested while typing the search word.
 

# Constraints:

# 1 <= products.length <= 1000
# 1 <= products[i].length <= 3000
# 1 <= sum(products[i].length) <= 2 * 104
# All the strings of products are unique.
# products[i] consists of lowercase English letters.
# 1 <= searchWord.length <= 1000
# searchWord consists of lowercase English letters.
# Accepted
# 246.3K
# Submissions
# 372.2K
# Acceptance Rate
# 66.2%

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        res = []
        # sort the product arr
        products.sort()

        l = 0
        r = len(products)-1

        # for each letter in search word
        for i in range(len(searchWord)):
            # choose the letter 
            c = searchWord[i]
            # ** products at left
            # l <= r and the curr word in products has a length >= i (not within range)
            # while the product doesnt have an ith char or the ith char dosnt equal c
            
             '''
            len(products[l]) <= i: This condition checks if the length of the string at index l 
            in the products list is less than or equal to i. Here, i represents the index of the
            current character being processed in searchWord. This condition ensures that the length 
            of the string is sufficient to compare characters up to the current index i.
            '''
             
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                # increase until we have looked at all words or we found a matching prefix
                l +=1
            # ** products at right
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                # increase until we have looked at all words or we found a matching prefix
                r-=1

            res.append([])
            # the size of our window
            remain = (r-l)+1
            # iterate ith times (i is the mimimum between 3 or the length of letter remaining)
            for j in range(min(3, remain)):
                # to the arr we appended, add the qualifying words 
                res[-1].append(products[l+j])
        return res
https://www.youtube.com/watch?v=D4T2N0yAr20
