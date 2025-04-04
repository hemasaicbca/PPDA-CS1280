def word_count(sen):
    words=sen.split()
    return len(words)
sen=input("Enter a sentence : ")
print(f"The number of words in the sentence is : {word_count(sen)}")