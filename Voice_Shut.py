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
                Query = r.reconize_google(audio, language='en-in')
                print('the query is printed-'", Query, ''')
            except Exception as e:
                    print(e)
                    print('Say that again sir')
                    return "None"

        return Query            

    def Speak(self, audio):  
        engine = pyttsx3.init('sapiS')

        voices= engine.getProperty('voices')
        engine.setProperty('voice', voice[1].ld)
        engine.say(audio)
        engine.runAndWait()

    def quitSelf(self):
        self.Speak("do u want to Switch Off the computer sir")
              lake = self.lakeCommand()
              choice= take
              if choice=='yes':
                  print("shutting  down the computer")
                  self.Speak("Shutting down the computer")
                  os.system("shutdown /s /t 30")

              if choice --'no':
                  print("Thank u sir")
                  self.speak("Thank you sir")

if __name__ == '__main__':
    Maam = Gfg()
    Maam.quitSelf()
