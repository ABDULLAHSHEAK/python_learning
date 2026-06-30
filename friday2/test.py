import pyttsx3
import time

engine = pyttsx3.init()

engine.say("First")
engine.runAndWait()

time.sleep(2)

engine.say("Second")
engine.runAndWait()