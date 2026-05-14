import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyze } }
    emotion_predict_response = requests.post(url, json = myobj, headers=header)
    json_emotion_predict = json.loads(emotion_predict_response.text)
    emotions = json_emotion_predict['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key = emotions.get )
    emotions['dominant_emotion'] = dominant_emotion
    return emotions