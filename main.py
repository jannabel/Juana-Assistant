from deep_translator import GoogleTranslator
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('escuchando...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='es-ES')
            command = command.lower()
            if 'juana' in command:
                command = command.replace('juana', '')
                print(command)
    except:
        pass
    return command


def run_juana():
    engine.setProperty('voice', voices[0].id)
    command = take_command()
    print('Tu: ' + command)
    if 'reproduce' in command:
        song = command.replace('reproduce', '')
        talk('reproduciendo ' + song)
        pywhatkit.playonyt(song)

    elif ('hola' or 'saludos' or 'hola juana') in command:
          talk('Hola humano, ¿en qué puedo ayudarte?')
    elif 'hora' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('la hora actual es ' + time)
    elif 'busca' in command:
        person = command.replace('busca', '')
        wikipedia.set_lang("es")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'cita' in command:
        talk('Lo siento, me duele la cabeza')
    elif ('estás soltera' or 'sal conmigo') in command:
        talk('Estoy en una relación con el WiFi')
    elif 'chiste'  in command:
        joke = pyjokes.get_joke('es')
        print(joke)
        talk(joke)
    elif 'correo'  in command:
        talk("Escriba el correo del destinatario")
        print("-- ")
        dest = input()
        talk("Diga el Asunto del correo")
        subject = take_command()
        talk("Diga el mensaje del correo")
        message = take_command()
        talk("El Destinatario es {0}, El asunto es {1}, El mensaje es {2}" .format(dest, subject, message))
        print("El Destinatario es {0}, El asunto es {1}, El mensaje es {2}".format(dest, subject, message))
        pywhatkit.send_mail('yourmail@gmail.com', 'password', subject, message, dest)
        talk("Mensaje enviado")
    elif 'traduce' in command:
        words = command.replace('traduce', '')
        tr = GoogleTranslator(source='es', target='en')
        result = tr.translate(words)
        print(result)
        engine.setProperty('voice', voices[1].id)
        talk(result)
    else:
        talk('Por favor, Repita la instrucción')


while True:
    run_juana()