import pyttsx3


# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    # save to file
    # engine.save_to_file(command, 'test.mp3')
    engine.runAndWait()


en_1 = open("test sample/en-1.txt", "r").read()
# SpeakText(en_1)

en_2 = open("test sample/en-2.txt", "r").read()
# SpeakText(en_2)

en_3 = open("test sample/en-3.txt", "r").read()
# SpeakText(en_3)

# can't read arabic text yet
# ar_3 = open("test sample/ar-3.txt", "r").read()
# SpeakText(ar_3)

# Changing voices
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[0].id)
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

# Changing speech rate
# engine = pyttsx3.init()
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate-50)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

# Changing volume
# engine = pyttsx3.init()
# volume = engine.getProperty('volume')
# engine.setProperty('volume', volume-0.75)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()