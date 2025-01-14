"""Init server to detect query emotions."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    """Collect query and return proper message."""
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze) # get emotions parse dict
    dom = emotions["dominant_emotion"]
    if emotions["dominant_emotion"] is None:
        msg = "Invalid text! Please try again!"
    else:
        msg = (
            "For the given statement, the system response is "
            f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
            f"'fear': {emotions['fear']}, 'joy': {emotions['joy']}, "
            f"'sadness': {emotions['sadness']}. The dominant emotion is {dom}."
        )
    return msg

@app.route("/")
def render_index_page():
    """Render index page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
