# Ask the user to type a sentence
sentence = input("Type a sentence: ")
# Split the sentence into words
words = sentence.split()
# Create an empty dictionary to store word counts
counts = {}
# Count how many times each word appears If the word is already in the dictionary, add 1 to its count.If it’s not in the dictionary yet, add it for the first time with a count of 1.
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
# Show each word and how many times it appears
for word in counts:
    print(word, ":", counts[word])