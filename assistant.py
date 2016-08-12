#!/home/manish/.pyenv/shims/python3
import speech_recognition as sr
import os

if __name__ == "__main__":
# Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        string = r.recognize_google(audio)
        print("You said: " + string)
        #String(string.lower())
        string = string.lower()
        string = string.replace('\'',' is ')
        os.system('python3'+' query.py '+string)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
