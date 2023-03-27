# 659 Encoding and Decoding Strings
# algorithm
# medium
# Passing rate
# 63%
# topic
# answer20
# notes90
# discuss4
# ranking
# Record

# describe
# Design an algorithm to encode a list of strings into a string. The encoded strings are then sent over the network and decoded back to the original list of strings.
# Please implement encodeanddecode

# Face-to-face Raiders first exposure!
# Byte, Ali, Flax "Algorithm Template for Frequent Interview Tests"

# You can get it by adding [jiuzhang1104] remarks [frequently tested] on WeChat


# sample
# sample 1

# 输入： ["lint","code","love","you"]
# 输出： ["lint","code","love","you"]
# 解释：
# 一种可能的编码方式为： "lint:;code:;love:;you"
# sample 2

# 输入： ["we", "say", ":", "yes"]
# 输出： ["we", "say", ":", "yes"]
# 解释：
# 一种可能的编码方式为： "we:;say:;:::;yes


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        # for every letter in s
        for s in strs:
            # to the res, add the length of the word as a str, the hashpound, and the word
            res += str(len(s)) + "#" + s
        return res
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = []
        i = 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j +=1
                # get the length of the string. The number you added previously
                # ex "4#lint4#code4#love3#you" it will be 4
            length = int(str[i:j])
            # gets the entire word decoded
            res.append(str[j+1: j +1 + length])
            # now we update i to be the end of the curr word plus 1
            i = j + 1 + length
        return res
