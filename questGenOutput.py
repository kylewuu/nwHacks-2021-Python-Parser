from pprint import pprint
from questGen.question import QGen


def questGenFunction(inputText):
    qg=QGen()
    payload = {
                "input_text":inputText
            }
    print(payload)
    output = qg.predict_mcq(payload)


            