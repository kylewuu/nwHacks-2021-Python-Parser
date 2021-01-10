from input import inputFunction


inputText1="At dinner, six shrimp were eaten by Harry. The savannah is roamed by beautiful giraffes. A movie is going to be watched by us tonight. The obstacle course was run by me in record time."
inputText = "It is believed by the candidate that a ceiling must be placed on the budget by Congress. The man was bitten by the dog. The letter was mailed by Wilson. The savannah is roamed by beautiful giraffes."
outputText = inputFunction(inputText)

sentence = ''
for element in range(0,len(outputText)):
    sentence = sentence + outputText[element]
    if outputText[element]=='.':
        print(sentence)      
        #TODO: Call parsing function ...
        sentence = ''   #Clear sentence
        
    




