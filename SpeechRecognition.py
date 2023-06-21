import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def speak_text(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while True:
    try:
        # Use the microphone as the source for input
        with sr.Microphone() as source:
            # Wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Listening...")
            # Listens for the user's input
            audio = r.listen(source, timeout=10)
            print("Processing...")
            # Using Google to recognize audio
            text = r.recognize_google(audio)
            text = text.lower()
            print("You said:", text)
            speak_text(text)
    except sr.RequestError as e:
        print("Could not request results: {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occurred")