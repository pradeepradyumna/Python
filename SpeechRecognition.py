import speech_recognition as sr
import playsound
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    print("playing..." + text)
    playsound.playsound(filename)


r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak something...')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('You said : ' + str(text))
        speak(text)
    except Exception as e:
        print("Sorry, didn't recognize your voice")
        print(e)
