# 912. Sort an Array
# Medium
# 4.2K
# 650
# Companies
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104
# Accepted
# 405.7K
# Submissions
# 683.1K
# Acceptance Rate
# 59.4%


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(arr, L, M, R):
            # get the left, and right array (so we don't modify nums)
            left, right = arr[L:M+1], arr[M+1:R+1]
            # create 3 pointers, 
            # i will point to nums, j starts at 0(of left), and k at 0(of left)
            i, j, k = L, 0, 0
            # while both pointers are within bounds
            while j < len(left) and k < len(right):
                # if the number at the left is less than or equal to the one on the right
                if left[j] <= right[k]:
                    # have the number in arr equal the number on the left
                    arr[i] = left[j]
                    # increase the left pointer
                    j +=1
                else:
                    # have the number in arr equal the number on the right
                    arr[i] = right[k]
                    # increase the right pointer
                    k+=1
                # increase i regardless because we want to look at all the digits in arr
                i+=1
            # if we still have digits left from our splitted arrs, lets merge them

            # if we have digits in the left arr, we need to address this
            # one of these while loops will execute
            
            # while j is less than left
            while j <len(left):
                # have the digit at arr equal the digit at left
                arr[i] = left[j]
                # increase i to move on to the next digit in left
                j += 1
                # increase i to move on to the next digit in arr
                i += 1
            while k <len(right):
                # have the digit at arr equal the digit at right
                arr[i] = right[k]
                # increase j to move on to the next digit in right
                k+=1
                # increase i to move on to the next digit in arr
                i +=1

        def mergeSort(arr, l, r):
            # if our arr is of length 1: return the arr
            if l == r:
                return arr

            # get the mid of the arr
            m = (l+r) //2
            # call mergeSort on the left half of array
            mergeSort(arr, l, m)
            # call mergeSort on the right half of array
            mergeSort(arr, m+1, r)
            # call the merge func on the arr by passing in the l, m, and r.
            merge(arr, l, m, r)
            # return the merged array
            return arr
        # call the mergerSort helper func:
        # pass in the arr, 0 to start, and len of nums-1 as the end
        return mergeSort(nums, 0, len(nums)-1)


# alternative 

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # merge sort algo to break down nums and compare it to the element level.
        return self.mergeSort(0, len(nums)-1, nums)  

    def merge(self, L, M , R, nums):
        left = nums[L:M+1] 
        right = nums[M+1:R+1]

        i, j, k = L, 0,0
        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                nums[i] = left[j]
                j +=1
            else:
                nums[i] = right[k]
                k += 1
            i +=1

        while j < len(left):
            nums[i] = left[j]
            j+=1
            i +=1
        
        while k < len(right):
            nums[i] = right[k]
            k+=1
            i +=1
        
        return nums




    def mergeSort(self,l, r, nums):

        if l == r:
            return nums

        mid = (l+r) //2

        self.mergeSort(l,mid, nums)
        self.mergeSort(mid+1, r, nums)
        res = self.merge(l, mid, r, nums)
        return res 

        

         
