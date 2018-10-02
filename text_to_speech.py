from gtts import gTTS
import os
import sys


class TextToSpeech:

    def __init__(self):
        pass

    def text_input(self):
        self.text = input("Enter Text : ")
        print("Text Entered")

    def create_gtts_object(self):
        self.gtts_object = gTTS(text=self.text, lang='en')
        print("Object Made")

    def speech_save(self):
        os.system("rm speech.mp3")  # deleting file, not overriding
        self.gtts_object.save('speech.mp3')
        print("File Saved")

    def run(self):
        os.system("mpg123 speech.mp3")
