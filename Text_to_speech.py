from gtts import gTTS
from playsound import playsound

def speak(text):
    mytext = text
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("note.mp3")
playsound("note.mp3")