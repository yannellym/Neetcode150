# Implement the function compute_closest_to_zero(ts) which takes an array of temperatures ts and returns the temperature closest to 0.
 
 
# Constraints:
# If the array is empty, the function should return 0
# 0 ≤ ts size ≤ 10000
# If two temperatures are equally close to zero, the positive temperature must be returned. For example, if the input is -5 and 5, then 5 must be returned.


def compute_closest_to_zero(ts):
    if not ts:  # empty array case
        return 0
      # chooses the first element in ts
    closest = ts[0]
    
    # iterate through ts
    for t in ts:
      # if the absolute value of t is less than the absolute value of closest OR
      # abs of t is equal to abs of closest and t is greater than closest 
        if abs(t) < abs(closest) or (abs(t) == abs(closest) and t > closest):
          # have closest equal t
            closest = t
    return closest
  
 temperatures = [4, -2, 5, -1, -3, 2, -4, 1, 3, -5]
closest_temp = compute_closest_to_zero(temperatures)
print("The temperature closest to 0 is:", closest_temp)
