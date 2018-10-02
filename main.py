from text_to_speech import TextToSpeech

obj = TextToSpeech()
obj.text_input()
obj.create_gtts_object()
obj.speech_save()
obj.run()
