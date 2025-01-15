import pygame
from gtts import gTTS

def tocar_audio(caminho_audio):
    pygame.mixer.init()
    pygame.mixer.music.load(caminho_audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def criar_audio(texto):
    tts = gTTS(texto, lang='pt-br')
    tts.save('bem_vindo.mp3')
    tocar_audio('bem_vindo.mp3')

# Tocar um áudio existente no diretório
tocar_audio('C:\\Users\\negri\\Desktop\\PYTHON\\n1.mp3')

# Gerar e tocar um novo áudio
criar_audio('Oi, sou kenny.')

# Teste de outras bibliotecas instaladas
try:
    import speech_recognition
    print('Speech Recognition: ', speech_recognition.__version__)
except ImportError:
    print('speech_recognition não está instalado.')

try:
    import pyttsx3
    pyttsx3.speak('Testando a biblioteca')
except ImportError:
    print('pyttsx3 não está instalado.')

try:
    import tensorflow
    print('TensorFlow:', tensorflow.__version__)
except ImportError:
    print('TensorFlow não está instalado.')

try:
    import librosa
    print('Librosa:', librosa.__version__)
except ImportError:
    print('Librosa não está instalado.')

try:
    import matplotlib
    print('Matplotlib: ', matplotlib.__version__)
except ImportError:
    print('Matplotlib não está instalado.')

try:
    import seaborn
    print('Seaborn: ', seaborn.__version__)
except ImportError:
    print('Seaborn não está instalado.')

try:
    import pyaudio
    print('Pyaudio ok!')
except ImportError:
    print('Pyaudio não está instalado.')
