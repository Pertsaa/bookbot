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

def print_report(text):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(text)} words found in the document\n")

    counts = letter_counts(text)
    counts_list = []
    for c in counts:
        if c.isalpha():
            counts_list.append((c, counts[c]))
    counts_list.sort(key=lambda t: t[1], reverse=True)

    for e in counts_list:
        print(f"The '{e[0]}' character was found {e[1]} times")

    print(f"--- End report ---")

with open("books/frankenstein.txt") as f:
    file_content = f.read()
    print_report(file_content)
