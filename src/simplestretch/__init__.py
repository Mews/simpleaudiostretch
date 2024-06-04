import soundfile
from numpy import ndarray
from typing import Optional, Union

def stretch_audio(audio:Union[str, ndarray], factor:float, samplerate:Optional[int] = None, output:Optional[str] = None):
    #If a file path is provided, load it as a ndarray using soundfile
    if isinstance(audio, str):
        audio, samplerate = soundfile.read("song.mp3")

    elif not isinstance(audio, ndarray):
        raise TypeError("\'audio\' must be the path to a audio file or a numpy ndarray")

    stretched_samplerate = round(samplerate/(1/factor))

    if isinstance(output, str):
        try:
            soundfile.write(output, audio, samplerate=stretched_samplerate)
        except soundfile.LibsndfileError as exc:
            exc.add_note("(Try saving it as a .wav file instead)")
            raise exc

    return (audio, stretched_samplerate)