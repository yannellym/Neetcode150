# Given a string, find the length of the longest substring which has no repeating characters.

# Example 1:

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".
# Example 2:

# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".

 
# 1 store()
# 2 store('a')
# 3 store('a', 'b')
# 4 store('a', 'b', 'c')
  # char in store so keep doing this while its inside store
  # 5 char = c is in store so remove a -> store('b', 'c')
  # 6 char = c is in store so remove b -> store('c')
  # 7 char = c is in store so remove c -> store()
  # 8 char = c is in store so remove c -> store()
  # 9 char = c NOT in store so ADD c -> store('c')
# 10 char = d NOT in store so ADD d -> store('c', 'd')
# 11 char = e NOT in store so ADD e -> store('c', 'd', 'e')

#both max lenghts were 3 so answer is 3


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
