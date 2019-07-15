#!/usr/bin/python3
import json
import fileinput
import base64
import sys

def get_audio_content_from_stdin():
    response = {}
    content = ""
    for line in fileinput.input():
        content += line

    response = json.loads(content)

    if 'audioContent' not in response:
        print("No audioContent property found")
        print(content)
        return None
    return response["audioContent"]

def write_audio_file(filename, content_base64):
    audio_content = base64.b64decode(content_base64)
    with open(filename, 'w+b') as myfile:
        myfile.write(audio_content)

def main():
    filename = "audio.mp3"
    if len(sys.argv) >= 2:
        filename = sys.argv[1]

    content_base64 = get_audio_content_from_stdin()
    write_audio_file(filename, content_base64)

main()