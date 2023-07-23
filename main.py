import speech_recognition as sr
from googletrans import Translator
import logging

def translate_speech_to_english():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Habla ahora...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="es-ES")
            logging.info("Texto reconocido: ", text)

            translator = Translator()
            translated_text = translator.translate(text, dest="en").text
            logging.info("Traducción a inglés: ", translated_text)

        except sr.UnknownValueError:
            logging.error("No se pudo reconocer el habla.")
        except sr.RequestError as e:
            logging.error("Error al solicitar los resultados del servicio de reconocimiento de voz; {0}".format(e))
        except Exception as e:
            logging.error("Error en la traducción; {0}".format(e))

if __name__ == "__main__":
    translate_speech_to_english()
