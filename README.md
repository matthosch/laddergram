# laddergram

# There is a game called Laddergrams which takes two words of the same length and
# challenges humans to find the shortest sequence of words going from the first word
# to the last word while changing only one letter at a time. For example, with the words 
# COLD and WARM, the shortest sequence is 5:
# COLD -> CORD -> CARD -> WARD -> WARM
# Note that other word sequences are possible to complete the laddergram.
# Given two words (first and last) of the same length and a list of valid words,
# return one of the shortest sequences from the first word to the last word.

# Clarifications:
# Q: Could there be multiple equal length sequences?
# A: Yes. Just return any one of the shortest ones.
# Q: Should the first and last words be part of the answer?
# A: Yes.
# Q: Is it guaranteed that it is possible to go from the first word to the last word?
# A: No, in that case return an empty array or empty string.
# Q: Do the intermediate words have to be English words?
# A: Whatever words are specified in the "valid words" array are the only words allowed.
