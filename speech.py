import speech_recognition as sr
import json
import os
import sys


def main():
    count = 0
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            audio = r.listen(source)

            try:
#               audio = r.listen(source)
                text = r.recognize_google(audio)
                data = open("data/data.json", "w")
                json_text = str(text)
                json_text = json_text.split()
                json_data = {}
                json_data["keywords"] = json_text
                data.write(json.dumps(json_data))
                data.close()
            except:
                print("Failed")
                count += 1
                #os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == "__main__":
    main()
