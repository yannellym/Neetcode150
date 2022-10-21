# Given a string, find the length of the longest substring which has no repeating characters.

# Example 1:

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".
# Example 2:

# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".

  
  def noRepeatingChars(str):
  max_length = 0
  store = set()
  win_start = 0

  for win_end in range(len(str)):
    while str[win_end] in store:
      store.remove(str[win_start])
      win_start += 1
    store.add(str[win_end])
    max_length = max(max_length, win_end - win_start + 1)
  print(max_length)

noRepeatingChars("aabccbb")
