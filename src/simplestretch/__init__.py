import soundfile
from numpy import ndarray
from typing import Optional, Union, Tuple

def stretch_audio(audio:Union[str, ndarray], factor:float, output:Optional[str] = None, samplerate:Optional[int] = None) -> Tuple[ndarray, int]:


    #Type checks
    if not (isinstance(audio, str) or isinstance(audio, ndarray)):
        raise TypeError("\'audio\' must be the path to a audio file or a numpy ndarray")

    if factor <= 0:
        raise ValueError("\'factor\' must be greater than 0")


    #If a file path is provided, load it as a ndarray using soundfile
    if isinstance(audio, str):
        audio, samplerate = soundfile.read("song.mp3")
    
    stretched_samplerate = round(samplerate/factor)

    if isinstance(output, str):
        try:
            soundfile.write(output, audio, samplerate=stretched_samplerate)
        except soundfile.LibsndfileError as exc:
            exc.add_note("(Try saving it as a .wav file instead)")
            raise exc

    return (audio, stretched_samplerate)