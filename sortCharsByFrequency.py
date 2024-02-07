451. Sort Characters By Frequency
Solved
Medium
Topics
Companies
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
Seen this question in a real interview before?
1/4
Yes
No
Accepted
579.9K
Submissions
819.8K
Acceptance Rate
70.7%

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # store = Counter(s)
        # x = sorted([(k,v) for k,v in store.items()], key=lambda x:-x[1])
   
        # res = ""
        # for k,v in x:
        #     res += k * v
        # return res

        # in the store, save the letter and the count of it from the str. 
        # we use a set so we dont save letters twice.
        store = {i : s.count(i) for i in set(s)}
        # sort the keys and values from store by the value that its highest.
        store = sorted(store.items(),key=lambda x:-x[1])
        # multiply each letter by its value, store in the array, then join and return 
        return ''.join([k*v for k,v in store])
        
