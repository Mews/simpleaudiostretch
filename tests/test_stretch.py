"""
Audio tone files from https://www.mediacollege.com/audio/tone/download/
"""

import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

import pathlib

import numpy as np
import pytest
import soundfile
from simplestretch import stretch_audio


class TestStretch:
    # Create a simple audio signal for testing
    sine_samplerate = 44100
    duration = 2  # seconds
    t = np.linspace(0, duration, int(sine_samplerate * duration), endpoint=False)
    sine_audio = 0.5 * np.sin(2 * np.pi * 440 * t)  # Generate a 440 Hz sine wave

    def test_stretch_audio_raw(self):
        factor = 2

        stretched_audio, stretched_samplerate = stretch_audio(
            audio=self.sine_audio, factor=factor, samplerate=self.sine_samplerate
        )

        assert self.sine_audio.all() == stretched_audio.all()

        assert round(self.sine_samplerate / factor) == stretched_samplerate

    def test_stretch_audio_file_wav(self):
        factor = 2
        file = "tests/sample_files/440hz.wav"

        audio, samplerate = soundfile.read(file)

        stretched_audio, stretched_samplerate = stretch_audio(audio=file, factor=factor)

        assert audio.all() == stretched_audio.all()

        assert round(samplerate / factor) == stretched_samplerate

    def test_stretch_audio_file_mp3(self):
        factor = 2
        file = "tests/sample_files/440hz.mp3"

        audio, samplerate = soundfile.read(file)

        stretched_audio, stretched_samplerate = stretch_audio(audio=file, factor=factor)

        assert audio.all() == stretched_audio.all()

        assert round(samplerate / factor) == stretched_samplerate

    def test_stretch_save_audio_file_wav(self):
        factor = 2
        out_file = "tests/test_files/stretch_save_test.wav"

        stretch_audio(
            audio=self.sine_audio,
            factor=factor,
            output=out_file,
            samplerate=self.sine_samplerate,
        )

        # Assert the file exists
        path = pathlib.Path(out_file)
        assert path.is_file()

        # Assert the file contents are correct
        out_audio, out_samplerate = soundfile.read(out_file)

        assert self.sine_audio.all() == out_audio.all()

        assert round(self.sine_samplerate / factor) == out_samplerate

    def test_stretch_invalid_audio_type(self):
        factor = 2

        # Pass an invalid audio data type
        with pytest.raises(TypeError):
            stretch_audio(audio=None, factor=factor, samplerate=self.sine_samplerate)

    def test_stretch_invalid_factor_zero(self):
        with pytest.raises(ValueError):
            stretch_audio(
                audio=self.sine_audio, factor=0, samplerate=self.sine_samplerate
            )

    def test_stretch_invalid_factor_negative(self):
        with pytest.raises(ValueError):
            stretch_audio(
                audio=self.sine_audio, factor=-1, samplerate=self.sine_samplerate
            )

    def test_stretch_raw_data_no_samplerate(self):
        factor = 2

        with pytest.raises(TypeError):
            stretch_audio(audio=self.sine_audio, factor=factor)

    def test_stretch_raw_data_invalid_samplerate(self):
        factor = 2

        with pytest.raises(TypeError):
            stretch_audio(audio=self.sine_audio, factor=factor, samplerate="")

    def test_stretch_raw_data_float_samplerate(self):
        factor = 2

        stretched_audio, stretched_samplerate = stretch_audio(
            audio=self.sine_audio, factor=factor, samplerate=float(self.sine_samplerate)
        )

        assert self.sine_audio.all() == stretched_audio.all()

        assert round(self.sine_samplerate / factor) == stretched_samplerate

    def test_stretch_save_invalid_mp3_samplerate(self):
        factor = 0.5

        out_file = "tests/test_files/stretch_invalid_mp3_save_test.mp3"

        with pytest.raises(soundfile.LibsndfileError):
            stretch_audio(
                audio=self.sine_audio,
                factor=factor,
                output=out_file,
                samplerate=self.sine_samplerate,
            )

        # Assert file was deleted
        assert not pathlib.Path(out_file).exists()