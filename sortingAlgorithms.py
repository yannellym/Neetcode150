  # insertion sort O(n^2)
        '''
        iterate starting at 1 through the length of nums
        for i in range(1, len(nums)):
            # set the current index to i
            curr_idx = i
            # while the current index is greater than 0 AND the digit to the left is greater than the curr digit
            while curr_idx > 0 and (nums[curr_idx-1] > nums[curr_idx]):
                # swap them 
                nums[curr_idx], nums[curr_idx-1] = nums[curr_idx-1], nums[curr_idx]
                # decrease the current index to check all the previous values
                curr_idx -=1
        return nums
        '''

        # bubble sort O(n^2)
        # set the swapped flag to true
        '''
        has_swapped = True
        # while the flag is True
        while has_swapped:
            # set flag to false
            has_swapped = False
            # iterate i the length of nums-1
            for i in range(len(nums)-1):
                # iterate j the length of nums-1
                for j in range(len(nums)-1):
                    # if nums j is greater than nums j +1 
                    if nums[j] >nums[j+1]:
                        # swap them
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        # set flag to True
                        has_swapped = True
        return nums
        '''

        # selection sort O(n^2)
        '''
        size = len(nums)
        for step in range(size):
            min_idx = step
            for i in range(step + 1, size):
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
                if nums[i] < nums[min_idx]:
                    min_idx = i
            # put min at the correct position
            (nums[step], nums[min_idx]) = (nums[min_idx], nums[step])
        return nums
        '''
        
        # merge sort - O(n(log(n)))
        '''
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
      '''
