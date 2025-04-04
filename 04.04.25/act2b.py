
def word_count_and_frequency(sentence):
   
    words = sentence.split()

    total_word_count = len(words)

    word_frequency = {}
    for word in words:
        word = word.lower()  
        word_frequency[word] = word_frequency.get(word, 0) + 1
    
    return total_word_count, word_frequency

sentence = input("Enter a sentence: ")
word_count, frequency = word_count_and_frequency(sentence)
print("Word Count:", word_count)
print("Word Frequencies:", frequency)
