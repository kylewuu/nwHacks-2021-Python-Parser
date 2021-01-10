from textDetection import *
from classes.Question import Question


def main():

    # extract text from uploaded image
    extractedText = extractText(
        'res/science_textbook_image_cropped_edited.jpg')
    print(extractedText)

    # summarize text
    # summarizedText = FUNCTION OF SUMMARIZE TEXT, MAKE IT RETURN ONE LONG STRING (paragraph form)

    # make into passive text
    # activeVoiceText = FUNCTION OF CONVERTING TO ACTIVE VOICE, should return another long string (paragraph form)

    # make array of questions
    # questions

    # def __init__(self, question_type, question, correct_answer, all_answers=[]):
    # example of how to set an object
    questions = output["questions"]
    questionsReturn = []
    questions[0] = {'question_statement': 'Who is the main actor in the film?', 'question_type': 'MCQ', 'answer': 'vijay', 'id': 1, 'options': ['Kohli', 'Dhoni', 'Milne'], 'options_algorithm': 'sense2vec', 'extra_options': ['Steyn', 'Sanga', 'Mccullum', 'Haddin'],
                    'context': 'The film stars Vijay and Vijay Sethupathi, with Malavika Mohanan, Arjun Das, Andrea Jeremiah and Shanthanu Bhagyaraj in supporting roles. The film stars Vijay and Vijay Sethupathi, with Malavika Mohanan, Arjun Das, Andrea Jeremiah and Shanthanu Bhagyaraj in supporting roles.'}

    for i in range(len(questions)):
        questionsReturn[i] = Question(questions[i]["questions_type"], questions[i]["questions_statement"], questions[i]["answer"], (
            questions[i]["questions_type"] == "MCQ" if questions[i]["options"].append(questions[i]["answer"]) else []))


if __name__ == "__main__":
    main()
