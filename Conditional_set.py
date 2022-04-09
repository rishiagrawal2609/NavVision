from Voice_driver import recognize_speech
import speech_recognition as sr
import spacy
from gtts import gTTS
import os
english = spacy.load("en_core_web_sm")
t = True
while t == True:
    res = recognize_speech(recognizer=sr.Recognizer(), microphone=sr.Microphone())
    # we will try to add all the features of the navvision into if else statement.
    # before that lets use NLP to break the sentence in list.
    ws = res['transcription']
    #print(ws)
    doc = english(ws)
    doc_list = []
    for token in doc:
        doc_list.append(token.text)
    # print(doc_list)
    # doc_list will tokenize the spoken sentence into list.
    # now we can use if-elif-else statement to proceed further


    





