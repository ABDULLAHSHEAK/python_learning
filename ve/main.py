import speech_recognition as sr
import pyttsx3

speakEngine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    speakEngine.say(text)
    speakEngine.runAndWait()

if __name__ == "__main__":
    speak("Hello World")

    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio = r.listen(source, timeout=2)

            print("Recognizing...")
            command = r.recognize_google(audio)
            print("You said:", command)

            if command.lower() == "exit":
                speak("Goodbye")
                break

        except sr.WaitTimeoutError:
            print("Listening timed out.")

        except sr.UnknownValueError:
            print("Could not understand audio.")

        except sr.RequestError as e:
            print(f"Request Error: {e}")