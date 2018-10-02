# importing pandas

import pandas as pd

# with the help of pandas read a text file
data = pd.read_csv("fliename.txt", header=None)

# Just printing the text file
print(data)


# Using Google text-to-speech(gtts)

from gtts import gTTS
import os

# en=english language
language = 'en'
myobj = gTTS(text=data, lang=language, slow=False)

# saving the speech as a mp3 file.
myobj.save("name.mp3")

os.system("mgp321 name.mp3")
