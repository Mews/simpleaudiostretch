import soundfile
from numpy import ndarray

def stretch_audio(audio, factor, samplerate=None, output=None):
    #If a file path is provided, load it as a ndarray using soundfile
    if isinstance(audio, str):
        audio, samplerate = soundfile.read("song.mp3")

    elif not isinstance(audio, ndarray):
        pass

    if isinstance(output, str):
        soundfile.write("out.wav", audio, samplerate=round(samplerate/(1/factor)))

sound, samplerate = soundfile.read("out.wav")
print(isinstance(sound, ndarray))