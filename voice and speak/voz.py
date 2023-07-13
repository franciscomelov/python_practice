import speech_recognition as sr
import pyttsx3
import pyaudio 
# import serial

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 120)
engine.setProperty('voice', 'spanish')
engine.setProperty('gender', 'male')
# hw_sensor = serial.Serial(port='COM3', baudrate=9600)


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print('Escuchando...')
        r.pause_threshold = 1
        audio = listener.listen(source)
        command = listener.recognize_google(audio, language="es-ES")
        print(command)

    try:
        print("Recognizing...")
        query = command
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


while True:

    # engine.setProperty("voice", voices[2].id)

    # speak('Hola ')

    # engine.runAndWait()

    # speak("hola")

    # speak("como estás")

    # hw_sensor.write('A'.encode('utf-8'))

    speak('habla: ')


    respuesta = takeCommand().lower()
    # respuesta = input("Enter a number: ")
    # hw_sensor.write('a'.encode('utf-8'))
    print(respuesta)

    if 'cómo te' in respuesta:
        speak("Cleo")
    elif 'dónde estamos' in respuesta:
        speak("isima ")
    elif 'dónde vivimos' in respuesta:
        speak("En tu casa ")
    elif 'dónde comemos' in respuesta:
        speak("En tu plato ")
    elif 'salir' in respuesta:
        speak("Adios")
        exit()
