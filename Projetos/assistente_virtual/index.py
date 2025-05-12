import speech_recognition as sr
import re
import pyttsx3
import webbrowser

nome = ""

while (True):

    mic = sr.Recognizer()

    with sr.Microphone() as source:
        engine = pyttsx3.init()
        engine.setProperty('voice', "com.apple.speech.synthesis.voice.luciana")
        mic.adjust_for_ambient_noise(source)

        print("Fale alguma coisa:")

        audio = mic.listen(source)

        try:
            frase = mic.recognize_google(audio, language="pt-BR")

            if (re.search(r'\b' + "ajudar" + r'\b', format(frase))):
                engine.say("Claro, estou aqui para ajudar!")
                engine.runAndWait()
                print("Algo relacionado a ajudar foi dito.")

            elif (re.search(r'\b' + "meu nome é" + r'\b', format(frase))):
                t = re.search('meu nome é (.*)', format(frase))
                nome = t.group(1)
                engine.say("Olá " + nome + ", prazer em conhecê-lo!")
                engine.runAndWait()
                print("Seu nome é: " + nome)

            elif (re.search("Abrir navegador", format(frase))):
                engine.say("Abrindo o navegador!")
                engine.runAndWait()
                print("Abrindo o navegador!")
                webbrowser.open("https://www.google.com")

            elif (re.search(r'\b' + "sair" + r'\b', format(frase))):
                engine.say("Até mais!")
                engine.runAndWait()
                print("Saindo do programa.")
                break

            print("Você disse: " + frase)

        except sr.UnknownValueError:
            print("Não consegui entender o que você disse.")
