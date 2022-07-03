import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print ("Rate: ", rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print ("Volumen: ", volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. 0 for female spanish
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for male english
#Spanish
engine.say("Hola Mundo, escuchas un audio desde un archivo Python!")
#English
engine.setProperty('voice', voices[2].id)
engine.say("Hello World, you hear an audio from a Python file!")
#German
#engine.setProperty('voice', voices[3].id)
engine.say("Hallo Welt, Sie hören ein Audio aus einer Python-Datei!")
#French
#engine.setProperty('voice', voices[4].id)
engine.say("Bonjour tout le monde, vous entendez l'audio d'un fichier Python !")
#Italian
#engine.setProperty('voice', voices[5].id)
engine.say("Ciao mondo, senti un audio da un file Python!")

engine.setProperty('voice', voices[1].id)    #changing index, changes voices. 2 for female english
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

"""Saving Voice to a file
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait() """