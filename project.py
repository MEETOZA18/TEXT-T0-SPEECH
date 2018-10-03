# Using Google text-to-speech(gtts)
from gtts import gTTS
import os

# en=english language
f=open("demofile.txt","rt")
myobj = gTTS(text=f,lang='language', slow=False)

# saving the speech as a mp3 file.
myobj.save("name.mp3")

os.system("mpg321 name.mp3")
