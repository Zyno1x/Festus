import speech_recognition as sr
from utils import logger


def listen_speech():
    '''
    It takes user's voice as input
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        logger.info(f"Recognized Command: {query}")
        return query

    except Exception as e:
        logger.error(str(e) + "Speech Unrecognized")
        print("I didn't recognize what you said, Can please repeat")
        return "None"
