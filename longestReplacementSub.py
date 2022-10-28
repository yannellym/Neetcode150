def longSubRepeatingChars(s, k):
  count = {}
  res = 0
  win_start = 0

  for win_end in range(len(s)):
    # gets the count of of the char in count and adds 1
      # if char is not in count, it will add it and set it 0
    count[s[win_end]] = 1 + count.get(s[win_end], 0)
    
    # while the size of the window minus the max char value in count:
      # this is the number of replacements we can do 
      # if the number of replacements we can do is greather than or equal to               K(allowed replacements)
      # take the count of the char at the left position and subtract one
      # we can shift the left pointer(increment it
    
    while(win_end - win_start + 1) - max(count.values()):
    # choose the max count between res and the window size
      count[s[win_start]] -= 1
      win_start += 1
    res = max(res, win_end - win_start + 1)
  print(res)
   
  
longSubRepeatingChars("ABABBA", 2) # ->
# 0: count the frequency of the letters in the window set to Store
# 1: take the window length and subtract the count of the max letter in store
# 2: the above result will equal how many letters we can replace, set to num_of_replacements
# 3: as long as  num_of_replacements <= k:
  # we can make those replacements in the window
