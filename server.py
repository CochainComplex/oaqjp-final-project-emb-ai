from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    
    result = emotion_detection(text_to_analyze)

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']

    dominant_emotion = result['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <strong>{dominant_emotion}</strong>."
    )

    return response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
