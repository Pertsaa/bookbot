def word_count(text):
    return len(text.split())

with open("books/frankenstein.txt") as f:
    file_content = f.read()
    print(file_content)
    print(f"words: {word_count(file_content)}")
