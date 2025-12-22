#program to sort words in a sentence alphabetically using list
my_sentence = "python is very, fun to learn"
words = my_sentence.split()
words.sort()
print("Sorted List:", words)
sorted_sentence = " ".join(words)
print("Sorted Sentence:", sorted_sentence)
