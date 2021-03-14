import os
import pyttsx3
import speech_recognition as sr

class Gfg:
    def takecommands(self):
        r = sr.recognizer()
        with sr.Microphone() as source:
            print('listening')

            r.pause_threshold = 0.7
            audio = r.listen(source)

            try:
                print("recognizing")