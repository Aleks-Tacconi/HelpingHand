import speech_recognition as sr

r = sr.Recognizer()

def speak():
    while 1:
        try:
            with sr.Microphone() as source2:

                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio2 = r.listen(source2, timeout=5, phrase_time_limit=15)

                MyText = r.recognize_google(audio2)
                return MyText

        except sr.UnknownValueError:
            print("Error")

if __name__ == '__main__':
    print(speak())
