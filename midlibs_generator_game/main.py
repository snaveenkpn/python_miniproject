# we are storing the content from the story.txt
with open("story.txt", "r") as f:
    my_story=f.read()

    
target_starting = "<"
target_ending = ">"

starting_word = -1

words = set()

# we are collecting the words that is present within <> in a list by using startingword and ending word
for i, char in enumerate(my_story):

    if char == target_starting:
        starting_word=i
    
    if char==target_ending and starting_word != -1:
        word= my_story[starting_word: i+1]

        words.add(word)

answers = {}

# we are getting user input and replace the words

for word in words:
    answer= input("Enter the word to be replace for "+ word + ": ")

    answers[word]=answer

for word in words:
    my_story=my_story.replace(word, answers[word])

print(my_story)

