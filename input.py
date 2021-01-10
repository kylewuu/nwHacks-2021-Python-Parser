#!/usr/bin/env python
import sys
import spacy
import pattern.text.en
from pass2act import pass2act

def inputFunction(inputText):

    nlp = spacy.load('en')
    prev = ''
    acts = ''

    s=inputText.strip()

    prev = s
    acts = pass2act(s)
    
    return acts
