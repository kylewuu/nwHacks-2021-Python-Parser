#Summarizes the large text into a smaller chunck. A sentence is included if 'Scentence Score > (# * average score of sentences)'

import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 



def summarizerFunction(text):  
    #text = """Master is an upcoming 2021 Indian Tamil-language action-thriller film co-written and directed by Lokesh Kanagaraj, and produced by Xavier Britto. The film stars Vijay and Vijay Sethupathi, with Malavika Mohanan, Arjun Das, Andrea Jeremiah and Shanthanu Bhagyaraj in supporting roles. The music is composed by Anirudh Ravichander, while cinematography and editing are performed by Sathyan Sooryan and Philomin Raj. Principal photography began in October 2019 and was completed in February 2020. Master was initially planned for theatrical release on 9 April 2020, but was postponed due to the COVID-19 pandemic in India. The makers of the film preferred to wait for a theatrical release, despite the digital streaming rights being sold to Prime Video. By the end of 2020, the film was confirmed for release on 13 January 2021 in theatres, during the week of Pongal."""
    
    # Tokenizing the text 
    stopWords = set(stopwords.words("english")) 
    words = word_tokenize(text) 
    
    # Creating a frequency table to keep the  
    # score of each word 
    
    freqTable = dict() 
    for word in words: 
        word = word.lower() 
        if word in stopWords: 
            continue
        if word in freqTable: 
            freqTable[word] += 1
        else: 
            freqTable[word] = 1
    
    # Creating a dictionary to keep the score 
    # of each sentence 
    sentences = sent_tokenize(text) 
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
    
    # Average value of a sentence from the original text 
    
    average = int(sumValues / len(sentenceValue)) 
    # Storing sentences into our summary. 
    summary = '' 
    for sentence in sentences: 
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1 * average)): 
            summary += " " + sentence 
    return summary