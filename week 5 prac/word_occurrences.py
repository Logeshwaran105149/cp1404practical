String = input("Enter a text:")

# Split the string into words
words = String.split()

# Create an empty dictionary to store the word counts
word_counts = {}

# Count the occurrences of each word
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word, count in word_counts.items():
    print(f"{word}:{count}")
