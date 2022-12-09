"""
Word Occurrences
Estimate: 20 minutes
Actual:   20 minutes
"""
total_text = {}

user_sentence = input("Text: ")

for i in user_sentence.split():
    if i in total_text:
        total_text[i] += 1
    else:
        total_text[i] = 1

for q in sorted(total_text):
    print(f"{q:10}: {total_text[q]}")




