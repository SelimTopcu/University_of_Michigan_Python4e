#Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.
    
def count_word(word, letter):
    count = 0
    word= str(word)
    letter = str(letter) 

    for i in word:
        if i == letter:
           count = count + 1
    print(count)
count_word ('banana','a')

count_word('Selim', 'i')