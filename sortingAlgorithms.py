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
