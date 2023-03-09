# 648. Replace Words
# Medium
# 1.9K
# 163
# Companies
# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

# Return the sentence after the replacement.

 

# Example 1:

# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# Example 2:

# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"
 

# Constraints:

# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case letters.
# 1 <= sentence.length <= 106
# sentence consists of only lower-case letters and spaces.
# The number of words in sentence is in the range [1, 1000]
# The length of each word in sentence is in the range [1, 1000]
# Every two consecutive words in sentence will be separated by exactly one space.
# sentence does not have leading or trailing spaces.
# Accepted
# 116.2K
# Submissions
# 185.4K
# Acceptance Rate
# 62.7%

 # split the sentence into words
        sentence = sentence.split(" ")
        # declar a list to hold our values
        hold = []

        # for every word in our sentence
        for word in sentence:
            # temp to hold our values
            temp = []
            # for every term in the dictionary
            for term in dictionary:
                # if the beginning of the word, which equals to the term length, is equal to term
                if word[:len(term)] == term:
                    # append it to temp
                    temp.append(term)
                else:
                    # if not, append the word to the temp
                    temp.append(word)
            #add the temp to our hold
            hold.append(temp)
        
        # res list will hold our answer
        res = []
        # for every subarray
        for sub in hold:
            # pick the minimum value of the sub and append it to res
            res.append(min(sub))
        # return everything by joining it together
        return ' '.join(res)
      
      
      # alternate solution 
      words = sentence.split()
        dic_set = set(dictionary)
        ans=[]
        
        for word in words:
            flag=False
            for i in range(len(word)):
                sub=word[:i+1]
                if sub in dic_set:
                    ans.append(sub)
                    flag=True
                    break
            
            if flag==False:
                ans.append(word)

        return " ".join(ans)
