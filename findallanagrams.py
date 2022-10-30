# https://www.youtube.com/watch?v=G8xtZy0fDKg&list=PLot-Xpze53leOBgcVsJBEGrHPd_7x_koV&index=5
def allAnagrams(s, p):
  win_start = 0
  sCount = {}
  pCount = {}

  if len(p) > len(s):
    return []

  #loop through the anagram
  for i in range(len(p)):
    # loop 3 times in this case
    # set both counts to be the count of the first 3 letters
    sCount[s[i]] = i + sCount.get(s[i], 0)
    pCount[p[i]] = i + pCount.get(p[i], 0)
  # if the above counts are the same, set the result to equal an array with 0. 
    # this will represent the array with initial indices of the matching anagrams
  # if not equal, set the result to an empty array as there is no matching anagram yet
  res = [0] if sCount == pCount else []
  # the first three were already checked so you just have to check the rest
  # start a loop from 3(the length of p) to 10(the length of s)
  for win_end in range(len(p), len(s)):
    # if the new character is in Scount, add 1 to it
      # if it is not in Scount, add it and set it to 0
    sCount[s[win_end]] = 1 + sCount.get(s[win_end], 0)
    # remove the character at the beginning of the window from sCount
    sCount[s[win_start]] -= 1

    # if the character at the beginning of the window in Scount = 0:
      # remove it from sCount so we get the correct count in the end
    if sCount[s[win_start]] == 0:
      sCount.pop(s[win_start])
      
    #increase win_start which is the beginning of the window
    win_start += 1
    # if the two counts are the same, append the starting index to the result
    if sCount == pCount:
      res.append(win_start)
allAnagrams("cbaebabacd", "abc")
