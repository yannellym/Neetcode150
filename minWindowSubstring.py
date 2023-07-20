Min Window Substring
HIDE QUESTION
Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, the first parameter being the string N and the second parameter being a string K of some characters, and your goal is to determine the smallest substring of N that contains all the characters in K. For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string. So for this example your program should return the string dae.

Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is "aabd" which is located at the beginning of the string. Both parameters will be strings ranging in length from 1 to 50 characters and all of K's characters will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters.


1. For input ["aaabaaddae", "aed"] the output was incorrect. The correct output is dae

2. For input ["aabdccdbcacd", "aad"] the output was incorrect. The correct output is aabd

3. For input ["ahffaksfajeeubsne", "jefaa"] the output was incorrect. The correct output is aksfaje

4. For input ["aaffhkksemckelloe", "fhea"] the output was incorrect. The correct output is affhkkse

5. For input ["aaaaaaaaa", "a"] the output was incorrect. The correct output is a

6. For input ["aaffsfsfasfasfasfasfasfacasfafe", "fafe"] the output was incorrect. The correct output is fafe

7. For input ["aaffsfsfasfasfasfasfasfacasfafe", "fafsf"] the output was incorrect. The correct output is affsf

8. For input ["vvavereveaevafefaef", "vvev"] the output was incorrect. The correct output is vvave

9. For input ["caae", "cae"] the output was incorrect. The correct output is caae

10. For input ["cccaabbbbrr", "rbac"] the output was incorrect. The correct output is caabbbbr



def MinWindowSubstring(strArr):
    N, K = strArr

    # Create dictionaries to store character frequencies
    target_freq = {}
    window_freq = {}
    for char in K:
        target_freq[char] = target_freq.get(char, 0) + 1

    # Variables to track the window boundaries and the minimum substring
    left, right = 0, 0
    min_length = float('inf')
    min_substr = ""

    # Variable to track the number of characters remaining to find
    remaining_chars = len(K)

    while right < len(N):
        # Expand the window to the right and update the character frequency in the window
        if N[right] in target_freq:
            window_freq[N[right]] = window_freq.get(N[right], 0) + 1
            if window_freq[N[right]] <= target_freq[N[right]]:
                remaining_chars -= 1

        # Contract the window from the left if all characters in K are found in the window
        while remaining_chars == 0:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_substr = N[left:right + 1]

            if N[left] in target_freq:
                window_freq[N[left]] -= 1
                if window_freq[N[left]] < target_freq[N[left]]:
                    remaining_chars += 1

            left += 1

        right += 1

    return min_substr

# Test cases
print(MinWindowSubstring(["aaabaaddae", "aed"]))  # Output: "dae"
print(MinWindowSubstring(["aabdccdbcacd", "aad"]))  # Output: "aabd"
