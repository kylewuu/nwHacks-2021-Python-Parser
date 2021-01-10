import io
import os

from google.cloud import vision


def extractText(filePath):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\englishDesktop\Coding\\nwHacks2021\keys\\nwHacks-ee0c4c9fc376.json"

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath(filePath)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    # print('Texts:')
    finalText = ""

    for i in range(len(texts)):
        # print(text.description)
        finalText += texts[i].description

    sentencesArray = finalText.splitlines()
    sentencesArray = sentencesArray[:-1]
    # print(sentencesArray)
    ret = ""

    for i in range(len(sentencesArray)):
        # print(sentencesArray[i], end=" ")
        ret += sentencesArray[i] + " "

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return ret
