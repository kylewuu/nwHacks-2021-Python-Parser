#Main Function

from input import inputFunction
from summarizer import summarizerFunction
from questGenOutput import questGenFunction

inputText = ""
summarizedText= ""
sentence = ''
outputText= ""

#inputText="At dinner, six shrimp were eaten by Harry. The savannah is roamed by beautiful giraffes. A movie is going to be watched by us tonight. The obstacle course was run by me in record time. It is believed by the candidate that a ceiling must be placed on the budget by Congress. The man was bitten by the dog. The letter was mailed by Wilson."




inputText = """Master is an upcoming 2021 Indian Tamil-language action-thriller film co-written and directed by Lokesh Kanagaraj, and produced by Xavier Britto. The film stars Vijay and Vijay Sethupathi, with Malavika Mohanan, Arjun Das, Andrea Jeremiah and Shanthanu Bhagyaraj in supporting roles. The music is composed by Anirudh Ravichander, while cinematography and editing are performed by Sathyan Sooryan and Philomin Raj. Principal photography began in October 2019 and was completed in February 2020. Master was initially planned for theatrical release on 9 April 2020, but was postponed due to the COVID-19 pandemic in India. The makers of the film preferred to wait for a theatrical release, despite the digital streaming rights being sold to Prime Video. By the end of 2020, the film was confirmed for release on 13 January 2021 in theatres, during the week of Pongal."""

#Call summarizerFunction from summarizer.py to summarize the inputText
summarizedText = summarizerFunction(inputText)

#Call inputFunction from input.py > pass2act.py to convert passive sentence into active sentences.
outputText = inputFunction(inputText)   
print(outputText)

parsedOutput = questGenFunction(outputText)
print(parsedOutput)







