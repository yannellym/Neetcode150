# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

# Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

# Example

# For sequence = [1, 3, 2, 1], the output should be
# solution(sequence) = false.

# There is no one element in this array that can be removed in order to get a strictly increasing sequence.

# For sequence = [1, 3, 2], the output should be
# solution(sequence) = true.

# You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].


def solution(sequence):
  def is_increasing(l):
    return all(l[i] > l[i - 1] for i in range(1, len(l)))

  if is_increasing(sequence):
    return True

  # Find non-increasing pair
  left, right = 0, 0
  for i in range(len(sequence) - 1):
    if sequence[i] >= sequence[i + 1]:
      left, right = i, i + 1
      break

  # Remove left element and check if it is strictly increasing
  if is_increasing(sequence[:left] + sequence[right:]):
    return True

  # Remove right element and check if it is strictly increasing
  if is_increasing(sequence[:right] + sequence[right + 1:]):
    return True

  return False

    
solution([1, 3, 2, 1])
