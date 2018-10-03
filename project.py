# Using Google text-to-speech(gtts)
from gtts import gTTS
import os

# en=english language
myobj = gTTS(text=input("Enter Text for Text to Speech : "),
             lang='en')

# saving the speech as a mp3 file.
myobj.save("name.mp3")

os.system("mgp321 name.mp3")
