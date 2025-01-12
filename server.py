from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze) 
    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]
    dom = emotions["dominant_emotion"]
    common_msg = "For the given statement, the system response is "
    msg = f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness: {sadness}."
    final_msg = f"The dominant emotion is {dom}"

    return common_msg + msg + final_msg

@app.route("/")
def return_index_page():
    render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
