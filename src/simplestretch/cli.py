import argparse

from . import speedup_audio, stretch_audio


def main():
    parser = argparse.ArgumentParser("Stretch an audio file or speed it up or down")

    parser.add_argument(
        "-a", "--audio", required=True, type=str, help="Path to the audio file"
    )
    parser.add_argument(
        "-f",
        "--factor",
        required=True,
        type=float,
        help="Factor for the change in audio length/speed",
    )
    parser.add_argument(
        "-o", "--output", required=True, type=str, help="Path for the output file"
    )
    parser.add_argument(
        "-s",
        "--speed",
        action="store_true",
        help="If this is passed, the factor will be applied to the speed of the audio rather than the length",
    )

    args = parser.parse_args()

    if args.speed:
        speedup_audio(audio=args.audio, factor=args.factor, output=args.output)

    else:
        stretch_audio(audio=args.audio, factor=args.factor, output=args.output)
