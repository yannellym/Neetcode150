# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 

# Example 1:

# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"
# Example 2:

# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
 

# Constraints:

# 1 <= secret.length, guess.length <= 1000
# secret.length == guess.length

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls, cows = 0,0
        n = len(secret)
        cows_secret, cows_guess = {},{}
        # loop through nth amount of times 
        for i in range(n):
            # if the letter at index i in secret == the letter at index in guess:
             # add it to bulls count
            if(secret[i]==guess[i]):
                bulls+=1
            # if the letters are not tin the same index and not the same:
            else:
                # if the letter is not in cows_secret, add it else add 1 
                # if the letter is not in cows_guess, add it else add 1
                cows_secret[secret[i]] = 1 + cows_secret.get(secret[i], 0)
                cows_guess[guess[i]] = 1 + cows_guess.get(guess[i], 0)
        # for every digit in cows_secret
        for x in cows_secret:
            # if the digit is in guess
            if(x in cows_guess):
                # cows will equal cows + the min between the value at cows_secret and cows_guess
                cows = cows + min(cows_secret[x],cows_guess[x])
        # return the count
        return str(bulls)+"A"+str(cows)+"B"

# secret and guess consist of digits only.
