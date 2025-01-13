from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    # collect the query
    text_to_analyze = request.args.get('textToAnalyze')
    # get emotions parse dict
    emotions = emotion_detector(text_to_analyze)
    dom = emotions["dominant_emotion"]
    if dom is None:
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
    # render index
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
