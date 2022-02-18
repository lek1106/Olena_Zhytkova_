text=str(input(' Enter the text: '))
text_words=text.split()
word_counts={word:text_words.count(word) for word in text_words}
print(word_counts)