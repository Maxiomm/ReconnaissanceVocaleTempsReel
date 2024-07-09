from vosk import Model, KaldiRecognizer
import os
import pyaudio
from gestion_commandes import gerer_commande_smashmelee # A CHANGER A CHAQUE FOIS SELON LE JEU

model_path = r"C:\Users\maxio\Desktop\vosk-model-fr-0.22\vosk-model-fr-0.22"
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

# Variable d'état pour contrôler l'écoute des commandes
en_traitement = False

# Variable pour stocker le dernier message partiel reconnu
message_precedent = ""

def ecouter_et_reconnaitre():
    global en_traitement, message_precedent
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=400)
    stream.start_stream()
    print("\n\n-----Écoute en cours-----")

    while True:
        data = stream.read(400, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_dict = eval(result)
            texte = result_dict.get('text', '')
            print("\n")
        else:
            partial = recognizer.PartialResult()
            partial_dict = eval(partial)
            partial_text = partial_dict.get('partial', '')

            # Si le texte partiel est différent du message précédent, l'afficher et le mettre à jour
            if partial_text != message_precedent:
                print("\n", partial_text)
                message_precedent = partial_text

                if gerer_commande_smashmelee(partial_text) and not en_traitement: # A CHANGER A CHAQUE FOIS SELON LE JEU
                    recognizer.Reset()  # Réinitialise le recognizer
                    en_traitement = True  # Indique qu'une commande est en cours de traitement
            
            # Réinitialiser en_traitement après le traitement d'une commande pour être prêt à recevoir de nouvelles commandes
            if en_traitement:
                en_traitement = False
