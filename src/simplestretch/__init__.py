import pathlib
from typing import Optional, Tuple, Union

import soundfile
from numpy import ndarray


def stretch_audio(
    audio: Union[str, ndarray],
    factor: float,
    output: Optional[str] = None,
    samplerate: Optional[int] = None,
) -> Tuple[ndarray, int]:
    """This function is used to stretch an audio's length by a certain factor.

    Because this function doesn't apply any resampling or similar algorithms, for very high factors (around 5 or higher) the audio quality might decrease noticeably.

    Args:
        audio (Union[str, ndarray]): The audio to be stretched.
            You can provide either a path to a file containing your audio,
            or the raw sound data as a numpy ndarray.
        factor (float): This is the factor by which the length of the audio will be changed.
            For example, a factor of 2 will make the audio twice as long,
            and a factor of 0.5 will make the audio half as long.
        output (Optional[str], optional): This is the path to which the stretched audio will be saved.
            If no argument is passed, it wont save the audio to a file. Defaults to ``None``.
        samplerate (Optional[int], optional): The sample rate of the original audio.
            You only need to pass this argument if you’ve provided a numpy ndarray as the audio.
            Otherwise, it will be determined automatically. Defaults to ``None``.

    Raises:
        TypeError: When audio isn't a string or a numpy ndarray
        ValueError: When the factor is negative
        TypeError: When a samplerate is required and the wrong type is provided
        soundfile.LibsndfileError: When an error happens saving the output to a file

    Returns:
        Tuple[ndarray, int]: A tuple containing the stretched audio data and sample rate.
            This is returned whether or not the audio gets saved to a file.
    """

    # Type checks
    if not (isinstance(audio, str) or isinstance(audio, ndarray)):
        raise TypeError("'audio' must be the path to a audio file or a numpy ndarray")

    if factor <= 0:
        raise ValueError("'factor' must be greater than 0")

    if isinstance(audio, ndarray) and not isinstance(samplerate, int):
        try:
            samplerate = int(samplerate)
        except:
            raise TypeError(
                f"You must provide a valid sample rate when working with raw audio data (Not {type(samplerate)})"
            )

    # If a file path is provided, load it as a ndarray using soundfile
    if isinstance(audio, str):
        audio, samplerate = soundfile.read(audio)

    stretched_samplerate = round(samplerate / factor)

    if isinstance(output, str):
        try:
            soundfile.write(output, audio, samplerate=stretched_samplerate)
        except soundfile.LibsndfileError as exc:
            # Delete invalid file
            pathlib.Path(output).unlink()

            exc.prefix += "\n(Try saving it as a .wav file instead)\n"

            raise exc

    return (audio, stretched_samplerate)


def speedup_audio(
    audio: Union[str, ndarray],
    factor: float,
    output: Optional[str] = None,
    samplerate: Optional[int] = None,
) -> Tuple[ndarray, int]:
    """This function is used to change an audio's speed by a certain factor.

    Because this function doesn't apply any resampling or similar algorithms, for very low factors (around 0.2 or lower) the audio quality might decrease noticeably.

    Args:
        audio (Union[str, ndarray]): The audio to be sped up or down.
            You can provide either a path to a file containing your audio,
            or the raw sound data as a numpy ndarray.
        factor (float): This is the factor by which the speed of the audio will be changed.
            For example, a factor of 2 will make the audio twice as fast,
            and a factor of 0.5 will make the audio half as fast.
        output (Optional[str], optional): This is the path to which the sped up audio will be saved.
            If no argument is passed, it wont save the audio to a file.. Defaults to ``None``.
        samplerate (Optional[int], optional): The sample rate of the original audio.
            You only need to pass this argument if you've provided a numpy ndarray as the audio.
            Otherwise, it will be determined automatically. Defaults to ``None``.

    Raises:
        TypeError: When audio isn't a string or a numpy.ndarray
        ValueError: When the factor is negative
        TypeError: When a samplerate is required and the wrong type is provided
        soundfile.LibsndfileError: When an error happens saving the output to a file

    Returns:
        Tuple[ndarray, int]: A tuple containing the sped up audio data and sample rate.
            This is returned whether or not the audio gets saved to a file.
    """

    # Type checks
    if factor <= 0:
        raise ValueError("'factor' must be greater than 0")

    # Stretch audio to match the specified speedup factor
    return stretch_audio(
        audio=audio, factor=1 / factor, output=output, samplerate=samplerate
    )
