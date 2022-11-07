# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# solution(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".

# Input/Output

# [execution time limit] 4 seconds (py)

# [input] string s1

# A string consisting of lowercase English letters.

# Guaranteed constraints:
# 1 ≤ s1.length < 15.

# [input] string s2

# A string consisting of lowercase English letters.

# Guaranteed constraints:
# 1 ≤ s2.length < 15.
  
 def solution(s1, s2):    
    dic1 = {}
    dic2 = {}
    res = 0
    
    for char in s1:
        if char not in dic1:
            dic1[char] = 0
        dic1[char] += 1
    
    for char in s2:
        if char not in dic2:
            dic2[char] = 0
        dic2[char] += 1
 
    for letter in dic1:
        if letter in dic2:
            res += min(dic1[letter], dic2[letter])
    return res


# dic1 = {
#     'a' : 2,
#     'b' : 1,
#     'c' : 2
# }

# dic2 = {
#     'a' : 3,
#     'd' : 1,
#     'c' : 1,
# }

# if i in dic1 and i in dic2:
# res += min(dic1[i], dic2[i])
