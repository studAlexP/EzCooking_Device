import speech_recognition as sr
import json


def main():
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                data = open("data/data.json", "w")
                json_text = str(text)
                json_text = json_text.split()
                json_data = {}
                json_data["keywords"] = json_text
                data.write(json.dumps(json_data))
                data.close()
                print(json_text)
            except:
                print("Failed")

if __name__ == "__main__":
    main()