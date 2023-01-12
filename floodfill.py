# 733. Flood Fill
# Easy
# 6.4K
# 619
# Companies
# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

 

# Example 1:


# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
# Example 2:

# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made to the image.
 

# Constraints:

# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 216
# 0 <= sr < m
# 0 <= sc < n
# Accepted
# 637.9K
# Submissions
# 1M
# Acceptance Rate


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        # get the number of rows and the number of columns. Ex. 3x3
        '''
        [
        -> columns
        [1,1,1]  -> row
        [1,1,0]  -> row
        [1,0,1]  -> row
        ]
        '''
        rows = len(image) 
        cols = len(image[0])

        # the color they want us to change the other colors to
        org_color = image[sr][sc]
        # if the color is the same as the new 
        if org_color == color: 
            return image

        # create a helper function to do depth first search
        # pass in the initial row, and colum coordinates. Example [1][1]  
        def dfs(r,c):
            # if the first coordinate is equal to the original color,
              # this means we can change it because it is the same color
            # this will also prevent the function from changing the color,
              # if the current coordinate doesnt equal the original color.
            if image[r][c] == org_color:
                # change the color to the new color
                image[r][c] = color

                # if the row is greater than 1 or 1, search underneath by doing r-1
                if r >= 1: dfs(r-1, c)      # top

                # if the row + 1 (the next row) is less than the amount of rows,
                  # (this means we're still within bounds), add one to the row
                if r +1 < rows: dfs(r+1, c) # down 


                #if the column is greater than or equal to 1, search to the left by doing c-1
                if c >= 1: dfs(r, c-1)    # left

                # if column plus 1 (the next column) is less than the amount of columns,
                  # (this means we're still within bounds), add one to the column
                if c +1 < cols: dfs(r, c+1) # right
        # call the function and pass the row and the colum initial coordiantes
        dfs(sr, sc)
        # return the modified image
        return image
