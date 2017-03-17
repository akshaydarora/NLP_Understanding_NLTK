from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

exampleSent="This is an ex showing off stop word filtration"
stopWords=set(stopwords.words("english"))

#print(stopWords)
words=word_tokenize(exampleSent)

filtered_sentence = []

for w in words:
    if w not in stopWords:
        filtered_sentence.append(w)

print(filtered_sentence)

