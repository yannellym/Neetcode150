# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

# Example 1:

# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Example 2:

# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# Example 3:

# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".




def charReplacement(str, k):
  count = {}
  res = 0
  win_start = 0

  for win_end in range(len(str)):
    r_char = str[win_end]
    count[r_char] = 1 + count.get(r_char, 0)
    while (win_end - win_start + 1) - max(count.values()) > k:
      count[str[win_start]] -= 1
      win_start += 1
    res = max(res, win_end - win_start + 1)
  print(res)
  

charReplacement("aabccbb",2)
