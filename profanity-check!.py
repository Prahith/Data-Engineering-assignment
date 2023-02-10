# Steps I would follow -

# Step-1. I'll change each one of the given set of profane words into lower case as
#    it will negate the case-sensitivity of the words (Obviously, any profane word in upper-case is still profane!)
profane_words = {'Abc', 'HfREcs', 'dfjd',
                 'JHF'}  # The provided set of words (The way these words are provided is not mentioned, so I took an example.)
profane_words1 = set()  # set containing new lowercase profane words
for w in profane_words:
    profane_words1.add(w.lower())

# 2. I'll import the contents of the twitter tweets file using file handling methods.
file = open('tweets.txt', 'r')
tweets = file.readlines()  # Assuming each sentence/tweet in the file is in a separate line.


# 3. The degree of profanity of each sentence is equal to the ratio of no. of profane words in a sentence
# to the total no. of words in the sentence.
def method1():
    profanity_degree = dict()
    # The sentence and it's profanity degree is stored in a dictionary where the sentence is the key and it's
    # corresponding value is the degree.
    for tweet in tweets:
        words = tweet.split()  # storing each word of the sentence in a list
        # changing the words to lowercase (reason being the same as before)
        for i in range(len(words)):
            words[i] = words[i].lower()
        no_of_profane_words = 0
        for w in words:
            if w in profane_words1:
                no_of_profane_words += 1
        degree = no_of_profane_words / len(words)
        profanity_degree[tweet] = degree

    for k, v in profanity_degree.items():
        print(k, v)


#        --- Further optimization --- (Because it struck my mind it!)
# As twitter users are being clever and they're getting to know how this program works,
# they're replacing a few letters of a profane word with '*'.

# The above program fails to identify these words as profane. Well, we as programmers being cleverer,
# we can identify these words by finding the longest common subsequence(lcs) of each word of a sentence and
# the given set of profane words. If they match closely, i.e. if
# (length of lcs + no. of '*') is equal to the length of the profane word, we can classify it to be profane as well!!!

# Ex- if the profane word is 'qwerty', then 'qw***y' is typed in the sentence.
# Here, lcs of 'qwerty' and 'qw***y' is 'qwy' and no. of '*' is 3.
# len(qwy) + 3 == len(qwerty). Hence, we can know it is a profane word.

# The below function returns the length of lcs of 2 strings s1, s2 and the number of '*' in s1.
def lcs(s1, s2):
    memo = [[0 for i in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    no_of_star = 0
    for i in range(1, len(s1) + 1):
        if s1[i - 1] == '*': no_of_star += 1
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                memo[i][j] = memo[i - 1][j - 1] + 1
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
    return memo[len(s1)][len(s2)], no_of_star


# making minor changes to method1
def method2():
    profanity_degree = dict()

    for tweet in tweets:
        words = tweet.split()
        for i in range(len(words)):
            words[i] = words[i].lower()
        no_of_profane_words = 0
        for s1 in words:
            for s2 in profane_words1:
                len_of_lcs, no_of_star = lcs(s1, s2)
                if len_of_lcs + no_of_star == len(s2):
                    no_of_profane_words += 1
        degree = no_of_profane_words / len(words)
        profanity_degree[tweet] = degree

    for k, v in profanity_degree.items():
        print(k, v)


print('Method1')
method1()  # Normal one
print('\n\n')
print('Method2')
method2()  # Optimized method to identify profane words with '*' as well

#            ---Further further optimization--- (only the process)
# This optimization is only for faster run-time in case of lakhs of tweets.
# In method2, we are going through each word in the 'profane_words1' set for each iteration of
# 'words' list.
# Instead, a trie data structure can be used to store the profane words first and can be checked whether
# each word of a sentence exists in the trie. I understand this might be over
