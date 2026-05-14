# Import the Flask class from the flask module --->flask --app server --debug run
from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, make_response, request, render_template


# Create an instance
#
# of the Flask class, passing in the name of the current module
app = Flask(__name__)

# root application
@app.route("/")
def render_index_page(): 
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_emotion():
    text = request.args.get('textToAnalyze') 
    emotions = emotion_detector(text)
    return make_response(emotions)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
