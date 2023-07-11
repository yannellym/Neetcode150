def ArrayChallenge(strArr):
  # if the array is empty, let's return an empty string
  if strArr == []:
    return ""

  # create a list to keep track of our elements
  res = []
  # for every character in the array
  for char in strArr:
    # if the character is in res 
    if char in res:
      # get the first index of it in the array
      idx = res.index(char)
      # pop the first appereance of it
      res.pop(idx)
      # append it to the end
      res.append(char)
    # if not in the array
    else:
      # append it to the end
      res.append(char)

  # our LRU cache can hold up TO 5 ELEMENTS. 
  # if our cache is ever greater than 5: we use the last 5 items.
  if len(res) > 5:
    res = res[-5:]
  # join everything in the res array with a "-" and return the final string
  return "-".join(res)

# keep this function call here 
print ArrayChallenge(raw_input())
