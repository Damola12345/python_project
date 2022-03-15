# python program
# word replacement program


# user input a sentence 
sentence = input('Enter your sentence: ')
print('your sentence is: '+sentence)

# user input to replace the sentence
word1 = input('Enter the word to replace: ')

# user input  sentence to replace it with another sentence 
word2 = input('Enter the word to replace it with: ')
print(sentence.replace(word1, word2))