'''
This is the server.py file
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

'''
this renders index page
'''
@app.route ('/')
def render_index_page():
    return render_template("index.html")

'''
this handles get request
'''
@app.route('/emotionDetector')
def request_get():
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    output = f"For the given statement, the system response is \
                'anger': {response['anger']}, \
                'disgust': {response['disgust']}, \
                'fear': {response['fear']}, \
                'joy': {response['joy']}, \
                'sadness': {response['sadness']}. \
                The dominant emotion is {response['dominant_emotion']}."
    return output

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
