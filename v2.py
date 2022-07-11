from gtts import gTTS
import playsound

# This module is imported so that we can
# play the converted audio

# The text that you want to convert to audio
language = 'ar'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
en_1 = open("test sample/en-1.txt", "r").read()
# SpeakText(en_1)

en_2 = open("test sample/en-2.txt", "r").read()
# SpeakText(en_2)

en_3 = open("test sample/en-3.txt", "r").read()
# SpeakText(en_3)

ar_1 = open("test sample/ar-1.txt", "r", encoding='utf-8').read()

gtts = gTTS(text=en_1, lang=language, slow=False)
gtts = gTTS(text=en_1, lang="en", tld="ca",  slow=False)
# gtts = gTTS(text=ar_1, lang="ar", tld="ax", slow=False)

# Saving the converted audio in a mp3 file named
# welcome
gtts.save("test.mp3")

# Playing the converted file
playsound.playsound("test.mp3")
