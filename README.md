
The file 'profanity-check!' consists of python code that imports data from a text file containing tweets by various users and checks for degree of profanity of each sentence of the tweets.
The racial slurs set is given as well.
Assumptions-
  1. It is assumed that each sentence/tweet is in an individual line in the file.
  2. The provided set of words indicating racial slurs is defined in the 'profane_words' set in the beginning of the program itself.

I've defined 2 ways of finding the degree of profanity for a sentence and both of them works well.
'method1' finds the degree if the words of sentences are normal.
'method2' finds the degree if the racial slurs are present in a sentence in an indirect way. (Mentioned in the code)

The validity of 'method2' can be checked by replacing a few of the letters in the profane words of a tweet/sentence with '\*'.
Ex. - if 'qwerty' is a profane word in the tweet, replace it with 'qw*\*\*y' in the tweet itself. 'method2' would still identify it as a racial slur!
