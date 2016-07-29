import sttClient
import json

from watson_developer_cloud import SpeechToTextV1
from os.path import join, dirname

def test():
    sttClient.Utils.getAuthenticationToken()
    speech_to_text = SpeechToTextV1(
        username='1b438e08-110f-4b25-943b-fb55c25db642',
        password='dMYfxV5dx0mQ',
        x_watson_learning_opt_out=False
    )
    stuff = ""
    with open(join(dirname(__file__), 'speech.wav'), 'rb') as audio_file:
        stuff += (json.dumps(speech_to_text.recognize(
            audio_file, content_type='audio/wav', timestamps=True), indent=2))
    

    return stuff
