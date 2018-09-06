import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load an audio file (replace 'your_audio_file.wav' with your file path)
audio_file = "your_audio_file.wav"

# Function to transcribe audio
def transcribe_audio(file_path):
    with sr.AudioFile(file_path) as source:
        # Record the audio file as an audio data object
        audio_data = recognizer.record(source)

        try:
            # Recognize the content from the audio input
            text = recognizer.recognize_google(audio_data)
            print("Transcription: " + text)



        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")

        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

# Transcribe the specified audio file
transcribe_audio(audio_file)
