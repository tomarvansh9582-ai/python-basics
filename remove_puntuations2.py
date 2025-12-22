import string
text =input()
clean_text = ""
for char in text:
    if char not in string.punctuation:
        clean_text =clean_text+char
print("Original Text:", text)
print("Text after removing punctuations:", clean_text)
