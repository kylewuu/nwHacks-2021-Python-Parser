import spacy
import pattern.text.en as en
from wordinv import nouninv

def myFunction():

    try:
        verb=en.conjugate('go',tense='PAST')
    except StopIteration:
        return
    return verb


myFunction()
print(verb)