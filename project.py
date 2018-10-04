# Using Google text-to-speech(gtts)
from gtts import gTTS
import os

n=int(input('1. Enter text\n2.Select a text file to convert to audio \n'))

if (n==1):
        myobj = gTTS(text=input("Enter Text for Text to Speech : "),
                        lang='en', slow=False)

else:
        data = open(input("Enter the name of the file :"),'rt' )
        text1 = data.read()
        print (text1)
        myobj = gTTS(text=text1,lang='en',slow=False)

# saving the speech as a mp3 file.
myobj.save("name.mp3")
os.system("mgp321 name.mp3")
