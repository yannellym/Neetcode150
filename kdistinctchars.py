# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Example 1:

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
# Example 2:

# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".
# Example 3:

# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".



def kDistinctChars(str, k):
  store = {}
  win_start = 0
  char_len = 0

  for win_end in range(len(str)):
    r_char = str[win_end]
    if r_char not in store:
      store[r_char] = 0
    store[r_char] += 1

    while len(store) > k:
      l_char = str[win_start]
      store[l_char] -= 1
      if store[l_char] == 0:
        del store[l_char]
      win_start += 1
    char_len = max(char_len, win_end - win_start + 1)
  print(char_len)
      
    
kDistinctChars('araaci', 2)
