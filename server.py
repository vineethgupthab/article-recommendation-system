# Launch with
#
# python app.py

from flask import Flask, render_template
import sys
import pickle

app = Flask(__name__)

@app.route("/")
def articles():
    """Show a list of article titles"""
    return render_template('articles.html',articles=articles_info)


@app.route("/article/<topic>/<filename>")
def article(topic, filename):
    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """

    top5 = recommended_info[(topic,filename)]
    title = top5[0]
    text = top5[1]
    return render_template('article.html',TITLE=title,text=text,recommended=top5)


f = open('articles.pkl', 'rb')
articles_info = pickle.load(f)
f.close()

f = open('recommended.pkl', 'rb')
recommended_info = pickle.load(f)
f.close()


# for local debug
if __name__ == '__main__':
    app.run(debug=True)

