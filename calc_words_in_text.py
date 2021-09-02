strings = str(input("Please enter your text "))
num_words = 0
for current_string in strings:
    for current_character in current_string:
        if current_character == " ":
            num_words += 1
nums_words = num_words
print("")
print("**********************************************")
print("There are", nums_words, "words in these text.")

