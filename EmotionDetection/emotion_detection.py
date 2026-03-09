import json
import requests

def emotion_detector(text_to_analyse):
    
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=input_json, headers=headers)
    json_response = {}
    if response.status_code == 400:
        json_response['anger'] = None
        json_response['disgust'] = None
        json_response['fear'] = None
        json_response['joy'] = None
        json_response['sadness'] = None
        json_response['dominant_emotion'] = None
    else:
        emotions = json.loads(response.text)
        json_response['anger'] = float(emotions['emotionPredictions'][0]['emotion']['anger'])
        json_response['disgust'] = float(emotions['emotionPredictions'][0]['emotion']['disgust'])
        json_response['fear'] = float(emotions['emotionPredictions'][0]['emotion']['fear'])
        json_response['joy'] = float(emotions['emotionPredictions'][0]['emotion']['joy'])
        json_response['sadness'] = float(emotions['emotionPredictions'][0]['emotion']['sadness'])
        
        max_score = -100.0
        dominant_emotion = ""

        for emotion in json_response:
            if json_response[emotion] > max_score:
                max_score = json_response[emotion]
                dominant_emotion = emotion
        json_response['dominant_emotion'] = dominant_emotion

    return json_response