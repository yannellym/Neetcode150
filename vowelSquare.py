# Vowel Square
# HIDE QUESTION
# Have the function VowelSquare(strArr) take the strArr parameter being passed which will be a 2D matrix of some arbitrary size filled with letters from the alphabet, and determine if a 2x2 square composed entirely of vowels exists in the matrix. For example: strArr is ["abcd", "eikr", "oufj"] then this matrix looks like the following:

# a b c d
# e i k r
# o u f j

# Within this matrix there is a 2x2 square of vowels starting in the second row and first column, namely, ei, ou. If a 2x2 square of vowels is found your program should return the top-left position (row-column) of the square, so for this example your program should return 1-0. If no 2x2 square of vowels exists, then return the string not found. If there are multiple squares of vowels, return the one that is at the most top-left position in the whole matrix. The input matrix will at least be of size 2x2.

def is_vowel(char):
    return char.lower() in 'aeiou'

def VowelSquare(strArr):
    rows = len(strArr)  # Get the number of rows in the matrix
    cols = len(strArr[0])  # Get the number of columns in the matrix

    # Iterate through each 2x2 submatrix
    for i in range(rows - 1):  # Stop at the second-to-last row
        for j in range(cols - 1):  # Stop at the second-to-last column
            # Check if all four characters in the submatrix are vowels
            if is_vowel(strArr[i][j]) and is_vowel(strArr[i][j+1]) and is_vowel(strArr[i+1][j]) and is_vowel(strArr[i+1][j+1]):
                # If a valid submatrix is found, return its top-left position as a string
                return "{}-{}".format(i, j)

    # If no valid 2x2 submatrix with all vowels is found, return "not found"
    return "not found"
'''
is_vowel(strArr[i][j+1]): This checks if the character at position (i, j+1) is a vowel. 
strArr[i][j+1] represents the character in the same row (i) but one column to the right (j+1).

is_vowel(strArr[i+1][j]): This checks if the character at position (i+1, j) is a vowel. strArr[i+1][j] 
represents the character in the row below (i+1) but in the same column (j).

is_vowel(strArr[i+1][j+1]): This checks if the character at position (i+1, j+1) is a vowel. strArr[i+1][j+1] 
represents the character in the row below (i+1) and one column to the right (j+1).

In the context of the problem, the function is checking if the 2x2 submatrix:

strArr[i][j]     strArr[i][j+1]
strArr[i+1][j]   strArr[i+1][j+1]
contains all vowels. If all four characters in this submatrix are vowels, it means there is a 2x2 square composed entirely of vowels
in the matrix, and the function returns the top-left position of that submatrix as a string (in the format "{row}-{column}").
Otherwise, it continues searching for other possible 2x2 submatrices until it finds a valid one or concludes that there is no 
such submatrix with all vowels.
'''

# alternative

def MatrixChallenge(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    vowels = set("aeiou")
    found_squares = []

    def dfs(r, c, visited):
        if (
            r + 1 >= rows
            or c + 1 >= cols
            or matrix[r][c] not in vowels
            or matrix[r + 1][c] not in vowels
            or matrix[r][c + 1] not in vowels
            or matrix[r + 1][c + 1] not in vowels
            or (r, c) in visited
        ):
            return

        visited.add((r, c))
        found_squares.append((r, c))

        dfs(r - 1, c, visited)
        dfs(r + 1, c, visited)
        dfs(r, c - 1, visited)
        dfs(r, c + 1, visited)

    for r in range(rows):
        for c in range(cols):
            visited = set()
            if matrix[r][c] in vowels:
                dfs(r, c, visited)

    if not found_squares:
        return "not found"

    return found_squares[0]

# Test cases
print(MatrixChallenge(["aeeei", "aeiou", "iiiiu"]))  # Output: (0, 1)
print(MatrixChallenge(["xyz", "aeiou", "pqr"]))     # Output: not found
