from typing import Optional, Tuple, Union

import soundfile
from numpy import ndarray



def stretch_audio(
    audio: Union[str, ndarray],
    factor: float,
    output: Optional[str] = None,
    samplerate: Optional[int] = None,
) -> Tuple[ndarray, int]:
    """This function is used to stretch an audio's length by a certain factor.\n
    Because this function doesn't apply any resampling or similar algorithms, for very high factors (around 5 or higher) the audio quality might decrease noticeably.

    :param audio: The audio to be stretched.\n
                  You can provide either a path to a file containing your audio, or the raw sound data as a numpy ndarray.
    :type audio: str | numpy.ndarray

    :param factor: This is the factor by which the length of the audio will be changed.\n
        For example, a factor of 2 will make the audio twice as long, and a factor of 0.5 will make the audio half as long.
    :type factor: float

    :param output: This is the path to which the stretched audio will be saved.\n
        If no argument is passed, it wont save the audio to a file.
    :type output: str, optional

    :param samplerate: The sample rate of the original audio.\n
        You only need to pass this argument if you've provided a numpy ndarray as the audio. Otherwise, it will be determined automatically.
    :type samplerate: int, optional

    :return: A tuple containing the stretched audio data and sample rate.\n
        This is returned whether or not the audio gets saved to a file.
    :rtype: Tuple[ndarray, int]

    """

    # Type checks
    if not (isinstance(audio, str) or isinstance(audio, ndarray)):
        raise TypeError("'audio' must be the path to a audio file or a numpy ndarray")

    if factor <= 0:
        raise ValueError("'factor' must be greater than 0")
    
    if isinstance(audio, ndarray) and not isinstance(samplerate, int):
        raise TypeError(f"You must provide a valid sample rate when working with raw audio data (Not {type(samplerate)})")
        

    # If a file path is provided, load it as a ndarray using soundfile
    if isinstance(audio, str):
        audio, samplerate = soundfile.read(audio)

    stretched_samplerate = round(samplerate / factor)

    if isinstance(output, str):
        try:
            soundfile.write(output, audio, samplerate=stretched_samplerate)
        except soundfile.LibsndfileError as exc:
            exc.add_note("(Try saving it as a .wav file instead)")
            raise exc

    return (audio, stretched_samplerate)


def speedup_audio(
    audio: Union[str, ndarray],
    factor: float,
    output: Optional[str] = None,
    samplerate: Optional[int] = None,
) -> Tuple[ndarray, int]:
    """This function is used to change an audio's speed by a certain factor.\n
    Because this function doesn't apply any resampling or similar algorithms, for very low factors (around 0.2 or lower) the audio quality might decrease noticeably.

    :param audio: The audio to be sped up or down.\n
                  You can provide either a path to a file containing your audio, or the raw sound data as a numpy ndarray.
    :type audio: str | numpy.ndarray

    :param factor: This is the factor by which the speed of the audio will be changed.\n
        For example, a factor of 2 will make the audio twice as fast, and a factor of 0.5 will make the audio half as fast.
    :type factor: float

    :param output: This is the path to which the sped up audio will be saved.\n
        If no argument is passed, it wont save the audio to a file.
    :type output: str, optional

    :param samplerate: The sample rate of the original audio.\n
        You only need to pass this argument if you've provided a numpy ndarray as the audio. Otherwise, it will be determined automatically.
    :type samplerate: int, optional

    :return: A tuple containing the sped up audio data and sample rate.\n
        This is returned whether or not the audio gets saved to a file.
    :rtype: Tuple[ndarray, int]

    """

    # Type checks
    if factor <= 0:
        raise ValueError("'factor' must be greater than 0")

    # Stretch audio to match the specified speedup factor
    return stretch_audio(
        audio=audio, factor=1 / factor, output=output, samplerate=samplerate
    )