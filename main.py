from textDetection import *
from classes.Question import Question
from input import inputFunction
from summarizer import summarizerFunction
from questGenOutput import questGenFunction


def main():

    # extract text from uploaded image
    extractedText = extractText(
        'res/science_textbook_image_cropped_edited.jpg')
    print(extractedText)


    inputText = ""
    summarizedText= ""
    sentence = ''
    outputText= ""

    inputText = extractedText

    #Call summarizerFunction from summarizer.py to summarize the inputText
    summarizedText = summarizerFunction(inputText)

    #Call inputFunction from input.py > pass2act.py to convert passive sentence into active sentences.
    outputText = inputFunction(inputText)   
    print(outputText)

    parsedOutput = questGenFunction(outputText)
    print(parsedOutput)

    questions = parsedOutput["questions"]
    questionsReturn = []
    questions[0] = {'question_statement': 'Who is the main actor in the film?', 'question_type': 'MCQ', 'answer': 'vijay', 'id': 1, 'options': ['Kohli', 'Dhoni', 'Milne'], 'options_algorithm': 'sense2vec', 'extra_options': ['Steyn', 'Sanga', 'Mccullum', 'Haddin'],
                    'context': 'The film stars Vijay and Vijay Sethupathi, with Malavika Mohanan, Arjun Das, Andrea Jeremiah and Shanthanu Bhagyaraj in supporting roles. The film stars Vijay and Vijay Sethupathi, with Malavika Mohanan, Arjun Das, Andrea Jeremiah and Shanthanu Bhagyaraj in supporting roles.'}

    for i in range(len(questions)):
        questionsReturn[i] = Question(questions[i]["questions_type"], questions[i]["questions_statement"], questions[i]["answer"], (
            questions[i]["questions_type"] == "MCQ" if questions[i]["options"].append(questions[i]["answer"]) else []))


if __name__ == "__main__":
    main()
