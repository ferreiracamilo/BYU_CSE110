def add_spaces(secretWord):
    secret_with_space = ""
    for i in range(len(secretWord)):
        if i<len(secretWord)-1:
            secret_with_space = secret_with_space + secretWord[i]+" "
        else:
            secret_with_space = secret_with_space + secretWord[i]
    return secret_with_space

def remove_letters(secretWord):
    secret_without_letters = ""
    for oneChar in secretWord:
        if oneChar.isalpha(): #This will review if the "char" is an actual letter to save it as underscore
            secret_without_letters = secret_without_letters + "_"
        else:
            secret_without_letters = secret_without_letters + oneChar
    return secret_without_letters

def replace_letter_by_index(wordUpdate,newLetter,indexLetter):
    newWord = ""
    for i in range(len(wordUpdate)):
        if i!=indexLetter:
            newWord = newWord + wordUpdate[i]
        else:
            newWord = newWord + newLetter
    return newWord

def compare_words(secretWord,guessWord):
    #Will work only if they are the same length
    fSecret = secretWord.lower()
    fGuess = guessWord.lower()
    for i in range(len(secretWord)):
        if fSecret[i] == fGuess[i]:
            fGuess = replace_letter_by_index(fGuess,fGuess[i].upper(),i)
        elif fSecret.find(fGuess[i]) == -1:
            #find would give -1 in case letter is not found
            fGuess = replace_letter_by_index(fGuess,"_",i)
    return fGuess

secret_word = "mosiah"
guess_word = ""
temporal_hint = ""
qty_attempts = 1

print("Welcome to the word guessing game!")
temporal_hint = remove_letters(secret_word)
temporal_hint = add_spaces(temporal_hint)
print(f"Your hint is: {temporal_hint}")
guess_word = input("What is your guess? ")

while guess_word.lower() != secret_word.lower():
    qty_attempts = qty_attempts + 1
    if guess_word.upper() == "STOP":
        exit()
    elif len(guess_word) != len(secret_word):
        print(f"Sorry, tue guess must have the same number of letters as the secret word ({len(secret_word)})")
        print("If you want to stop playing, type STOP")
        guess_word = input("What is your guess? ")
    else:
        print("If you want to stop playing, type STOP")
        temporal_hint = compare_words(secret_word,guess_word)
        temporal_hint = add_spaces(temporal_hint)
        print(f"Your hint is: {temporal_hint}")
        guess_word = input("What is your guess? ")

print(f"\nCongratulations! You guessed it!, word was {secret_word}")
print(f"It took you {qty_attempts} guess/es")