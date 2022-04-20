import speech_recognition as sr

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            data = open("data/data.txt", "w")
            data.write(text)
            data.close()
            print(text)
        except:
            print("Failed")