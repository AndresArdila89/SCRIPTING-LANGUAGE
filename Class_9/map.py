"""
    Map in Python

"""
from random import shuffle
def changeWord(word):
    anagram = list(word)
    shuffle(anagram)
    #print(anagram)
    return "" .join(anagram)

words = ["babies", "girls", "boys"]
anagrams = []
#1 -For Loop
for word in words:
    anagrams.append(changeWord(word))

print(words)
print(anagrams)

#2 -List Comprehension
print([changeWord(words) for word in words])


#3 -Map 
result = map(changeWord, words)
print(list(result))
print(list(filter(changeWord,words)))


