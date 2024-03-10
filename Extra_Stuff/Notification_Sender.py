import pyttsx3
import time
from winotify import Notification, audio

engine = pyttsx3.init()
engine.say("Do you wish to send the test notification? Y/N")
engine.runAndWait()
user_input = input("Y/N? ")
user_input = user_input.lower()

if user_input == "y":
    toast = Notification(app_id="Reminder!",
                    title="This is a test!",
                    msg="A notification used a test. ",
                    duration="short",
                    icon=r"C:/Users/Asif\Documents\Alarm-PNG-HD-Image.png")

    toast.set_audio(audio.LoopingAlarm, loop=True)
    toast.show()

    engine.runAndWait()

elif user_input == "n":
    quit()