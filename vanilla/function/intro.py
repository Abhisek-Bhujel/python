def multiply(x: float , y: float) -> float:
    return x * y


def is_palindrome(string: str) -> bool:
    string = string.casefold()
    return string[::-1] == string


def palindrome_sentence (sentence: str) -> bool:
    sentence = sentence.replace(" ", "")
    return is_palindrome(sentence)

sentence = input(("Please enter a sentence to check if it is palindrome: "))

if palindrome_sentence(sentence):
    print("{} is palindrome".format(sentence))
else:
    print("{} is not palindrome".format(sentence))
    
# word = input(("Please enter a word to check if it is palindrome: "))

# if is_palindrome(word):
#     print("{} is palindrome".format(word))
# else:
#     print("{} is not palindrome".format(word))

print(multiply(2,  5))

for i in range (1, 6):
    print(multiply(2 , i))
    
p = palindrome_sentence()