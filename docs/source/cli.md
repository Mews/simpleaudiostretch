# CLI

You can use the command line interface to stretch your audios, through the `simplestretch` command.

## Required Arguments

| Short | Long       | Description                       | Type   |
|-------|------------|-----------------------------------|--------|
| `-a`  | `--audio`  | Path to the audio file            | String |
| `-f`  | `--factor` | Factor for the change in audio length/speed   | Float  |
| `-o`  | `--output` | Path for the output file          | String |

## Optional Arguments

| Short | Long      | Description                        | Type    |
|-------|-----------|------------------------------------|---------|
| `-s`  | `--speed` | Use this flag to target audio speed instead of length | Boolean |

## Example Commands

To stretch an audio file to 1.5 times its original size and save it:

```sh
simplestretch -a path/to/audio/file -f 1.5 -o path/to/output/file
```

To speed up an audio file to 2 times speed and save it:

```sh
simplestretch -a path/to/audio/file -f 2 -o path/to/output/file -s
```