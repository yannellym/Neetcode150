You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.

Example

For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
solution(a, b) = [9876, 5434, 0].

Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
solution(a, b) = [223, 104, 105].

Explanation: 12300040005 + 10001000100 = 22301040105.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer a

The first number, without its leading zeros.

Guaranteed constraints:
0 ≤ a size ≤ 104,
0 ≤ element value ≤ 9999.

[input] linkedlist.integer b

The second number, without its leading zeros.

Guaranteed constraints:
0 ≤ b size ≤ 104,
0 ≤ element value ≤ 9999.

[output] linkedlist.integer

The result of adding a and b together, returned without leading zeros in the same format.

[Python 3] Syntax Tips

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def get_padded_string(num):
    selected = str(num)
    while len(selected) < 4:
        selected = "0" + selected
    return selected

def solution(a, b):
    l1 = a
    l2 = b
    res1 = ""
    res2 = ""

    while l1:
        selected = get_padded_string(l1.value)
        res1 += selected
        l1 = l1.next

    while l2:
        selected = get_padded_string(l2.value)
        res2 += selected
        l2 = l2.next
        

    new_val = int(res1) + int(res2) # 987654340000

     # Convert the result back to list of integers
    if new_val == 0:
        return [0]
    
    f_res = []
    
    while new_val > 0:
        sub_value = new_val % 10000 # calculates the remainder of dividing new_val 
                                #by 10000. This gives you the last 4 digits of new_val
        f_res.append(sub_value)
        new_val //= 10000
    
    return f_res[::-1]
    
    
    '''
    988994340000 % 10000 = 4000
    988994340000 // 10000 = 98899434

    98899434 % 10000 = 9434
    98899434 // 10000 = 9889

    9889 % 10000 = 9889
    9889 // 10000 = 0
    
    Three groups of digits are extracted: [0, 9876, 5434, 0]

    Step 2: Reversing the Result List

        f_res = [0, 9876, 5434, 0]

        Reversed result: [0, 5434, 9876, 0]

    '''
