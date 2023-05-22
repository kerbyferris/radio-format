#! /usr/bin/python
import os
from sys import argv, exit

from pydub import AudioSegment, effects, exceptions

RADIO_MUSIC_DIR = "/home/kerby/Dropbox/music/radio-music/active/2"

help = """
Usage: radio-format [folder]

ex) $ radio-format ./

Pass a source folder. If nothing is passed the current directory will be used.
"""


def get_files(path="."):
    scandir_iter = os.scandir(path)
    return [
        item
        for item in scandir_iter
        if item.is_file and item.name.lower().endswith("wav")
    ]


def normalize_audio(wav_file_path):
    song = AudioSegment.from_wav(wav_file_path)
    return effects.normalize(song)


def main():
    try:
        src_dir = argv[1]
        files = get_files(src_dir)
    except IndexError as e:
        print(f"{help}\n\nError: {e}")
        exit()

    for file in files:
        try:
            normalized = normalize_audio(file.path)
            normalized.export(
                f"{RADIO_MUSIC_DIR}/{file.name}",
                format="WAV",
                parameters=["-ac", "1"],
            )
        except exceptions.CouldntDecodeError as e:
            print(f"Error decoding {file.path}: {e}")
            continue


if __name__ == "__main__":
    main()
