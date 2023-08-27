def word_count(text):
    return len(text.split())

def letter_counts(text):
    letter_counts = {}
    for c in text:
        if c.lower() in letter_counts:
            letter_counts[c.lower()] += 1
        else:
            letter_counts[c.lower()] = 0
    return letter_counts

with open("books/frankenstein.txt") as f:
    file_content = f.read()
    print(file_content)
    print(f"words: {word_count(file_content)}")
    print(letter_counts(file_content))
