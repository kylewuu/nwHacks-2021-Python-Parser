# Import libraries

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize



# Text which will be inputted by the user and summarized
input_text = """" """"


# Text becomes tokenized
stopWords = set(stopwords.words("english"))
words = word_tokenize(input_text)

# Create a hash map to count the number of times
# a word appears
freqTable = dict()

for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

# Hash map to keep the score
# of each sentence

sentences = sent_tokenize(input_text)
sentenceValue = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

# Calculate a sentence's average value from the text
average = int(sumValues / len(sentenceValue))

# Create summary
summary =''
for sentence in sentences:
    if (sentence in sentenceValue) and sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence
print(summary)