
# Given a string, find the length of the longest substring which has no repeating characters.



def lengthoflongestsub(str):
  store = set()
  res = 0
  win_start = 0

  for win_end in range(len(str)):
    while str[win_end] in store:
      store.remove(str[win_start])
      win_start += 1
    store.add(str[win_end])
    res = max(res, win_end - win_start + 1)
  print(res)
  return res

lengthoflongestsub('abccde')
  
