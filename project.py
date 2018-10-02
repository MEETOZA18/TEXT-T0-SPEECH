# Using Google text-to-speech(gtts)
from gtts import gTTS
import os

# en=english language
language = 'en'
myobj = gTTS(text=input("Enter Text : "), lang=language, slow=False)

# saving the speech as a mp3 file.
myobj.save("name.mp3")

os.system("mgp321 name.mp3")
