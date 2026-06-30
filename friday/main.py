import speech_recognition as sr
import pyttsx3

speakEngine = pyttsx3.init()


def speak(text):
    speakEngine.say(text)
    speakEngine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Friday ..")
    r = sr.Recognizer()
    while True:

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            print(word)
            if "friday" in word.lower():
              print("Wake word detected")

              speak("Yes boss")

              import time
              time.sleep(2)

              print("After Speak")





        except sr.WaitTimeoutError:
            print("Listening timed out.")

        except sr.UnknownValueError:
            print("Could not understand audio.")

        except sr.RequestError as e:
            print(f"Request Error: {e}")