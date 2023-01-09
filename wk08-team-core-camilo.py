input_letter = input("What's you favorite letter? ")
word_review = input("What's the word to review? ")
new_word = ""

#CORE REQ 1, 2 & 3
for letter in word_review:
    if letter.lower() == input_letter.lower():
        new_word = new_word + "_"
    else:
        new_word = new_word + letter.lower()

print(new_word)