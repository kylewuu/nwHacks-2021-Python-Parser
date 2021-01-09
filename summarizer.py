# Import libraries

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize



# Text which will be inputted by the user to be summarized
input_text = """ Master is an upcoming 2021 Indian Tamil-language action-thriller film co-written and directed by Lokesh Kanagaraj, and produced by Xavier Britto. The film stars Vijay and Vijay Sethupathi, with Malavika Mohanan, Arjun Das, Andrea Jeremiah and Shanthanu Bhagyaraj in supporting roles. The music is composed by Anirudh Ravichander, while cinematography and editing are performed by Sathyan Sooryan and Philomin Raj. Principal photography began in October 2019 and was completed in February 2020.

Master was initially planned for theatrical release on 9 April 2020, but was postponed due to the COVID-19 pandemic in India. The makers of the film preferred to wait for a theatrical release, despite the digital streaming rights being sold to Prime Video. By the end of 2020, the film was confirmed for release on 13 January 2021 in theatres, during the week of Pongal. """


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
    if (sentence in sentenceValue) and sentenceValue[sentence] > (1.2 * average):
        summary += " " + sentence
print(summary)