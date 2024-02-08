from flask import Flask, request, render_template
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

@app.route('/', methods=['GET', 'POST'])
def sentiment_analysis():
    result = ""
    user_input = ""

    if request.method == 'POST':
        if 'reset' in request.form:
            user_input = ""
            result = ""
        else:
            user_input = request.form['user_input']
            sentiment_scores = sia.polarity_scores(user_input)
            compound_score = sentiment_scores['compound']
            print(sentiment_scores)
            if compound_score >= 0.05:
                result = "Positive"
            elif compound_score <= -0.05:
                result = "Negative"
            else:
                result = "Neutral"

    return render_template('index.html', result=result, user_input=user_input)

#if __name__ == '__main__':
#    app.run(debug=True)