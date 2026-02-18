# simpleaudiostretch

**simpleaudiostretch** is a simple python package to stretch audio files and change their speed.

## Installation

You can install the package by running the command `pip install simpleaudiostretch`

## Usage/Examples

This is an example on how you might use this library\
In this example we take a file called `song.mp3` and make it twice as long:
```python
import simplestretch

# A factor of 2 means the song becomes twice as long
simplestretch.stretch_audio("song.mp3", 2, "out.wav")
```

You might also have the raw audio data, in which case you could do the following:
```python
import simplestretch, soundfile

# In this example we use soundfile to get the audio data
# But you can use any numpy ndarray representing audio
audio_data, samplerate = soundfile.read("song.mp3")

# When working with raw audio data
# You will also need to pass the audio's sample rate to the function
simplestretch.stretch_audio(audio_data, 2, output="out.wav", samplerate=samplerate)
```

You can also work with changes in speed rather than changes in length through the `speedup_audio` method:
```python
import simplestretch

# In this example we make the song twice as fast rather than twice as long
simplestretch.speedup_audio("song.mp3", 2, "out.wav")
```

For the full documentation for `stretch_audio` and `speedup_audio`, see the [api reference](api.md).

```{toctree}
:maxdepth: 2
:caption: Contents

api
cli
```
