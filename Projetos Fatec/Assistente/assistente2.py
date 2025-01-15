import pyttsx3
import speech_recognition as sr
from playsound import playsound
import random
import datetime
import webbrowser as wb
import os

# Carrega os módulos de comandos e respostas
from modules import comandos_respostas
comandos = comandos_respostas.comandos
respostas = comandos_respostas.respostas

meu_nome = 'Maria'

# Função para síntese de fala
def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)  # Número de palavras por minuto
    engine.setProperty('volume', 1)  # Volume máximo
    engine.say(audio)
    engine.runAndWait()

speak('Testando o sintetizador de voz da assistente')

# Função para captar áudio do microfone
def listen_microphone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source, duration=0.8)
        print('Ouvindo:')
        audio = microfone.listen(source)
        # Salva o áudio capturado em um arquivo WAV
        with open('recordings/speech.wav', 'wb') as f:
            f.write(audio.get_wav_data())
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print('Você disse: ' + frase)
    except sr.UnknownValueError:
        frase = ''
        print('Não entendi')
    return frase

print('[INFO] Pronto para começar!')

# Tocar o som inicial, se o arquivo existir
if os.path.exists('n1.mp3'):
    playsound('n1.mp3')

# Loop principal da assistente
while True:
    result = listen_microphone()

    if meu_nome in result:
        result = result.lower().replace(meu_nome + ' ', '')
        print('Acionou a assistente!')
        print('Após o processamento:', result)

        # Comando para listar funções
        if result in comandos[0]:
            if os.path.exists('n2.mp3'):
                playsound('n2.mp3')
            speak('Até agora minhas funções são: ' + respostas[0])

        # Comando para informar as horas
        elif result in comandos[1]:
            if os.path.exists('n2.mp3'):
                playsound('n2.mp3')
            speak('Agora são ' + datetime.datetime.now().strftime('%H:%M'))

        # Comando para informar a data
        elif result in comandos[2]:
            if os.path.exists('n2.mp3'):
                playsound('n2.mp3')
            speak('Hoje é dia ' + datetime.date.today().strftime('%d de %B de %Y'))

        # Comando para encerrar a assistente
        elif result == 'encerrar':
            if os.path.exists('n2.mp3'):
                playsound('n2.mp3')
            speak(random.choice(respostas[4]))
            break
    else:
        if os.path.exists('n3.mp3'):
            playsound('n3.mp3')

# Configuração do caminho do Google Chrome no Windows
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

# Função para realizar uma pesquisa no Google
def search(frase):
    wb.get(chrome_path).open('https://www.google.com/search?q=' + frase)

# Exemplo de uso da função de pesquisa
search('linguagem natural')
