
# simpleaudiostretch

A simple python package to stretch audio files and change their speed.

## Installation

You can install the package by running the command\
`pip install simpleaudiostretch`
##  Features

- Supports many different audio formats, including mp3, wav, and also raw audio data in the form of numpy ndarrays.
- Its incredibly fast when working with raw audio data.
## Usage/Examples

**The full documentation for this package can be found [here](https://simpleaudiostretch.readthedocs.io/en/latest/simplestretch.html)**.

This is an example on how you might use this library\
In this example we take a file called `song.mp3` and make it twice as long:
```python
import simplestretch

#A factor of 2 means the song becomes twice as long
simplestretch.stretch_audio("song.mp3", 2, "out.wav")
```

You might also have the raw audio data, in which case you could do the following:
```python
import simplestretch, soundfile

# In this example we use soundfile to get the audio data
# But you can use any numpy ndarray representing audio
audio_data, samplerate = soundfile.read("song.mp3")

#When working with raw audio data
#You will also need to pass the audio's sample rate to the function
simplestretch.stretch_audio(audio_data, 2, output="out.wav", samplerate=samplerate)
```

You can also work with changes in speed rather than changes in length through the `speedup_audio` method:
```python
import simplestretch

#In this example we make the song twice as fast rather than twice as long
simplestretch.speedup_audio("song.mp3", 2, "out.wav")
```
## Support
If you have any issues using this package or would like to request features, you can [open an issue](https://github.com/Mews/simpleaudiostretch/issues/new) or contact me through [my discord!](https://discord.com/users/467268976523739157)

