import vosk
import wave
import os 
import json 

# Create record files
def get_text_from_voice(filename="static/recording.wav"):
    
    if not os.path.exists("static/vosk-model-small-en-in-0.4"):
        print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
        exit (1)

    wf = wave.open(filename, "rb")
    
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        exit (1)

    results = ""
    model = vosk.Model("static/vosk-model-small-en-in-0.4")
    rec = vosk.KaldiRecognizer(model, wf.getframerate())
    # rec.SetWords(True)
    anant = ""
    x = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            recognizerResult = rec.Result()
            x.append(recognizerResult)
    results = rec.FinalResult()
    x.append(results)
    for item in x:
        try:
            json_data = json.loads(item)
            text_value = json_data.get('text', '')
            anant += " " + text_value
            print("final result is :",text_value)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    return anant
