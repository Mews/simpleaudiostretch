
# simpleaudiostretch
[![Tests badge](https://github.com/Mews/simpleaudiostretch/actions/workflows/run_tests.yml/badge.svg)](https://github.com/Mews/simpleaudiostretch/actions/workflows/run_tests.yml)
[![Coverage badge](https://raw.githubusercontent.com/Mews/simpleaudiostretch/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/Mews/simpleaudiostretch/blob/python-coverage-comment-action-data/htmlcov/index.html)
[![Documentation badge](https://readthedocs.org/projects/simpleaudiostretch/badge/?version=latest&style=flat-default)](https://simpleaudiostretch.readthedocs.io/en/latest/simplestretch.html)
[![PyPI Version](https://badge.fury.io/py/simpleaudiostretch.svg)](https://pypi.python.org/pypi/simpleaudiostretch)

A simple python package to stretch audio files and change their speed.

## Installation

You can install the package by running the command `pip install simpleaudiostretch`

##  Features

- Supports many different audio formats, including mp3, wav, and also raw audio data in the form of numpy ndarrays.
- Its really fast, especially when working with raw audio data.
## Documentation

The full documentation for this package can be found [here](https://simpleaudiostretch.readthedocs.io/en/latest/simplestretch.html).
# Usage/Examples
## Python
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
## CLI

You can also use the command line interface to stretch your audios, through the `simplestretch` command.

### Required Arguments

| Short | Long       | Description                       | Type   |
|-------|------------|-----------------------------------|--------|
| `-a`  | `--audio`  | Path to the audio file            | String |
| `-f`  | `--factor` | Factor for the change in audio length/speed   | Float  |
| `-o`  | `--output` | Path for the output file          | String |

### Optional Arguments

| Short | Long      | Description                        | Type    |
|-------|-----------|------------------------------------|---------|
| `-s`  | `--speed` | Use this flag to target audio speed instead of length | Boolean |

### Example Commands

To stretch an audio file to 1.5 times its original size and save it:

```sh
simplestretch -a path/to/audio/file -f 1.5 -o path/to/output/file
```

To speed up an audio file to 2 times speed and save it:

```sh
simplestretch -a path/to/audio/file -f 2 -o path/to/output/file -s
```
# Support
If you have any issues using this package or would like to request features, you can [open an issue](https://github.com/Mews/simpleaudiostretch/issues/new) or contact me through [my discord!](https://discord.com/users/467268976523739157)

