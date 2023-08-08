You have two integer arrays, a and b, and an integer target value v. Determine whether there is a pair of numbers, where one number is taken from a and the other from b, that can be added together to get a sum of v. Return true if such a pair exists, otherwise return false.

Example

For a = [1, 2, 3], b = [10, 20, 30, 40], and v = 42, the output should be
solution(a, b, v) = true.

Input/Output

[execution time limit] 4 seconds (py)

[memory limit] 1 GB

[input] array.integer a

An array of integers.

Guaranteed constraints:
0 ≤ a.length ≤ 105,
-109 ≤ a[i] ≤ 109.

[input] array.integer b

An array of integers.

Guaranteed constraints:
0 ≤ b.length ≤ 105,
-109 ≤ b[i] ≤ 109.

[input] integer v

Guaranteed constraints:
-109 ≤ v ≤ 109.

[output] boolean

true if there are two elements from a and b which add up to v, and false otherwise.

[Python 2] Syntax Tips
  
  def solution(a, b, v):
    a.sort()
    b.sort()
    
    left = 0
    right = len(b) - 1
    
    while left < len(a) and right >= 0:
        current_sum = a[left] + b[right]
        if current_sum == v:
            return True
        elif current_sum < v:
            left += 1
        else:
            right -= 1
    
    return False
