"""
Audio tone files from https://www.mediacollege.com/audio/tone/download/
"""

import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

import pathlib
import unittest

import numpy as np
import soundfile
from simplestretch import speedup_audio, stretch_audio


class TestAudioFunctions(unittest.TestCase):
    def setUp(self):
        # Create a simple audio signal for testing
        self.sine_samplerate = 44100
        duration = 2  # seconds
        t = np.linspace(
            0, duration, int(self.sine_samplerate * duration), endpoint=False
        )
        self.sine_audio = 0.5 * np.sin(
            2 * np.pi * 440 * t
        )  # Generate a 440 Hz sine wave

    def test_stretch_audio_raw(self):
        factor = 2

        stretched_audio, stretched_samplerate = stretch_audio(
            audio=self.sine_audio, factor=factor, samplerate=self.sine_samplerate
        )

        self.assertEqual(self.sine_audio.all(), stretched_audio.all())

        self.assertEqual(round(self.sine_samplerate / factor), stretched_samplerate)

    def test_speedup_audio_raw(self):
        factor = 2

        spedup_audio, spedup_samplerate = speedup_audio(
            audio=self.sine_audio, factor=factor, samplerate=self.sine_samplerate
        )

        self.assertEqual(self.sine_audio.all(), spedup_audio.all())

        self.assertEqual(round(self.sine_samplerate / (1 / factor)), spedup_samplerate)

    def test_stretch_audio_file_wav(self):
        factor = 2
        file = "tests/sample_files/440hz.wav"

        audio, samplerate = soundfile.read(file)

        stretched_audio, stretched_samplerate = stretch_audio(audio=file, factor=factor)

        self.assertEqual(audio.all(), stretched_audio.all())

        self.assertEqual(round(samplerate / factor), stretched_samplerate)

    def test_stretch_audio_file_mp3(self):
        factor = 2
        file = "tests/sample_files/440hz.mp3"

        audio, samplerate = soundfile.read(file)

        stretched_audio, stretched_samplerate = stretch_audio(audio=file, factor=factor)

        self.assertEqual(audio.all(), stretched_audio.all())

        self.assertEqual(round(samplerate / factor), stretched_samplerate)

    def test_speedup_audio_file_wav(self):
        factor = 2
        file = "tests/sample_files/440hz.wav"

        audio, samplerate = soundfile.read(file)

        spedup_audio, spedup_samplerate = speedup_audio(audio=file, factor=factor)

        self.assertEqual(audio.all(), spedup_audio.all())

        self.assertEqual(round(samplerate / (1 / factor)), spedup_samplerate)

    def test_speedup_audio_file_mp3(self):
        factor = 2
        file = "tests/sample_files/440hz.wav"

        audio, samplerate = soundfile.read(file)

        spedup_audio, spedup_samplerate = speedup_audio(audio=file, factor=factor)

        self.assertEqual(audio.all(), spedup_audio.all())

        self.assertEqual(round(samplerate / (1 / factor)), spedup_samplerate)

    def test_stretch_save_audio_file(self):
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
        self.assertTrue(path.is_file())

        # Assert the file contents are correct
        out_audio, out_samplerate = soundfile.read(out_file)

        self.assertEqual(self.sine_audio.all(), out_audio.all())

        self.assertEqual(round(self.sine_samplerate / factor), out_samplerate)

    def test_speedup_save_audio_file(self):
        factor = 2
        out_file = "tests/test_files/speedup_save_test.wav"

        speedup_audio(
            audio=self.sine_audio,
            factor=factor,
            output=out_file,
            samplerate=self.sine_samplerate,
        )

        # Assert the file exists
        path = pathlib.Path(out_file)
        self.assertTrue(path.is_file())

        # Assert the file contents are correct
        out_audio, out_samplerate = soundfile.read(out_file)

        self.assertEqual(self.sine_audio.all(), out_audio.all())

        self.assertEqual(round(self.sine_samplerate / (1 / factor)), out_samplerate)


if __name__ == "__main__":
    unittest.main() # pragma: no cover