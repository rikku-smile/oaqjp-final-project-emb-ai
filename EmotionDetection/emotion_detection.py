import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=headers)
    prettyresponse = json.loads(response.text)
    # All the emotions are already a dict
    emotions = prettyresponse["emotionPredictions"][0]["emotion"].copy() #create new object
    # Add dominant as another key of the dictionary
    emotions["dominant_emotion"] = max(emotions, key=emotions.get)
    return emotions