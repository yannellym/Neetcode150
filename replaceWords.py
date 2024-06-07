648. Replace Words
Solved
Medium
Topics
Companies
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"


class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
  
        # [(0, u'the'), (1, u'cattle'), (2, u'was'), (3, u'rattled'), 
        # (4, u'by'), (5, u'the'), (6, u'battery')]
        sentence = [(i, word) for i, word in enumerate(sentence.split(" "))]
        k = len(sentence)

        for keyword in dictionary:
            for i in range(k):
    
                n = len(keyword)
                # if the keyword = the root of the selected word from sentence
                if keyword == sentence[i][1][:n]:
                    # make the selected word equal the index and root
                    sentence[i] = (i, keyword)
        return " ".join(word[1] for word in sentence)



# OR 

# Sort dictionary by length of words for shortest roots first
        dictionary.sort(key=len)
        
        # Convert sentence to list of words
        words = sentence.split()
        
        # For each word in the sentence
        for i, word in enumerate(words):
            # Check each dictionary word
            for root in dictionary:
                # If the root matches the start of the word, replace it
                if word.startswith(root):
                    words[i] = root
                    break
        
        # Join the sentence back together
        return " ".join(words)
