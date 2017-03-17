# I was taking a ride on my bike
# I was riding my bike

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

for w in example_words:
    print(ps.stem(w))

newtext="I was taking a ride on my bike as I was riding my bike"

words= word_tokenize(newtext)

for w in words:
    print(ps.stem(w))
    
