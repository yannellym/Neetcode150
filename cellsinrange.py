# 2194. Cells in a Range on an Excel Sheet
# Easy

# 263

# 42

# Add to List

# Share
# A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:

# <col> denotes the column number c of the cell. It is represented by alphabetical letters.
# For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
# <row> is the row number r of the cell. The rth row is represented by the integer r.
# You are given a string s in the format "<col1><row1>:<col2><row2>", where <col1> represents the column c1, <row1> represents the row r1, <col2> represents the column c2, and <row2> represents the row r2, such that r1 <= r2 and c1 <= c2.

# Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2. The cells should be represented as strings in the format mentioned above and be sorted in non-decreasing order first by columns and then by rows.

 

# Example 1:


# Input: s = "K1:L2"
# Output: ["K1","K2","L1","L2"]
# Explanation:
# The above diagram shows the cells which should be present in the list.
# The red arrows denote the order in which the cells should be presented.
# Example 2:


# Input: s = "A1:F1"
# Output: ["A1","B1","C1","D1","E1","F1"]
# Explanation:
# The above diagram shows the cells which should be present in the list.
# The red arrow denotes the order in which the cells should be presented.
 

# Constraints:

# s.length == 5
# 'A' <= s[0] <= s[3] <= 'Z'
# '1' <= s[1] <= s[4] <= '9'
# s consists of uppercase English letters, digits and ':'.

1	def cellsInRange(s):
2	    lis = [] 
3	    i = ord(s[0])
4	    while i <= ord(s[3]):
5	        for j in range(int(s[1]),int(s[4])+1):
6	            lis.append(chr(i)+str(j))
7	        i += 1
8	    return lis
9	    
10	cellsInRange("K1:L2")

# first declare a list
# declare i which will be the unicode of the first char in the s string
# while i is less than or equal to the 4th char in s, do the following:
# loop for the range of (the second char in s), and (the and the 5th char in s)
# append to list declared earlier ( char of value of i + the number represented by j as a string
# increase i by one
# return the list
