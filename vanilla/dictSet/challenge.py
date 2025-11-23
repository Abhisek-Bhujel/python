# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}
 
# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
 
# Your code goes here ...
lower_text=text.lower()
for i in lower_text:
    word_count[i] = word_count.setdefault(i, 0) + 1
 
# Printing the dictionary
for letter, count in reversed(sorted(word_count.items())):
    print(letter, count)
 

    
